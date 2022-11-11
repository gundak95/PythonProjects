import argparse
parser = argparse.ArgumentParser(description="See if you're on the guest list")
parser.add_argument("--guest",
    choices=("Julia","Gunda","Fabs"),
    dest="guest",
    default="Fabs"
)