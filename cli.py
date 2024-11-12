import argparse
from viper import Viper

parser = argparse.ArgumentParser(prog="Viper", description="Compute vIP score")

parser.add_argument("seq", type=str)

parser.add_argument("-D", "--double_strand", action="store_true")

if __name__ == "__main__":
    args = parser.parse_args()
    viper_obj = Viper()
    if args.double_strand:
        score = viper_obj.compute_double_strand_score(args.seq)
    else:
        score = viper_obj.compute_single_strand_score(args.seq)
    print(
        f"The vIP value ({'double strand' if args.double_strand else 'single strand'}) is {score:.4f}"
    )
