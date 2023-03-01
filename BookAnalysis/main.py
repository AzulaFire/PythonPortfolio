import re
import nltk
#nltk.download('stopwords')
from nltk.corpus import stopwords

english_stopwords = stopwords.words("english")


def word_count(word):
    result = word + ":" + str(d[word])
    return result


# Open Book .txt file to begin analysis

with open('bible-niv.txt', 'r') as file:
    book = file.read()


pattern = re.compile('Chapter [0-9]+') # Find all the chapters

pattern = re.compile('God is [^.]*')

findings = re.findall(pattern, book)

# What are the most used words?

pattern = re.compile('[a-zA-Z]+')

findings = re.findall(pattern, book.lower())

# How many words in the book
#print(len(findings))

d = {}
for finding in findings:
    if finding in d.keys():
        d[finding] = d[finding] + 1
    else:
        d[finding] = 1

d_list = [(value, key) for (key, value) in d.items()]
d_list = sorted(d_list, reverse=True)


filtered_words = []
for count, word in d_list:
    if word not in english_stopwords:
        filtered_words.append((word, count))

print(filtered_words[:10])        

word = input("Enter the word you want to find in the bible to get the number of times it is found: ").lower()
words = word_count(word)
print(words)