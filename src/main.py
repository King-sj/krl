from lex import lexer
from parser import parser
import argparse
from interpreter import Interpreter


def main():
  arg_parser = argparse.ArgumentParser(description="Run KRL script.")
  arg_parser.add_argument("file", type=str, help="KRL script file.")
  args = arg_parser.parse_args()
  with open(args.file, "r") as f:
    data = f.read()
    parser.parse(data)
    from parser import root
    krl_interpreter = Interpreter(root)
    krl_interpreter.run()


if __name__ == '__main__':
  main()
