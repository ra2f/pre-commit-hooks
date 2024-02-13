#!/usr/bin/env python3
# pylint: disable=invalid-name
"""
An example hook script to check the commit log message.
Called by "git commit" with one argument, the name of the file
that has the commit message.  The hook should exit with non-zero
status after issuing an appropriate message if it wants to stop the
commit.  The hook is allowed to edit the commit message file.
"""
import argparse
import sys

def main():
    """Inspect the commit message."""
    if len(argv) < 1:
        argv = sys.argv[1:]

    try:
        args = parser.parse_args(argv)
    except SystemExit:
        return 1

    with open(args.input) as f:
        message = f.read()

    if message and len(message) > 1:
        return 0
    else:
        print(f"""[Bad Commit message] >> {message}""")
        return 1

if __name__ == "__main__":
    raise SystemExit(main())
