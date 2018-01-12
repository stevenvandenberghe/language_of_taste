import csv
from collections import defaultdict
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
from nltk.tokenize import RegexpTokenizer
import nltk.data

word_tokenize = RegexpTokenizer('\w+(?:-\w+)*(?:[?!.,:])*')
sent_tokenize = nltk.data.load('tokenizers/punkt/french.pickle')
translation = str.maketrans("","", ",.?!:")


def create_corpus(directory):
    corpus = PlaintextCorpusReader(directory, '.*', encoding="iso-8859-1", word_tokenizer=word_tokenize, sent_tokenizer=sent_tokenize)
    return corpus


def create_wordlist(corpus):
    wordcount = defaultdict(int)
    counter = 0
    for file in corpus.fileids():
        for word in corpus.words(file):
            word = word.lower().translate(translation)
            if word[0].isalpha():
                wordcount[word] += 1
                counter += 1
    print(f'{repr(corpus)} has {counter} tokens and {len(wordcount)} types')
    return wordcount


def write_wordlist(wordcount, filename):
    wordlist = sorted(wordcount.items())
    with open(f'{filename}.csv', 'w', newline='', encoding='iso-8859-1') as out:
        csv_out = csv.writer(out, delimiter='\t')
        csv_out.writerow(['word', 'abs'])
        for row in wordlist:
            csv_out.writerow(row)

write_wordlist(create_wordlist(create_corpus('testcorpus/6070/')), 'c6070_wordlist_freq')
write_wordlist(create_wordlist(create_corpus('testcorpus/8090/')), 'c8090_wordlist_freq')
