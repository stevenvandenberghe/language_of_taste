import csv
from collections import defaultdict, OrderedDict
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
from nltk.tokenize import RegexpTokenizer
import nltk.data
from string import punctuation

c6070_dir = 'testcorpus/6070/'
c8090_dir = 'testcorpus/8090/'
c6070_wordcount = defaultdict(int)
c8090_wordcount = defaultdict(int)
word_tokenize = RegexpTokenizer('\w+(?:-\w+)*(?:[?!.,:])*')
sent_tokenize = nltk.data.load('tokenizers/punkt/french.pickle')
translation = str.maketrans("","", ",.?!:")

# ([A-Z]\.)+\w+(-\w+)*\$?\d+(\.\d+)?%?\.\.\.[][.,;"\'?():-_`]

counter = 0

c6070 = PlaintextCorpusReader(c6070_dir, '.*', encoding="iso-8859-1", word_tokenizer=word_tokenize, sent_tokenizer=sent_tokenize)
c8090 = PlaintextCorpusReader(c8090_dir, '.*', encoding="iso-8859-1", word_tokenizer=word_tokenize, sent_tokenizer=sent_tokenize)

for file in c6070.fileids():
    for word in c6070.words(file):
        word = word.lower().translate(translation)
        if word[0].isalpha():
            c6070_wordcount[word] += 1
            counter += 1

print(f'C6070 has {counter} tokens and {len(c6070_wordcount)} types')

counter = 0
for file in c8090.fileids():
    for word in c8090.words(file):
        word = word.lower().translate(translation)
        if word[0].isalpha():
            c8090_wordcount[word] += 1
            counter += 1

print(f'C8090 has {counter} tokens and {len(c8090_wordcount)} types')


# sort by name, ascending and write to file
c6070_wordlist = sorted(c6070_wordcount.items())
with open('c6070_wordlist_freq.csv', 'w', newline='', encoding='iso-8859-1') as out:
    csv_out = csv.writer(out, delimiter='\t')
    csv_out.writerow(['word', 'abs'])
    for row in c6070_wordlist:
        csv_out.writerow(row)

# sort by name, ascending and write to file
c8090_wordlist = sorted(c8090_wordcount.items())
with open('c8090_wordlist_freq.csv', 'w', newline='', encoding='iso-8859-1') as out:
    csv_out = csv.writer(out, delimiter='\t')
    csv_out.writerow(['word', 'abs'])
    for row in c8090_wordlist:
        csv_out.writerow(row)

# sort by frequency, descending
print(OrderedDict(sorted(c6070_wordcount.items(), key=lambda v: v[1], reverse=True)))
print(OrderedDict(sorted(c8090_wordcount.items(), key=lambda v: v[1], reverse=True)))


# TODO: refactor to functions for repeating functionality