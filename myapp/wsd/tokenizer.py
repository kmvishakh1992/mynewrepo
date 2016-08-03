from nltk.data import load
from nltk.tokenize.treebank import TreebankWordTokenizer
def sent_tokenize(text, language='english'):
	tokenizer = load('tokenizers/punkt/{0}.pickle'.format(language))
	return tokenizer.tokenize(text)	

_treebank_word_tokenize = TreebankWordTokenizer().tokenize

def word_tokenize(text, language='english'):
	return [token for sent in sent_tokenize(text, language)
		for token in _treebank_word_tokenize(sent)]