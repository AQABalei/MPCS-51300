import argparse
import sys
import ekparser
import utils
import semanticsChecker


if __name__== "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('source_file', metavar='source_file', help='input file name')
    parser.add_argument('-emit-ast', action='store_true', default=False,
                        dest='boolean_emit_ast', help='generate ast and save as yaml file')
    args = parser.parse_args()

    source_code = utils.readFile(args.source_file)
    ast = ekparser.getAst(source_code)

    if not ast:
        raise RuntimeError('error: AST parsing failure')
        sys.exit(-1)
    
    # check semantic errors
    semanticsChecker.check(ast)

    if args.boolean_emit_ast:
        utils.emitAst(args.source_file.rsplit('.', 1)[0] + '.ast.yaml', ast)

    sys.exit(0)