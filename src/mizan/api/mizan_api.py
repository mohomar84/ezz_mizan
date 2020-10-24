from flask import json

from mizan.aya_weight.aya_weight_count import alphabet_weight


def read():
    aya = "في قلوبهم مرض فزادهم الله مرضا ولهم عذاب أليم بما كانوا يكذبون"
    strr = alphabet_weight.aya_weight(aya)
    print("********************************************************************")


    return json.dumps(strr, default=lambda o: o.__dict__, indent=4 , encoding='ISO 8859-6')
    # return json.jsonify(strr)
