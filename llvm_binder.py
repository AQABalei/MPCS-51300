import llvmlite.binding as llvm
from ctypes import CFUNCTYPE, c_int, c_float

def bind(module, *args, optimize = False):
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
