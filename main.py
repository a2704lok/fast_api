import sys
import argparse
from pathlib import Path
codesetup_path = Path.home()/"Desktop"/"codesetup"
sys.path.append(str(codesetup_path))

from function import addition # type: ignore

if __name__ =="__main__":
    parser = argparse.ArgumentParser(description = "add two numbers")
    parser.add_argument("num1", type=float, help = "the first number")
    parser.add_argument("num2", type=float, help = "the second number")
    args = parser.parse_args()

    result = addition(args.num1,args.num2)
    print(f"The sum is {result}.")

