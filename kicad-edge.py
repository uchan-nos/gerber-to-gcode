#!/usr/bin/python3

import argparse

def parse_gerber(gerber_file):
    for line in gerber_file:
        line = line.strip()
        if line[0] == '%' and line[-1] == '%':
            print('extended command: ' + line[1:-1])
        else:
            print('unknown command: ' + line)

def main():
    p = argparse.ArgumentParser()
    p.add_argument('gerber')
    args = p.parse_args()

    with open(args.gerber) as f:
        parse_gerber(f)

if __name__ == '__main__':
    main()
