import io

import tokenizers.pre_tokenizers
import evaluate
from evaluate import load

import csv

with open("generifs1000.tsv") as file:
    tsv_file = csv.reader(file, delimiter="\t")

    for line in tsv_file:
        print(line[4])


corpus = []
max1 = []
max2 = []
