
#from nltk import pos_tag

from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import wordnet as wn
from tester1 import lemmatize
from tokenizer import word_tokenize
from p_tag import pos_tag

porter = PorterStemmer()
wnl = WordNetLemmatizer()

def lemmatize_sentence(sentence, neverstem=False, keepWordPOS=False, 
                       tokenizer=word_tokenize, postagger=pos_tag, 
                       lemmatizer=wnl, stemmer=porter):
    words, lemmas, poss = [], [], []
    for word, pos in postagger(tokenizer(sentence)):
        print(pos)
        pos = penn2morphy(pos)
        '''returnNone=False
        morphy_tag = {'NN':wn.NOUN, 'JJ':wn.ADJ,
                  'VB':wn.VERB, 'RB':wn.ADV}
        try:
            morphy_tag[pos[:2]]
        except:
            None if returnNone else ''
        '''
       # print(pos)
        lemmas.append(lemmatize(word.lower(), pos, neverstem,
                                lemmatizer, stemmer))
        '''print("0")
        print(pos)
        print("1")
        print(neverstem)
        print("2")
        print(lemmatizer)
        print("3")
        print(stemmer)'''
        #print(lemmas)
        poss.append(pos)
        words.append(word)
    if keepWordPOS:
        '''for i in poss:
            print(i)'''
        return words, lemmas, [None if i == '' else i for i in poss]
    #print(words)
    #print(poss)
    return lemmas

def penn2morphy(pos, returnNone=False):
    m_tag = {'NN':wn.NOUN, 'JJ':wn.ADJ,
                  'VB':wn.VERB, 'RB':wn.ADV}
    try:
        return m_tag[pos[:2]]
    except:
        return None if returnNone else ''
       
