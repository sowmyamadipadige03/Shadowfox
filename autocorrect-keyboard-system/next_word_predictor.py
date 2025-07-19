from collections import defaultdict
import random

def build_trigrams(text):
    words = text.lower().split()
    model = defaultdict(list)
    for i in range(len(words) - 2):
        key = (words[i], words[i+1])
        model[key].append(words[i+2])
    return model

def predict_next_word(word1, word2, trigrams):
    options = trigrams.get((word1.lower(), word2.lower()), [])
    if not options:
        return "..."
    return random.choice(options)
