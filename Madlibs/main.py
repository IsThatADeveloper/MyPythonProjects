import os
import random
import re
from helper import choices

os.system('cls' if os.name == 'nt' else 'clear')

print('Hi user welcome to Madlibs!')

sentence = random.choice(choices)
print(sentence)

adjective = 1

import re

def replace_sentence(sentence):
    placeholders = re.findall(r'\[(.*?)\]', sentence)  # Extract all placeholders from the sentence
    for placeholder in placeholders:
        if placeholder == 'adjective':
            adj = input('Please provide an adjective: ')
            sentence = sentence.replace('[adjective]', adj, 1)
        elif placeholder == 'noun':
            nou = input('Please provide a noun: ')
            sentence = sentence.replace('[noun]', nou, 1)
        elif placeholder == 'verb':
            verb = input('Please provide a verb: ')
            sentence = sentence.replace('[verb]', verb, 1)
        elif placeholder == 'place':
            place = input('Please provide a place: ')
            sentence = sentence.replace('[place]', place, 1)
        elif placeholder == 'adverb':
            adverb = input('Please provide an adverb: ')
            sentence = sentence.replace('[adverb]', adverb, 1)
    return sentence

modified_sentence = replace_sentence(sentence)
print(modified_sentence)

print('\nThank you for playing MadLibs!')