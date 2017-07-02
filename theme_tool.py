#!/usr/bin/env python3

import sys
import argparse
import themes

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("subcommand", type=str,
            help="the subcommand you want to use. "
            "currently only `generate` and `palette`")
    args = ap.parse_args()
    if args.subcommand == "generate":
        themes.generate()
    elif args.subcommand == "palette":
        themes.print_color_palette()
    else:
        sys.exit("[ERROR] Command not recogonized")

if __name__ == "__main__":
    main()
