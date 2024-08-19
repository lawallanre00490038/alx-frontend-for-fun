#!/usr/bin/python3
"""
A python fine that prints 
"""
import sys, os

if len(sys.argv) < 3:
  print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
  sys.exit(1)

markdown_file = sys.argv[1]
output_file = sys.argv[2]

if not os.path.isfile(markdown_file):
  print("Missing <filename>", file=sys.stderr)
  sys.exit(1)


sys.exit(0)


