from quaran_count_waight.common.alphabets_weight import ArWeight


def aya_weight(aya: str):

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
        single_alphabet = find_special_alphabet(v)
        weight = find_in_alph_weight(single_alphabet)
        if weight is not None:
            total += find_in_alph_weight(single_alphabet)
        print("الحرف : ", v)
        print("الوزن: ", find_in_alph_weight(v))
    print(" اجمالي الكلمه: ", total)
    return total


def find_in_alph_weight(alpha):
    for d in ArWeight:
        if alpha == d.name:
            return d.value


def find_special_alphabet(character):
    sp_alpha = ["إ", "أ", "ٱ", "آ", "ى", "ؤ", "ئ", "ة"]
    for v in sp_alpha:
        if v == character:
            print(True, character)
            return alphabet(character)
    return character


def alphabet(sp_alphabet):
    a_alpha = ["إ", "أ", "ٱ", "آ"]
    i_alpha = ["ى", "ؤ", "ئ", "ة"]
    h_alpha = ["ة"]
    if sp_alphabet in a_alpha:
        return "ا"
    if sp_alphabet in i_alpha:
        return "ي"
    if sp_alphabet in h_alpha:
        return "ه"
