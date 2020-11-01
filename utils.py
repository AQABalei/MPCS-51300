from yaml import dump
import mmap

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