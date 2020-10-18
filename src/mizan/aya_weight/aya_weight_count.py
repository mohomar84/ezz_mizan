from mizan.utils.utils import Util


class alphabet_weight:

    @staticmethod
    def aya_weight(aya: str):
        """

        :param aya:
        :return:
        """

        all_words = aya.split(" ")
        total = 0
        words_count = 0

        for i in all_words:
            if i != '':
                print("الكلمه : ", i)
                one_word = list(i)
                word_count = alphabet_weight.get_word_weight(one_word)
                words_count += 1
                total += word_count
        print("-------------")
        print(f' آية :  {aya}')
        print("عدد الكلمات : ", words_count)
        print(" وزن الايه : ", total)
        print("-------------")

    @staticmethod
    def get_word_weight(one_word):
        """
        get word by word alphabet weight in numbers and loop in word by word alphabets
        :param one_word: arabic word
        :return: total word weight in numbers
        """
        total = 0

        for v in one_word:
            single_alphabet = Util.find_special_alphabet(v)
            weight = Util.find_in_alph_weight(single_alphabet)
            if weight is not None:
                total += Util.find_in_alph_weight(single_alphabet)
            print("الحرف : ", v)
            print("الوزن: ", Util.find_in_alph_weight(v))
        print(" اجمالي الكلمه: ", total)
        return total
