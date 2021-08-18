import sys
import pathlib
from collections import defaultdict
from typing import NewType, Dict, List, Tuple

Bag = NewType("Bag", Dict[str, int])


def read_file(
    f: str = "data\\SMSSpamCollection",
) -> Tuple[Bag, Bag]:
    filepath = pathlib.Path(f)
    if not filepath.exists:
        print("Training data file not found!")
        sys.exit(1)

    with open(filepath) as corpus:
        data = corpus.readlines()

    ham = Bag(defaultdict(int))
    spam = Bag(defaultdict(int))
    for line in data:
        if line.startswith("ham"):
            for word in line[2:].split():
                ham[word.lower()] += 1
        else:
            for word in line[3:].split():
                spam[word.lower()] += 1
    return ham, spam


def compute_probability(word: str, ham: Bag, spam: Bag) -> float:
    count_in_ham: int = ham[word]
    count_in_spam: int = spam[word]

    total_ham = sum(v for _, v in ham.items())
    total_spam = sum(v for _, v in spam.items())

    p_ws = count_in_spam / total_spam
    p_wh = count_in_ham / total_ham
    probability = p_ws / (p_ws + p_wh)
    return probability
