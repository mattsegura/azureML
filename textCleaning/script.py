import re

# from nltk import stopwords

""" 
Text Cleaning with NLTK:
1. Normalize text [done]
2. Remove Unicode Characters [done]
3. Remove Stopwords [optional]
4. Perform Stemming and Lemmatization [in progress]
"""


# If you're recieving an SSL error from instal nltk for the first time then this is a workaround
""" import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
 """
# nltk.download("stopwords")

# text = "Hey Amazon - my package never arrived https://www.amazon.com/gp/css/order-history?ref_=nav_orders_first FIX THIS ASAP! @AmazonHelp"

text = input("Please enter your body\n")
# nltk.download("stopwords")
# stop = stopwords.words("english")

# case normalization to have a base text
text = text.lower()
# removing punctuations, emojis, urls and @s
text = re.sub(r"(@\[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|^rt|http.+?", "", text)
print(text)
""" 
optional: removes stopwords using the nltk lib 
stop = set(stopwords.words("english"))
removing stop words
 """
