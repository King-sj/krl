import argparse

arg_parser = argparse.ArgumentParser(description="KRL SERVER")

arg_parser.add_argument("--file",
                        type=str,
                        required=True,
                        help="KRL script file.")
arg_parser.add_argument("--port",
                        type=int,
                        help="KRL server port.",
                        default=5001)
arg_parser.add_argument("--host",
                        type=str,
                        help="KRL server host.",
                        default="localhost")
arg_parser.add_argument("--debug",
                        type=bool,
                        help="KRL server debug.",
                        default=True)
args = arg_parser.parse_args()
