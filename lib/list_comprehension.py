#!/usr/bin/env python3

def return_evens(num_list):
    # for elements in num_list:
    #     if elements%2 == 0:
    #         print(elements)
    return[elements for elements in num_list if elements%2 == 0]

print(return_evens([1,2,3,4,5,6,7,8,9,10]))  

def make_exclamation(sentence_list):
    # for word in sentence_list:
    #     if len(sentence_list) > 0:
    #         print(f"{word}!")
    return [f"{word}!" for word in sentence_list if len(sentence_list) > 0]

print(make_exclamation(["Hello", "I'm doing great", "Python is fun"]))