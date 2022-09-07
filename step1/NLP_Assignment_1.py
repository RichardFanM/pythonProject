import io

import tokenizers.pre_tokenizers as pt
import evaluate
from evaluate import load

import csv

corpus = []
max1 = []
max2 = []

is_FirstLine = False

with open("generifs1000.tsv") as file:
    tsv_file = csv.reader(file, delimiter="\t")

    for line in tsv_file:
        if is_FirstLine:
            corpus.append(line[4])
        is_FirstLine = True

print("Corpus size: " + str(len(corpus)))


def tokenize():
    bpt = pt.BertPreTokenizer()
    print(bpt.pre_tokenize_str("this is a test"))


tokenize()
