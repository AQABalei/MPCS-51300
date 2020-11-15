import argparse
import sys
import ekparser
import utils
import semanticsChecker
import IR
import llvm_binder

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

    parser.add_argument('-emit-llvm', action='store_true',
                    default=False,
                    dest='boolean_emit_llvm',
                    help='generate ast')
    parser.add_argument('-jit', action='store_true',
                default=False,
                dest='boolean_jit',
                help='generate ast'),
    parser.add_argument('-o', action='store',
                    dest='output_file',
                    help='output file name',
                    required=False)
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
        utils.emitAst(args.source_file.rsplit('.', 1)[0] + '.ast.yaml', ast)
    
    module = IR.mainFunc(ast, args.sysarg)

    if args.boolean_emit_llvm:
        utils.emit_ir(args.output_file.rsplit('.', 1)[0] + '.ll', module)

    if args.boolean_jit:
        module = llvm_binder.bind(module, args.sysarg, optimize = False)

    sys.exit(0)

if __name__== "__main__":
    main()
