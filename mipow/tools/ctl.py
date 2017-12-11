#! /usr/bin/env python3

import argparse
import mipow


def parse_color(s):
    if len(s) == 6:
        return [int(ca + cb, 16) for ca, cb in zip(s[::2], s[1::2])]
    if len(s) == 3:
        return [int(c + c, 16) for c in s]
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
