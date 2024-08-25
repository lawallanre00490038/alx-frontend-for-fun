#!/usr/bin/python3
"""
A python fine that prints 
Return: null
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


# Open the input and output files
with open(markdown_file, 'r') as infile, open(output_file, 'w') as outfile:
    for line in infile:
        line = line.strip()
        if line.startswith('#'):
            # Count the number of leading # to determine heading level
            level = len(line.split(' ')[0])
            content = line[level:].strip()
            outfile.write(f"<h{level}>{content}</h{level}>\n")
