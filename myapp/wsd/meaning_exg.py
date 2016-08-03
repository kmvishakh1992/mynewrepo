import sys
from nltk.corpus import wordnet
 
 
line=raw_input("Word : ")
print "-" * 80
#ount+=1
    # Get a collection of synsets for a word
synsets = wordnet.synsets(line.strip())
    # Print the information
print " %s" %(line.strip())
for synset in synsets:
  print "-" * 10
  print "%s(%s)" %(synset.name().split('.')[0],  synset.lexname().split('.')[0]) 
  print "Definition:", synset.definition()
  for example in synset.examples():
    print "Example:", example

    
