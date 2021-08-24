import sys

import mjolnir.compute as c
from mjolnir.utils import exceptions


@exceptions(IndexError)
def main() -> None:
    ham, spam = c.read_file()

    phrase = sys.argv[1:]
    print(c.compute_phrase(phrase, ham=ham, spam=spam))


main()
