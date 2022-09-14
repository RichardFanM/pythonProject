import io

import tokenizers.pre_tokenizers as pt
import evaluate
from evaluate import load
import torch
import transformers

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
    print(bpt.pre_tokenize_str("this is a test, and hello world."))


tokenize()

perplexity = load("perplexity", module_type="measurement")
bbu_results = perplexity.compute(add_start_token=False, data=corpus, model_id='bert-base-uncased')
bp_results = perplexity.compute(add_start_token=False, data=corpus, model_id='monologg/biobert_v1.1_pubmed')
print(bp_results.get("mean_perplexity"))
print(bbu_results.get("mean_perplexity"))

# https://zhuanlan.zhihu.com/p/31852747
