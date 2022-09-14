import nltk
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
nltk.download('punkt')

import csv

corpus = []

is_FirstLine = False

with open("generifs1000.tsv") as file:
    tsv_file = csv.reader(file, delimiter="\t")

    for line in tsv_file:
        if is_FirstLine:
            corpus.append(line[4])
        is_FirstLine = True


# Finish me
def getJaccard(tokenset1, tokenset2):
    len1 = len(tokenset1)
    len2 = len(tokenset2)
    intersection = 0

    for str1 in tokenset2:
        if str1 in tokenset1:
            intersection += 1

    full = len1 + len2 - intersection

    return 1 - intersection / full


stop_words = set(stopwords.words('english'))


def tokenizeByTweetTokenizer(input_str):
    tk = TweetTokenizer()
    tk_tokens = tk.tokenize(input_str)
    filtered_tk_tokens = [w for w in tk_tokens if not w in stop_words]
    return filtered_tk_tokens


def tokenizeByWord_tokenize(input_str):
    wt_tokens = word_tokenize(input_str)
    filtered_wt_tokens = [w for w in wt_tokens if not w in stop_words]
    return filtered_wt_tokens


max_distance = 0
max_distance_str = ""

for geneRIF in corpus:
    tk_output = tokenizeByTweetTokenizer(geneRIF)
    wt_output = tokenizeByWord_tokenize(geneRIF)
    distance = getJaccard(tk_output, wt_output)
    if distance > max_distance:
        max_distance = distance
        max_distance_str = geneRIF

print(max_distance_str)
print(tokenizeByWord_tokenize(max_distance_str))
print(tokenizeByTweetTokenizer(max_distance_str))
