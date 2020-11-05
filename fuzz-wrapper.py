import afl, ekcc, os, sys

afl.init()
ekcc.fuzztest(sys.stdin.read())
os._exit(0)