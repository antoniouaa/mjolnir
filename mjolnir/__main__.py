import sys

import mjolnir.compute as c

ham, spam = c.read_file()

word = sys.argv[1]
print(c.compute_probabilities(word, ham=ham, spam=spam))
