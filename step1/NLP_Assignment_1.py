import io

import nltk.corpus
import tokenizers.pre_tokenizers
import evaluate
from evaluate import load

f = open("generifs1000.tsv", "r")
print(f.read())

corpus = []
max1 = []
max2 = []
