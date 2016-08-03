from nltk.corpus import wordnet as wn
from nltk.stem import PorterStemmer, WordNetLemmatizer

porter = PorterStemmer()
wnl = WordNetLemmatizer()


def lemmatize(ambiguous_word, pos=None, neverstem=False, lemmatizer=wnl, stemmer=porter):
	if pos:
		lemma = lemmatizer.lemmatize(ambiguous_word, pos=pos)
	else:
		lemma = lemmatizer.lemmatize(ambiguous_word)
	stem = stemmer.stem(ambiguous_word)

	if not wn.synsets(lemma):
		if neverstem:
			return ambiguous_word
		if not wn.synsets(stem):
			return ambiguous_word
		else:
			return stem
	else:
		return lemma