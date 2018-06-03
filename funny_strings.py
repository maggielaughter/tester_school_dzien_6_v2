"""Module for funny string manipulations"""
from random import randint
import string


def bubbleize(text):
    text = text.lower()
    new_text=''
    for indx, char in enumerate(text):
        if indx % 2 == 1:
            new_text += char.upper()
        else:
            new_text += char
    return new_text

def bubbleize2(text):
    """
    Program to change letters to upper and lower
    :param text: text to bubbleize
    :return: bubbleize text
    """
    chars=[]
    for idx, char in enumerate(text):
        if idx % 2:
            chars.append(char.upper())
        else:
            chars.append(char.lower())
    return ''.join(chars)


def randomize(text):
    """
        Program to randomized strings
        :param text: text to randomize d
        :return: randomized text
        """
    chars = []
    for idx, char in enumerate(text):
        if randint(0,1):
            chars.append(char.upper())
        else:
            chars.append(char.lower())
    return ''.join(chars)


def numberize(text):
    text=text.lower()
    new_word=''
    for char in text:
        if char=='e':
            new_word += '3'
        elif char == 'o':
            new_word += '0'
        elif char == 'i':
            new_word += '1'
        elif char == 'a':
            new_word += '@'
        else:
            new_word += char
    return new_word
