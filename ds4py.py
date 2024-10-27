# Usage: python ds4py.py <filename>

import sys
import os
import re

FILE_PATH = "your_file.py"


def create_docstring(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    with open(filename, "w") as f:
        for line in lines:
            match = re.match(r"(\s*)def\s+(\w+)\s*\((.*?)\)\s*:", line)
            if match:
                indent = match.group(1)
                func_name = match.group(2)
                args = match.group(3)
                arg_list = [arg.strip() for arg in args.split(",") if arg.strip()]
                f.write(line)
                f.write(indent + '    """\n')
                f.write(indent + "    Edit Description\n\n")
                for arg in arg_list:
                    f.write(indent + "    {}: type\n".format(arg))
                f.write("\n")
                f.write(indent + "    ret: type\n")
                f.write(indent + '    """\n')
            else:
                f.write(line)


if __name__ == "__main__":
    filename = FILE_PATH

    if filename != "your_file.py" and not os.path.exists(filename):
        print(
            "File not found '{}'\nEnsure that this file is in the same directory as your python file. ".format(
                filename
            )
        )
        sys.exit(1)

    if len(sys.argv) < 2:
        print("Usage: python docstring_helper.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    if not os.path.exists(filename):
        print(
            "File not found '{}'\nEnsure that this file is in the same directory as your python file. ".format(
                filename
            )
        )
        sys.exit(1)
    create_docstring(filename)
