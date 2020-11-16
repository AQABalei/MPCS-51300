import argparse
import sys
import ekparser
import utils
import semanticsChecker
import ir

def fuzztest(source_code):
    ast = ekparser.getAst(source_code)
    if not ast:
        print('no valid ast')
        sys.exit(-1)
    semanticsChecker.check(ast)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('source_file', metavar='source_file', help='input file name')
    parser.add_argument('-emit-ast', action='store_true', default=False,
                        dest='boolean_emit_ast', help='generate ast and save as yaml file')

    parser.add_argument('-emit-ir', action='store_true',
                    default=False,
                    dest='boolean_emit_ir',
                    help='generate ir')
    parser.add_argument('-jit', action='store_true',
                    default=False,
                    dest='boolean_jit',
                    help='generate ast')
    parser.add_argument('sysarg', nargs='*')
    args = parser.parse_args()

    source_code = utils.readFile(args.source_file)
    ast = ekparser.getAst(source_code)

    if not ast:
        print('no valid ast')
        sys.exit(-1)
    
    # check semantic errors
    semanticsChecker.check(ast)

    if args.boolean_emit_ast:
        utils.emit_ast(args.source_file.rsplit('.', 1)[0] + '.ast.yaml', ast)
    
    #assignment 3
    module = ir.mainFunc(ast, args.sysarg)

    if args.boolean_emit_ir:
        utils.emit_ir(args.source_file.rsplit('.', 1)[0] + '.ll', module)

    if args.boolean_jit:
        module = ir.llvm_bind(module, args.sysarg, optimize = False)

    sys.exit(0)

if __name__== "__main__":
    main()
