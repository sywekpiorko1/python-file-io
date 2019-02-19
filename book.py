# deal with regular expresions
import  re
# and to allow us to count occurieces of words
import collections 

text = open('book_all.txt').read().lower()
words = re.findall('\w+', text)
print(collections.Counter(words).most_common(10))