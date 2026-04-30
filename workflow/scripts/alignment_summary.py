#!/usr/bin/env python3
"""Parse AMAS per-gene stats files and write a combined summary report."""

import argparse
import os


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--stats", nargs="+", required=True, help="AMAS stats files")
    parser.add_argument("--output", required=True, help="Output summary file")
    return parser.parse_args()


def main():
    args = parse_args()

    with open(args.output, "w") as out:
        out.write("Alignment Quality Summary Report\n")
        out.write("=" * 60 + "\n\n")

        for stats_file in sorted(args.stats):
            gene = os.path.basename(stats_file).replace("_stats.txt", "")
            out.write(f"Gene: {gene}\n")
            out.write("-" * 40 + "\n")
            with open(stats_file) as f:
                out.write(f.read())
            out.write("\n")

    print(f"Summary written to {args.output}")


if __name__ == "__main__":
    main()
