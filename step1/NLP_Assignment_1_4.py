import nltk
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
nltk.download('punkt')

# Finish me
def getJaccard(tokenset1, tokenset2):
    return 0.0


stop_words = set(stopwords.words('english'))

tk = TweetTokenizer()
tk_tokens = tk.tokenize("This is a test")
filtered_tk_tokens = [w for w in tk_tokens if not w in stop_words]
print(tk_tokens)
print(filtered_tk_tokens)

wt_tokens = word_tokenize("This is a test")
filtered_wt_tokens = [w for w in wt_tokens if not w in stop_words]
print(word_tokenize("This is a test"))
print(filtered_wt_tokens)