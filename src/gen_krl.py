from lex import lexer
from parser import parser
import argparse
from interpreter import Interpreter
from arg import args

def gen_krl():
  with open(args.file, "r") as f:
    data = f.read()
    parser.parse(data)
    from parser import root
    krl_interpreter = Interpreter(root)
    return krl_interpreter
