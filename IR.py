from llvmlite import ir
import llvmlite.binding as llvm
import strings
import copy
from ctypes import CFUNCTYPE, c_int, c_float

# declare types
i1 = ir.IntType(1)
i32 = ir.IntType(32)
f32 = ir.FloatType()

def initialize():
    # Initialize llvm
    llvm.initialize()
    llvm.initialize_native_target()
    llvm.initialize_native_asmprinter()


def ir_type(string):
    if "ref" in string:
        if "int" in string:
            return ir.PointerType(i32)
        return ir.PointerType(f32)
    if "int" in string:
        return i32
    if "float" in string:
        return f32
    if "bool" in string:
        return i1
    return ir.VoidType()


def convert_extern(extern, module, *sysArgs):
    returnType = ir_type(extern["ret_type"])

    args = list()
    if "tdecls" in extern:
        for arg in extern["tdecls"]["types"]:
            args.append(ir_type(arg))

    if extern["globid"] == "getarg":
        getArg(module, *sysArgs)

    elif extern["globid"] == "getargf":
        getArgf(module, *sysArgs)
        pass

    else:
        fnty = ir.FunctionType(returnType, args)
        func = ir.Function(module, fnty, name=extern["globid"])


def getArg(module, sysArgs):
    sysArgs = [
        int(float(value)) for value in sysArgs
    ]
    array_type = ir.ArrayType(i32, len(sysArgs))
    arr = ir.Constant(array_type, sysArgs)

    fnty = ir.FunctionType(i32, [i32])
    func = ir.Function(module, fnty, name = "getarg")
    entry = func.append_basic_block("entry")
    builder = ir.IRBuilder(entry)

    ptr = builder.alloca(array_type)

    index = func.args[0]
    ptr_arg = builder.alloca(i32)
    builder.store(index, ptr_arg)
    value = builder.load(ptr_arg)


    for number, arg in enumerate(sysArgs):
        int_1 = ir.Constant(i32, arg)
        builder.insert_value(arr, int_1, number)
    builder.store(arr, ptr)


    int_0 = ir.Constant(i32, 0)

    address = builder.gep(ptr, [int_0,value])
    builder.ret(builder.load(address))


def getArgf(module, sysArgs):
    sysArgs = [float(value) for value in sysArgs]
    array_type = ir.ArrayType(f32, len(sysArgs))
    arr = ir.Constant(array_type, sysArgs)

    fnty = ir.FunctionType(f32, [i32])
    func = ir.Function(module, fnty, name = "getargf")
    entry = func.append_basic_block("entry")
    builder = ir.IRBuilder(entry)

    ptr = builder.alloca(array_type)

    #function arguments
    index = func.args[0]
    ptr_arg = builder.alloca(i32)
    builder.store(index, ptr_arg)
    value = builder.load(ptr_arg)


    for number, arg in enumerate(sysArgs):
        float_1 = ir.Constant(f32, arg)
        builder.insert_value(arr, float_1, number)
    builder.store(arr, ptr)

    int_0 = ir.Constant(i32, 0)

    address = builder.gep(ptr, [int_0,value])
    builder.ret(builder.load(address))


def convert_func(ast, module, known_funcs):
    func_name = ast[strings.globid]
    symbols = {}
    symbols['cint'] = set()
    symbols[strings.cint_args] = {}
    symbols[strings.cint_args][func_name] = []

    returnType = ir_type(ast[strings.ret_type])
    
    # find arguments
    argument_types = list()
    args = ()
    if strings.vdecls in ast:
        funcArgs = vdecls(ast[strings.vdecls], symbols, func_name)
        argument_types = funcArgs[0]
        args = funcArgs[1]

    fnty = ir.FunctionType(returnType, argument_types)
    func = ir.Function(module, fnty, name=func_name)
    known_funcs[func_name] = (fnty, symbols[strings.cint_args][func_name]) # add parameter info
    populate_known_funcs(symbols, known_funcs)


    entry = func.append_basic_block('entry')
    builder = ir.IRBuilder(entry)

    for index, value in enumerate(func.args):
        var_name = args[index]
        var_type = argument_types[index]

        if var_type.is_pointer:
            ptr = value
            symbols[var_name] = ptr
        else:
            ptr = builder.alloca(var_type)
            symbols[var_name] = ptr
            builder.store(value, ptr)

    returned = pure_blk(ast[strings.blk], builder, symbols)
    if ast[strings.ret_type] == 'void':
        builder.ret_void()
        return fnty
    if not returned:
        raise RuntimeError("function missing return statement")


def pure_blk(blk, builder, symbols):
    if strings.contents not in blk:
        return None
    legacy = copy.copy(symbols)
    returned = False
    for statement in blk[strings.contents][strings.stmts]:
        returned = stmt(statement, builder, legacy) or returned
        if returned:
            return returned
    return returned


def populate_known_funcs(symbols, known_funcs):
    for name, t in known_funcs.items():
        symbols[name] = t[0]


def vdecls(vdec, symbols, function_name):
    variables = vdec["vars"]
    variableList = list()
    args = list()
    for i in variables:
        variableList.append(ir_type(i["type"]))
        args.append(i["var"])
    return [variableList, args]


def blk_stmt(stmt, builder, symbols):
    return pure_blk(stmt[strings.contents], builder, symbols)


def stmt(ast, builder, symbols):
    name = ast["name"]
    if name == 'while':
        whileStmt(ast, builder, symbols)

    elif name == 'if':
        return ifStmt(ast, builder, symbols)

    elif name == 'ret':
        return returnStmt(ast, builder, symbols)

    elif name == 'vardeclstmt':
        vardeclstmt(ast, builder, symbols)

    elif name == 'expstmt':
        expression(ast[strings.exp], symbols, builder)

    elif name == 'blk':
        return blk_stmt(ast, builder, symbols)

    elif name == strings.printStmt:
        print_number(ast, builder, symbols)

    elif name == 'printslit':
        print_slit(ast, builder, symbols)

    else:
        raise RuntimeError('this is not processed: ' + str(ast))


def print_number(ast, builder, symbols):
    '''
    print i1, i32, f32
    note: the floar need to be converted to double when using printf
    '''
    value = expression(ast["exp"], symbols, builder)
    if value.type.is_pointer:
        value = builder.load(value)
    if value.type == i1:
        value = builder.zext(value, i32)
    if value.type == f32:
        value = builder.fpext(value, ir.DoubleType())
    voidptr_ty = ir.IntType(8).as_pointer()
    fmt = "%i \n\0" if value.type == i32 else "%f \n\0"
    c_fmt = ir.Constant(ir.ArrayType(ir.IntType(8), len(fmt)), bytearray(fmt.encode("utf8")))
    global_fmt = get_global_format(builder, str(value.type), c_fmt)
    fmt_arg = builder.bitcast(global_fmt, voidptr_ty)
    fn = builder.module.globals.get('printf')
    builder.call(fn, [fmt_arg, value])


def print_slit(ast, builder, symbols):
    '''
    print string with printf
    note: string need 
    '''
    string = ast['string']
    if len(string) == 0:
        return None
    voidptr_ty = ir.IntType(8).as_pointer()
    fmt = string + " \n\0"
    c_fmt = ir.Constant(ir.ArrayType(ir.IntType(8), len(fmt)), bytearray(fmt.encode("utf8")))
    global_fmt = get_global_format(builder, string, c_fmt)
    fmt_arg = builder.bitcast(global_fmt, voidptr_ty)
    fn = builder.module.globals.get('printf')
    builder.call(fn, [fmt_arg])


def get_global_format(builder, name, value):
    if name in builder.module.globals:
        return builder.module.globals[name]
    else:
        # code from https://blog.usejournal.com/writing-your-own-programming-language-and-compiler-with-python-a468970ae6df
        glob = ir.GlobalVariable(builder.module, value.type, name = name)
        glob.linkage = 'internal'
        glob.global_constant = True
        glob.initializer = value
        return glob


def whileStmt(ast, builder, symbols):
    w_body_block = builder.append_basic_block("w_body")
    w_after_block = builder.append_basic_block("w_after")

    # head
    cond_head = expression(ast[strings.cond], symbols, builder)
    builder.cbranch(cond_head, w_body_block, w_after_block)
    # body
    builder.position_at_start(w_body_block)
    stmt(ast["stmt"], builder, symbols)
    cond_body = expression(ast[strings.cond], symbols, builder)
    builder.cbranch(cond_body, w_body_block, w_after_block)
    # after
    builder.position_at_start(w_after_block)


def ifStmt(ast, builder, symbols):
    cond = expression(ast["cond"], symbols, builder)
    returned = False
    entry = builder.block
    if "else_stmt" in ast:
        with builder.if_else(cond) as (then, otherwise):
            with then:
                returned_then = stmt(ast["stmt"], builder, symbols)
            with otherwise:
                returned_else = stmt(ast["else_stmt"], builder, symbols)
        returned = returned_then and returned_else

    else:
        with builder.if_then(cond):
            stmt(ast["stmt"], builder, symbols)
    if returned:
        endif = builder.block
        builder.function.blocks.remove(endif)
    return returned



def returnStmt(ast, builder, symbols):
    if "exp" in ast:
        ret_exp = expression(ast["exp"], symbols, builder)
        if ret_exp.type.is_pointer:
            return builder.ret(builder.load(ret_exp))
        builder.ret(ret_exp)
    else:
        builder.ret_void()
    return True


def vardeclstmt(ast, builder, symbols):
    var_declaration = ast[strings.vdecl]
    var_type = var_declaration[strings.typ]
    var_name = var_declaration[strings.var]
    if 'ref' in var_type:
        return ref_var_decl_stmt(ast, builder, symbols)

    vtype = to_ir_type(var_type)
    ptr = builder.alloca(vtype)
    symbols[var_name] = ptr
    exp = ast[strings.exp]
    value = expression(exp, symbols, builder)
    if value.type.is_pointer:
        value = builder.load(value)

    if vtype != value.type:
        if vtype == f32:
            value = builder.uitofp(value, f32)
        if vtype == i32:
            if value.type == i1:
                value = builder.zext(value, i32)
            value = builder.fptosi(value, i32)

    try:
        builder.store(value, ptr)
    except TypeError as err:
        raise RuntimeError('error converting: ' + str(ast), err)


def ref_var_decl_stmt(ast, builder, symbols):
    var_declaration = ast[strings.vdecl]
    var_type = var_declaration[strings.typ]
    var_name = var_declaration[strings.var]
    exp = ast[strings.exp]
    pointee = expression(exp, symbols, builder)
    symbols[var_name] = pointee


def binary_convert(builder, il):
    if il.type.is_pointer:
        il = builder.load(il)
    if il.type == i32:
        il = builder.uitofp(il, f32)
    if il.type == f32:
        il = builder.fptosi(il, i1)

    return il


def extract_value(exp, builder):
    if exp.type.is_pointer:
        return builder.load(exp)
    return exp


def binop(ast, symbols, builder, target_type):
    lhs = expression(ast["lhs"], symbols, builder)
    rhs = expression(ast["rhs"], symbols, builder)
    lhs = extract_value(lhs, builder)
    rhs = extract_value(rhs, builder)
    exp_type = target_type
    op = ast["op"]


    if lhs.type != i1 and rhs.type != i1:
        if op != "and" and op != "or":
            if "float" in exp_type:
                if lhs.type != f32:
                    lhs = builder.uitofp(lhs, f32)
                if rhs.type != f32:
                    rhs = builder.uitofp(rhs, f32)

            if "int" in exp_type:
                if lhs.type != i32:
                    lhs = builder.fptosi(lhs, i32)
                if rhs.type != i32:
                    rhs = builder.fptosi(rhs, i32)

    flags = list()
    if "float" == target_type:
        flags= ["fast"]

    try:
        if op == "and":
            if lhs.type != rhs.type:
                lhs = binary_convert(builder, lhs)
                rhs = binary_convert(builder, rhs)
            return builder.and_(lhs, rhs, name="and", flags = flags)
        elif op == "or":
            if lhs.type != rhs.type:
                lhs = binary_convert(builder, lhs)
                rhs = binary_convert(builder, rhs)
            return builder.or_(lhs, rhs, name="or", flags = flags)
        elif "int" in exp_type:
            if op == 'mul':
                return builder.mul(lhs, rhs, name='mul')
            elif op == 'div':
                return builder.sdiv(lhs, rhs, name='div')
            elif op == 'add':
                return builder.add(lhs, rhs, name="add")
            elif op == 'sub':
                return builder.sub(lhs, rhs, name='sub')
            elif op == 'eq':
                return builder.icmp_signed('==', lhs, rhs, name="eq")
            elif op == 'lt':
                return builder.icmp_signed('<', lhs, rhs, name="lt")
            elif op == 'gt':
                return builder.icmp_signed('>', lhs, rhs, name="gt")
        elif "float" in exp_type:
            if op == 'mul':
                return builder.fmul(lhs, rhs, name='mul', flags = flags)
            elif op == 'div':
                return builder.fdiv(lhs, rhs, name='div', flags = flags)
            elif op == 'add':
                return builder.fadd(lhs, rhs, name="add", flags = flags)
            elif op == 'sub':
                return builder.fsub(lhs, rhs, name='sub', flags = flags)
            elif op == 'eq':
                return builder.fcmp_ordered('==', lhs, rhs, name="eq", flags = flags)
            elif op == 'lt':
                return builder.fcmp_ordered('<', lhs, rhs, name="lt", flags = flags)
            elif op == 'gt':
                return builder.fcmp_ordered('>', lhs, rhs, name="gt", flags = flags)
        elif "bool" in exp_type:
            if "int" in ast["lhs"]["type"]:
                if op == 'eq':
                    return builder.icmp_signed('==', lhs, rhs, name="eq")
                elif op == 'lt':
                    return builder.icmp_signed('<', lhs, rhs, name="lt")
                elif op == 'gt':
                    return builder.icmp_signed('>', lhs, rhs, name="gt")
            elif "float" in ast["lhs"]["type"]:
                if op == 'eq':
                    return builder.fcmp_ordered('==', lhs, rhs, name="eq", flags = flags)
                elif op == 'lt':
                    return builder.fcmp_ordered('<', lhs, rhs, name="lt", flags = flags)
                elif op == 'gt':
                    return builder.fcmp_ordered('>', lhs, rhs, name="gt", flags = flags)
            else:
                pass
    except ValueError as err:
        raise RuntimeError('error processing: ' + str(ast), err)
    except AttributeError as err:
        raise RuntimeError('error processing: ' + str(ast), err)

def check_int(lhs, rhs, builder, op):
    result = None
    if op == 'mul':
        result = builder.smul_with_overflow(lhs, rhs, name='mul')
    elif op == 'div':
        a = builder.sdiv(lhs, rhs, name='div')
        l = builder.icmp_signed('==', lhs, ir.Constant(i32,-2147483648 ), name="eq")
        r = builder.icmp_signed('!=', rhs, ir.Constant(i32,-1), name="nq")
        cond = builder.mul(l, r, name='mul')

        with builder.if_else(cond) as (then, otherwise):
            with then:
                pass
            with otherwise:
                lhs = check_int(lhs, ir.Constant(i32, -1), builder, 'mul')
                rhs = check_int(rhs, ir.Constant(i32, -1), builder, 'mul')
        return a

    elif op == 'add':
        result = builder.sadd_with_overflow(lhs, rhs, name="add")
    elif op == 'sub':
        result = builder.ssub_with_overflow(lhs, rhs, name='sub')
    
    if result is not None:
        is_overflow = builder.extract_value(result, 1)

        with builder.if_then(is_overflow):
            overflows(None, builder)


        return builder.extract_value(result, 0)


    if op == 'eq':
        return builder.icmp_signed('==', lhs, rhs, name="eq")
    elif op == 'lt':
        return builder.icmp_signed('<', lhs, rhs, name="lt")
    elif op == 'gt':
        return builder.icmp_signed('>', lhs, rhs, name="gt")


class Error2147483648(Exception):
    pass


def uop(ast, symbols, builder):
    try:
        uop_value = expression(ast["exp"], symbols, builder, neg=True, exception=True)
    except Error2147483648:
        return ir.Constant(i32, -2147483648)
    if uop_value.type.is_pointer:
        uop_value = builder.load(uop_value)
    if ast["type"] == "minus":
        if uop_value.type == i32:
            return builder.neg(uop_value, name="Minus")
        else:
            f32_0 = ir.Constant(f32, 0)
            return builder.fsub(f32_0, uop_value, name='sub', flags = ["fast"])
    else:
        return builder.not_(uop_value, name="logicalNeg")


def deference(builder, p):
    if p.type.is_pointer:
        return builder.load(p)
    return p


def expression(ast, symbols, builder, neg=False, exception=False):
    name = ast[strings.name]
    try:
        if name == strings.uop:
            return uop(ast, symbols, builder)
        if name == strings.litExp or name == "flit":
            r = ir.Constant(to_ir_type(ast['type']), ast['value'])
            return r
        if name == strings.slitExp:
            return ast["value"]
        if name == strings.varExp:
            id = ast[strings.var]
            try:
                return symbols[id]
            except TypeError as err:
                raise RuntimeError('error parsing: ' + str(ast), err)
        if name == strings.funcCallExp:
            function_name = ast[strings.globid]
            fn = builder.module.globals.get(function_name)
            params = ast[strings.params]
            parameters = []
            if function_name != "getarg" and function_name != "getargf":
                parameters = prepare_parameters(function_name, symbols, params, builder)
            else:
                parameters = [
                    deference(
                        builder,
                        expression(param, symbols, builder)
                    ) for param in params[strings.exps]
                ]

            return builder.call(fn, parameters)
        if name == strings.binop:
            target_type = ast[strings.typ]
            return binop(ast, symbols, builder, target_type)

        if name == strings.assign:
            var_name = ast[strings.var]

            if var_name not in symbols:
                raise RuntimeError(f'{var_name} has not been defined')

            ptr = symbols[var_name]

            value = expression(ast[strings.exp], symbols, builder)
            store_helper(builder, ptr, value)
            return None
        
        if name == strings.caststmt:
            target_type = ir_type(ast[strings.typ])
            source_type = ir_type(ast[strings.exp][strings.typ])
            value = expression(ast[strings.exp], symbols, builder)
            if source_type == target_type:
                return value
            else:
                if source_type == f32 and target_type == i32:
                    return builder.fptosi(value, target_type, name='fptosi')
                elif source_type == i32 and target_type == f32:
                    return builder.sitofp(value, target_type, name='fptosi')
                else:
                    # need to be handled
                    pass

        raise RuntimeError('Not processed: ' + str(ast))

    except KeyError as err:
        raise RuntimeError('error converting: ' + str(ast), err)


def prepare_parameters(function_name, symbols, params, builder):
    parameters = []
    if len(params) > 0:
        fnArgs = symbols[function_name].args
        for index in range(len(params[strings.exps])):
            param = params[strings.exps][index]
            argType = fnArgs[index]
            if argType.is_pointer:
                if strings.var not in param:
                    raise RuntimeError("non-variable object passed as ref type")
                var_name = param[strings.var]
                parameters.append(
                    symbols[var_name]
                )
            else:
                value = expression(param, symbols, builder)
                parameters.append(
                    deference(
                        builder,
                        value
                    )
                )
    return parameters

def store_helper(builder, ptr, value):
    if value.type.is_pointer:
        value = builder.load(value)

    if ptr.type.pointee == i32:
        if value.type == i1:
            value = builder.uitofp(value, f32)
        if value.type == f32:
            value = builder.fptosi(value, ptr.type.pointee)
    elif ptr.type.pointee == f32:
        if value.type == i1 or value.type == i32:
            value = builder.uitofp(value, f32)

    builder.store(value, ptr)
    return None


def to_ir_type(_type):
    return ir_type(_type)

def overflows(ast, builder):
    ast = {"string": "Error: int value overflowed", "name": "slit"}
    printStmt(ast, builder, None)

def convert_externs(ast, module, *sysArgs):
    externList = ast[strings.externs]
    for i in externList:
        convert_extern(i, module, *sysArgs)


def convert_funcs(ast, module, known_funcs):
    funcList = ast[strings.funcs]
    for i in funcList:
        convert_func(i, module, known_funcs)


def convert(ast, module, *sysArgs):
    if strings.externs in ast:
        convert_externs(ast[strings.externs], module, *sysArgs)
    known_funcs = ast["funcList"]
    declare_print_function(module, known_funcs)
    convert_funcs(ast[strings.funcs], module, known_funcs)


def declare_print_function(module, known_funcs):
    '''
    Declare printf function
    Code from https://blog.usejournal.com/writing-your-own-programming-language-and-compiler-with-python-a468970ae6df
    '''
    voidptr_ty = ir.IntType(8).as_pointer()
    fnty = ir.FunctionType(ir.IntType(32), [voidptr_ty], var_arg=True)
    printf = ir.Function(module, fnty, name="printf")
    known_funcs["printf"] = "slit"


def mainFunc(ast, *args):
    initialize()
    module = ir.Module(name="prog")
    module.triple = llvm.get_default_triple()
    convert(ast, module, *args)
    return module

# -jit handler
def llvm_bind(module, *args, optimize = False):
    llvm_ir_parsed = llvm.parse_assembly(str(module))
    llvm_ir_parsed.verify()

    target_machine = llvm.Target.from_default_triple().create_target_machine()
    engine = llvm.create_mcjit_compiler(llvm_ir_parsed, target_machine)
    engine.finalize_object()
    entry = engine.get_function_address("run")
    cfunc = CFUNCTYPE(c_int)(entry)
    result = cfunc()
    print("\nprogram returns: {}".format(result))
    return llvm_ir_parsed
