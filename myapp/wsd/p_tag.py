
from nltk.tag.mapping       import map_tag
from nltk.tag.perceptron    import PerceptronTagger
#from t import PerceptronTagger
from nltk.data import load

def _pos_tag(tokens, tagset, tagger):
	tagged_tokens = tagger.tag(tokens)
	if tagset:
		tagged_tokens = [(token, map_tag('en-ptb', tagset, tag)) for (token, tag) in tagged_tokens]
	return tagged_tokens


def pos_tag(tokens, tagset=None):
	tagger = PerceptronTagger()
	return _pos_tag(tokens, tagset, tagger) 