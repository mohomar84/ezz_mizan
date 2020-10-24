from typing import List


class aya_alphabet(object):
    def __init__(self, alphabet: str, alphabet_weight: str):
        self.alphabet = alphabet
        self.alphabet_weight = alphabet_weight


class aya_word(object):
    def __init__(self, aya_word, word_weight, word_alphabets: List[aya_alphabet]):
        self.aya_word = aya_word
        self.word_weight = word_weight
        self.word_alphabets = word_alphabets


class full_aya(object):
    def __init__(self, full_aya, full_weight, aya_words: List[aya_word]):
        self.full_aya = full_aya
        self.full_weight = full_weight
        self.aya_words = aya_words
