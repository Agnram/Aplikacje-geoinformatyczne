from cw4.actual_source_code.first import example_for_logging
from cw4.utils.parse_cli_args import parse_args

if __name__ == "__main__":
    example_for_logging()

    args = parse_args()
    
    print(args.verbosity)
    print(args.text)