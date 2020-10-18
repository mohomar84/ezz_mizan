from mizan.aya_weight.aya_weight_count import alphabet
from mizan.common.alpha_config import ArWeight


class Util:

    @staticmethod
    def find_in_alph_weight(alpha):
        for d in ArWeight:
            if alpha == d.name:
                return d.value

    @staticmethod
    def find_special_alphabet(character):
        """
        check if the arabic alphabet is part of the special arabic alphabets
        if the alphabet id a special alphabet the method will call alphabet_origin()
        to return the alphabet origin
        :param character: arabic alphabet
        :return:
        """
        sp_alpha = ["إ", "أ", "ٱ", "آ", "ى", "ؤ", "ئ", "ة"]
        for v in sp_alpha:
            if v == character:
                print(True, character)
                return alphabet(character)
        return character

    @staticmethod
    def alphabet_origin(sp_alphabet):
        """
        get the arabic alphabet special origin
        :param sp_alphabet: special arabic alphabet
        :return: the bas alphabet
        """
        a_alpha = ["إ", "أ", "ٱ", "آ"]
        i_alpha = ["ى", "ؤ", "ئ", "ة"]
        h_alpha = ["ة"]
        if sp_alphabet in a_alpha:
            return "ا"
        if sp_alphabet in i_alpha:
            return "ي"
        if sp_alphabet in h_alpha:
            return "ه"
