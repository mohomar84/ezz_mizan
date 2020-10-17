from quaran_count_waight.common.alphabets_weight import ArWeight


# param
aya = "في قلوبهم مرض فزادهم الله مرضا ولهم عذاب أليم بما كانوا يكذبون"


def aya_weight(aya:str):

    all_words = aya.split(" ")
    total = 0
    words_count = 0

    for i in all_words:
        if i != '':
            print("الكلمه : ", i)
            one_word = list(i)
            word_count = get_word_count(one_word)
            words_count += 1
            total += word_count
    print("-------------")
    print("عدد الكلمات : ", words_count)
    print(" وزن الايه : ", total)
    print("-------------")


def get_word_count(one_word):
    total = 0
    for v in one_word:
        weight = find_in_alph_weight(v)
        if weight is not None:
            total += find_in_alph_weight(v)
        print("الحرف : ", v)
        print("الوزن: ", find_in_alph_weight(v))
    print(" اجمالي الكلمه: ", total)
    return total


def find_in_alph_weight(alpha):
    for d in ArWeight:
        if alpha == d.name:
            return d.value


aya_weight(aya)
