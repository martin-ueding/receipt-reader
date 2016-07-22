#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright © 2016 Martin Ueding <dev@martin-ueding.de>

import argparse
import os
import subprocess


def main():
    options = _parse_args()

    original = options.receipt

    base, ext = os.path.splitext(original)
    optimized = base + '-levels.png'

    #adjust_levels(original, optimized)
    optimized = original
    ocr(optimized)


def format_levels(black, white, gamma):
    return '{:f}%,{:f}%,{:f}'.format(black / 255 * 100, white / 255 * 100, gamma)


def adjust_levels(infile, outfile):
    level = format_levels(58, 206, 0.52)
    command = ['convert', infile, '-level', level, outfile]
    print(command)
    subprocess.check_call(command)


def ocr(filename):
    command = ['tesseract', '-l', 'deu', '-psm', '6', filename, 'stdout']
    output = subprocess.check_output(command).decode()
    for line in output.split('\n'):
        print(line)


def _parse_args():
    '''
    Parses the command line arguments.

    :return: Namespace with arguments.
    :rtype: Namespace
    '''
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('receipt')
    options = parser.parse_args()

    return options


if __name__ == '__main__':
    main()
