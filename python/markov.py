#!/usr/bin/env python

# Write a Markov text generator, [markov.py](python/markov.py). Your program should be called from the command line with two arguments: the name of a file containing text to read, and the number of words to generate. For example, if `chains.txt` contains the short story by Frigyes Karinthy, we could run:

# ```bash
# ./markov.py chains.txt 40
# ```

# A possible output would be:

# > show himself once more than the universe and what I often catch myself playing our well-connected game went on. Our friend was absolutely correct: nobody from the group needed this way. We never been as the Earth has the network of eternity.

# There are design choices to make; feel free to experiment and shape the program as you see fit. Jeff Atwood's [Markov and You](http://blog.codinghorror.com/markov-and-you/) is a fun place to get started learning about what you're trying to make.



import sys
import random

stdin = sys.argv[1]#
with open(stdin, mode = 'rt',encoding='utf-8') as f:
    text = f.read()

grams = text.split()
grams = [word.strip(",.`\:;?!{}[]-\'\"()") for word in grams]
grams = [i for i in grams if not len(i)==0]

try:
    word_count = int(sys.argv[2])
    grams = grams[:word_count]
except:
    word_count = len(grams)

def trigram(grams):
    if len(grams) < 3:
        return "Text is too short"
    tri = []
    for i, word in enumerate(grams):
        word = word.strip(",.`\:;?!{}[]")
        if i == len(grams)-3:
            break
        tri.append([grams[i], grams[i + 1], grams[i + 2]])
    return tri

def tri_dict(trigrams):
    tridict = {}
    for gram1, gram2, gram3 in trigrams:
        k = (gram1, gram2)
        if k in tridict:
            tridict[k].append(gram3)
        else:
            tridict[k] = [gram3]
    return tridict


def markov_text(d):
    if type(d)==dict:
        pass
    else:
        d = tri_dict(trigram(grams))
    egrams = dict(enumerate(grams))
    rand = random.choice(list(egrams))
    seed, next = egrams[rand], egrams[rand+1]
    markov_words = []
    for i in range(word_count):
        markov_words.append(seed)
        try:
            seed, next = next, random.choice(d[(seed, next)])
            markov_words.append(next)
        except KeyError:
            markov_words.append(next)
    return ' '.join(markov_words)

trigrams = trigram(grams)
tri_to_dict = tri_dict(trigrams)
sentence = markov_text(tri_to_dict)
print(markov_text(grams))
#print(sentence)
