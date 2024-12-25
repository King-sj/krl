from lex import lexer
from parser import parser
import argparse
from interpreter import Interpreter
from arg import args

def gen_krl():
  """
  Generates a KRL interpreter instance from the contents of a specified file.

  This function reads the contents of a file specified by `args.file`, parses the data,
  and creates an instance of the `Interpreter` class using the parsed root.

  Returns:
    Interpreter: An instance of the `Interpreter` class initialized with the parsed root.
  """
  with open(args.file, "r") as f:
    data = f.read()
    parser.parse(data)
    from parser import root
    krl_interpreter = Interpreter(root)
    return krl_interpreter
