#!/usr/bin/env python3
import logging
import logging.config
import argparse

from utils.settings import settings

def init_argpase() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        usage="%(prog)s [Option] [FILE]...",
        description="This is my template for python programs.\nIt includes a main function, argument parsing and a logger."
    )
    parser.add_argument(
        '-v', '--version', action='version',
        version = f'{parser.prog} version 1.0.0'
    )
    parser.add_argument('files', nargs='*')
    return parser

def main() -> None:
    parser = init_argpase()
    args = parser.parse_args()

    logging.config.fileConfig('logging.conf')
    logger = logging.getLogger(__name__)

    logger.info(args)


if __name__ == '__main__':
    main()
