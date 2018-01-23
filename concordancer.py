from create_cat_corpus import create_corpus
from nltk.text import Text

catcorpus = create_corpus('catcorpus/')
print(catcorpus.categories())

c6070_words = Text(catcorpus.words(categories='c6070'))
c8090_words = Text(catcorpus.words(categories='c8090'))

keyword = 'restaurant'
print(f'c6070 concordances of {keyword}')
c6070_words.concordance(keyword)
print(c6070_words.concordance_index)
print(f'c8090 concordances of {keyword}')
c8090_words.concordance(keyword)
print(c8090_words.concordance_index)