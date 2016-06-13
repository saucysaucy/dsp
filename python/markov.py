import sys
import random

stdin = sys.argv[1]
with open(stdin, mode = 'rt',encoding='utf-8') as f:
    text = f.read()

grams = text.split()
grams = [word.strip(",.`\:;?!{}[]-\'\"()").lower() for word in grams]
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

tri = trigram(grams)
tridict = tri_dict(tri)
gen = markov_text(tridict)

print(gen)
