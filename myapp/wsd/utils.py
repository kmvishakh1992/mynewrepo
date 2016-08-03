
from nltk.corpus import wordnet as wn
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk import pos_tag, word_tokenize

SS_PARAMETERS_TYPE_MAP = {'definition':str, 'lemma_names':list, 
                          'examples':list,  'hypernyms':list,
                         'hyponyms': list, 'member_holonyms':list,
                         'part_holonyms':list, 'substance_holonyms':list,
                         'member_meronyms':list, 'substance_meronyms': list,
                         'part_meronyms':list, 'similar_tos':list}

def remove_tags(text):
  import re
  tags = {i:" " for i in re.findall("(<[^>\n]*>)",text.strip())}
  no_tag_text = reduce(lambda x, kv:x.replace(*kv), tags.iteritems(), text)
  return " ".join(no_tag_text.split())
  
def offset_to_synset(offset):
 
    return wn._synset_from_pos_and_offset(str(offset[-1:]), int(offset[:8]))

def semcor_to_synset(sensekey):
 
    return wn.lemma_from_key(sensekey).synset

def semcor_to_offset(sensekey):
 
    synset = wn.lemma_from_key(sensekey).synset
    offset = '%08d-%s' % (synset.offset, synset.pos)
    return offset



porter = PorterStemmer()
wnl = WordNetLemmatizer()




def synset_properties(synset, parameter):

    return_type = SS_PARAMETERS_TYPE_MAP[parameter]
    func = 'synset.' + parameter
    return eval(func) if isinstance(eval(func), return_type) else eval(func)()

def has_synset(word):
    return wn.synsets(lemmatize(word, neverstem=True))


