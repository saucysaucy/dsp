#!/usr/bin/env python

# Write a Markov text generator, [markov.py](python/markov.py). Your program should be called from the command line with two arguments: the name of a file containing text to read, and the number of words to generate. For example, if `chains.txt` contains the short story by Frigyes Karinthy, we could run:

# ```bash
# ./markov.py chains.txt 40
# ```

# A possible output would be:

# > show himself once more than the universe and what I often catch myself playing our well-connected game went on. Our friend was absolutely correct: nobody from the group needed this way. We never been as the Earth has the network of eternity.

# There are design choices to make; feel free to experiment and shape the program as you see fit. Jeff Atwood's [Markov and You](http://blog.codinghorror.com/markov-and-you/) is a fun place to get started learning about what you're trying to make.

import sys

stdin = sys.argv[1]
with open(stdin, mode = 'rt',encoding='utf-8') as f:
    text = f.read()

grams = text.split()
try:
    word_count = int(sys.argv[2])
    grams = grams[:word_count]

except IndexError:
    pass

def n_grams(grams,num):
    phrases = []
    n = 0      #while loop counter
    while n<len():         #joins num inputed number of adjacent words
        phrases.append(' '.join(lower[n:(n+num)]))
        n=n+1
    unique_phrases=set(phrases)    #sets only the unique phrases
    up_dict={}
    for i in unique_phrases:
        up_dict[i]=phrases.count(i)  #adds phrases and coorisponding count
    all_phrases = sorted(up_dict.items(),key=lambda x: x[1],reverse=True)   #sorts in descending order
    common_phrases = []
    for i in all_phrases:  #only appends if frequency is greater than 3 times
        if i[1]>2:
            common_phrases.append(i)
    return common_phrases      #returns list of common phrases by 'num' words in list