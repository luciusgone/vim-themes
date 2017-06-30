#!/usr/bin/env python3

import sys
import argparse
import themes

def main():
    if sys.argv[1] in ("g", "generate"):
        themes.generate()
    elif sys.argv[1] in ("p", "palette"):
        themes.print_color_palette()

if __name__ == "__main__":
    main()
