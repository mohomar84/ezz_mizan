# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from mizan.aya_weight.aya_weight_count import aya_weight


def metric(aya):
    # Use a breakpoint in the code line below to debug your script.
    aya = "في قلوبهم مرض فزادهم الله مرضا ولهم عذاب أليم بما كانوا يكذبون"
    aya_weight(aya)
    print(f' آية :  {aya}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    metric('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
