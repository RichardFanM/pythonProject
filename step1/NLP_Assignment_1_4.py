import nltk
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
nltk.download('punkt')


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

tk = TweetTokenizer()
tk_tokens = tk.tokenize("This is a test")
filtered_tk_tokens = [w for w in tk_tokens if not w in stop_words]
print(tk_tokens)
print(filtered_tk_tokens)

wt_tokens = word_tokenize("This is a test sample")
filtered_wt_tokens = [w for w in wt_tokens if not w in stop_words]
print(word_tokenize("This is a test"))
print(filtered_wt_tokens)

distance = getJaccard(filtered_wt_tokens, filtered_tk_tokens)
print(distance)
