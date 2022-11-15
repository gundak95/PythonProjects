import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-s", "square", help="display the square of the entered number", type=int)
parser.add_argument("-v", "--verbosity", action="store_true", help="increase output verbosity")
args = parser.parse_args()
answer = args.square**2
if args.verbosity:
    print("verbosity turned on")
else:
    print(answer)
#python3 .\assignment008.py 3 --verbosity 1
#With this input in the cmd line, I get the correct output.

#Broke it again. Don't know how.