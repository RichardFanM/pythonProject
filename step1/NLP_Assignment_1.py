import io

import tokenizers.pre_tokenizers as pt
import evaluate
from evaluate import load

import string
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


def tokenize(input_str):
    result = []
    bpt = pt.BertPreTokenizer()
    for ele in bpt.pre_tokenize_str(input_str):
        if ele[0] not in string.punctuation:
            result.append(ele[0])
    return result


max1_len = 0
max2_len = 0

for gene_rif in corpus:
    tokens = tokenize(input_str=gene_rif)
    current_len = len(tokens)
    if max1_len < current_len:
        max2 = max1
        max1 = tokens
        max2_len = max1_len
        max1_len = current_len
    elif max2_len < current_len:
        max2 = tokens
        max2_len = current_len

print("Highest number of token in geneRIF: " + str(max1_len))

perplexity = load("perplexity", module_type="measurement")
bbu_results = perplexity.compute(add_start_token=False, data=corpus, model_id='bert-base-uncased')
bp_results = perplexity.compute(add_start_token=False, data=corpus, model_id='monologg/biobert_v1.1_pubmed')
print(bp_results.get("mean_perplexity"))
print(bbu_results.get("mean_perplexity"))

# https://zhuanlan.zhihu.com/p/31852747
