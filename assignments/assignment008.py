import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", type=int, help="display the square of the entered number",)
parser.add_argument("-v", "--verbosity", action="store_true", help="increase output verbosity")
args = parser.parse_args()
answer = args.square**2
if args.verbosity:
    print(f"The square of {args.square} equals {answer}.")
else:
    print(answer)
#...\assignments>python3 assignment008.py 4 -v
#With this input in the cmd line, I get the correct output.
#Next time: multiple layers of verbosity with this tutorial: https://docs.python.org/3/howto/argparse.html
