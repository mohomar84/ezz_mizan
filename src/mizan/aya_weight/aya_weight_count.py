import json
import sys
import pyarabic.araby as araby
from idna import unicode
from pyarabic.araby import strip_tashkeel
from mizan.dict.aya_report import full_aya, aya_alphabet, aya_word
from mizan.utils.utils import Util
from collections import OrderedDict

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
        aya_words = []
        strip_tashkeel(aya)
        for i in all_words:
            if i != '':
                print("الكلمه : ", i)
                one_word = list(i)
                word_count = alphabet_weight.get_word_weight(one_word).word_weight

                aya_words.append(alphabet_weight.get_word_weight(i))

                words_count += 1
                total += word_count

        for key in aya_words:
            print("**********************")
            print(key.aya_word)
            print(key.word_weight)
            for y in key.word_alphabets:
                print(y.alphabet)
                print(y.alphabet_weight)


        print("-------------")
        print(f' آية :  {aya}')
        print("عدد الكلمات : ", words_count)
        print(" وزن الايه : ", total)
        print("-------------")



        full_aya_dec = full_aya(full_aya=aya, full_weight=total, aya_words=aya_words)
        #print(aya_dict)
        #for key in aya_dict.items():
        #    print("json : ", key)
        # Serialization
        # complexjson.dumps
        # json_data = json.dumps(full_aya_dec, default=lambda o: o.__dict__, indent=4, ensure_ascii=False)#.encode('utf-8')
        print(sys.getdefaultencoding())

        # json_data =json.dumps(full_aya_dec, default=lambda o: o.__dict__, indent=4, ensure_ascii=False).encode('utf_8').decode('utf_8') #.decode('unicode-escape').encode('utf8')
        # json_data =json.dumps(full_aya_dec, default=lambda o: o.__dict__, indent=4)
        # .encode('windows-1256')

        # return json.JSONDecoder().decode(json_data)
        # return json_databv
        # return json.loads(araby.autocorrect(json_data.encode('utf8')))
        # return [json.loads(full_aya_dec[key]) for key in full_aya_dec]
        # return json.loads(aya_dict)
        # person = '{"name": "Bob", "languages": ["English", "Fench"]}'
        # return aya_dict
        # return
        return full_aya_dec

    @staticmethod
    def get_word_weight(one_word):
        """
        get word by word alphabet weight in numbers and loop in word by word alphabets
        :param one_word: arabic word
        :return: total word weight in numbers
        """
        total = 0
        alphabet_dict = []
        origin_word = one_word
        for v in one_word:
            single_alphabet = Util.find_special_alphabet(v)
            weight = Util.find_in_alph_weight(single_alphabet)
            if weight is not None:
                count = Util.find_in_alph_weight(single_alphabet)
                alphabet_dict.append(aya_alphabet(alphabet=v, alphabet_weight=count))
                total += count
            print("الحرف : ", v)
            print("الوزن: ", Util.find_in_alph_weight(v))

        one_word_object = aya_word(aya_word=origin_word, word_weight=total, word_alphabets=alphabet_dict)
        print(" اجمالي الكلمه: ", total)
        return one_word_object
