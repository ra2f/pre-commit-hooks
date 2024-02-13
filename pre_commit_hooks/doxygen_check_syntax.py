import argparse
import subprocess
import sys
from pathlib import Path
from typing import Optional, Sequence

CONFIG_PATH = Path(__file__).parent.resolve() / 'data' / '.relint.yml'


def main(argv: Optional[Sequence[str]] = None):
    retv = 1
    if CONFIG_PATH.exists():
        parser = argparse.ArgumentParser()
        parser.add_argument('filenames', nargs='*', help='Filenames to check')
        args = parser.parse_args(argv)

        retv = 0

        for filename in args.filenames:
            relint = subprocess.run(
                ('relint', '--config', str(CONFIG_PATH), filename),
                encoding='utf-8',
            )
            retv |= relint.returncode
    else:
        print(f'Config .relint.yml ({str(CONFIG_PATH)}) does not exists.')
    return retv


if __name__ == '__main__':
    sys.exit(main())
