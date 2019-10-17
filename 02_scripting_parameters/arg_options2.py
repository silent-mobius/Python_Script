#!/usr/bin/env python3
import argparse

p = argparse.ArgumentParser()

p.add_argument('echo', help='echo the string you use here')
p.add_argument('-v','--verbose', help='adds verbosibility',action='store_true')
args = p.parse_args()

print(args.echo)
