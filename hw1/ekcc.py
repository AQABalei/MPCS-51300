from yaml import dump
import argparse
import mmap
import sys
import lex

def readFile(fileName):
  f = open(fileName,"r")
  mMap = mmap.mmap(f.fileno(),0, prot = mmap.PROT_READ)
  stringFile =str(mMap[:])
  stringFile = stringFile[2:-1]
  data = mMap[:].decode('ascii')
  return data

def emitAst(fileName, output):
  yaml = dump(output, default_flow_style=False)
  file = open(fileName, 'w')
  file.write(yaml)
  file.close()

if __name__== "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('input_file', metavar='input_file',
                    help='input file name')
  parser.add_argument('-emit-ast', action='store_true',
                    default=False,
                    dest='boolean_emit_ast',
                    help='generate ast'),
  parser.add_argument('-emit-llvm', action='store_true',
                  default=False,
                  dest='boolean_emit_llvm',
                  help='generate ast')
  parser.add_argument('-o', action='store',
                    dest='output_file',
                    help='output file name',
                    required=False)
  parser.add_argument('-O', action='store_true',
                  dest='optimization',
                  help='optimization',
                  required=False)
  args = parser.parse_args()

  code = readFile(args.input_file)
  ast = lex.toAst(code)
  if ast is None:
      raise RuntimeError('AST parsing failure')
      sys.exit(-1)

  if args.boolean_emit_ast:
    emitAst(args.input_file.rsplit('.', 1)[0] + '.ast.yaml', ast)

  print('exit: 0')
  sys.exit(0)