#! /usr/bin/env python3

import argparse
import mipow


def parse_color(s):
    # TODO: Allow hex notation
    return [int(c) for c in s.split(",")]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-a", "--address",
        required=True,
    )
    parser.add_argument(
        "-c", "--color",
        type=parse_color,
        required=True,
    )
    parser.add_argument(
        "-b", "--brightness",
        type=int,
        default=0,
    )
    args = parser.parse_args()

    mw = mipow.Mipow(args.address)
    mw.set(args.color[0], args.color[1], args.color[2], l=args.brightness)


if __name__ == "__main__":
    main()
