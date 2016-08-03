#!/usr/bin/env python -*- coding: utf-8 -*-

import string
from itertools import chain

from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
from nltk import word_tokenize, pos_tag

from utils import  porter,synset_properties
from tester1 import lemmatize
from tester2 import lemmatize_sentence 
EN_STOPWORDS = stopwords.words('english')



def compare_overlaps(context, synsets_signatures, \
                     nbest=False, keepscore=False, normalizescore=False):
  
    overlaplen_synsets = []
    for ss in synsets_signatures:
        overlaps = set(synsets_signatures[ss]).intersection(context)
        overlaplen_synsets.append((len(overlaps), ss))
    
    ranked_synsets = sorted(overlaplen_synsets, reverse=True)
    
    if normalizescore:
        total = float(sum(i[0] for i in ranked_synsets))
        ranked_synsets = [(i/total,j) for i,j in ranked_synsets]
      
    if not keepscore: 
        ranked_synsets = [i[1] for i in sorted(overlaplen_synsets, \
                                               reverse=True)]
      
    if nbest: 
        return ranked_synsets
    else:
        return ranked_synsets[0]

  

def simple_signature(ambiguous_word, pos=None, lemma=True, stem=False, \
                     hyperhypo=True, stop=True):
   
    synsets_signatures = {}
    for ss in wn.synsets(ambiguous_word):
        try: 
            if pos and str(ss.pos()) != pos:
                continue
        except:
            if pos and str(ss.pos) != pos:
                continue
        signature = []
        ss_definition = synset_properties(ss, 'definition')
        signature+=ss_definition
        ss_examples = synset_properties(ss, 'examples')
        signature+=list(chain(*[i.split() for i in ss_examples]))
        ss_lemma_names = synset_properties(ss, 'lemma_names')
        signature+= ss_lemma_names
        
        if hyperhypo == True:
            ss_hyponyms = synset_properties(ss, 'hyponyms')
            ss_hypernyms = synset_properties(ss, 'hypernyms')
            ss_hypohypernyms = ss_hypernyms+ss_hyponyms
            signature+= list(chain(*[i.lemma_names() for i in ss_hypohypernyms]))
        
        if stop == True: 
            signature = [i for i in signature if i not in EN_STOPWORDS]
        if lemma == True: 
            signature = [lemmatize(i) for i in signature]
        if stem == True: 
            signature = [porter.stem(i) for i in signature]
        synsets_signatures[ss] = signature
        
    return synsets_signatures



def adapted_lesk(context_sentence, ambiguous_word, \
                pos=None, lemma=True, stem=True, hyperhypo=True, \
                stop=True, context_is_lemmatized=False, \
                nbest=False, keepscore=False, normalizescore=False):
  
    # Ensure ambiguous word is a lemma.
    ambiguous_word = lemmatize(ambiguous_word)
    # If ambiguous word not in WordNet return None
    if not wn.synsets(ambiguous_word):
        return None
    ss_sign = simple_signature(ambiguous_word, pos, lemma, stem, hyperhypo)
    for ss in ss_sign:
        ss_mem_holonyms = synset_properties(ss, 'member_holonyms')
        ss_part_holonyms = synset_properties(ss, 'part_holonyms')
        ss_sub_holonyms = synset_properties(ss, 'substance_holonyms')
        ss_mem_meronyms = synset_properties(ss, 'member_meronyms')
        ss_part_meronyms = synset_properties(ss, 'part_meronyms')
        ss_sub_meronyms = synset_properties(ss, 'substance_meronyms')
        ss_simto = synset_properties(ss, 'similar_tos')
        
        related_senses = list(set(ss_mem_holonyms+ss_part_holonyms+ 
                                  ss_sub_holonyms+ss_mem_meronyms+ 
                                  ss_part_meronyms+ss_sub_meronyms+ ss_simto))
    
        signature = list([j for j in chain(*[synset_properties(i, 'lemma_names') 
                                             for i in related_senses]) 
                          if j not in EN_STOPWORDS])
        
    if lemma == True:
        signature = [lemmatize(i) for i in signature]
    #if stem == True:
    signature = [porter.stem(i) for i in signature]
    ss_sign[ss]+=signature
  
    if context_is_lemmatized:
        context_sentence = context_sentence.split()
    else:
        context_sentence = lemmatize_sentence(context_sentence)
    best_sense = compare_overlaps(context_sentence, ss_sign, \
                                    nbest=nbest, keepscore=keepscore, \
                                    normalizescore=normalizescore)
    return best_sense

