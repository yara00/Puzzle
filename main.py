# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import State

# Press the green button in the gutter to run the script.


if __name__ == '__main__':
    s1 = State.State()
    s1.set_state(123456780)
    print(s1.find_neighbours())
    res = str(123456789).zfill(10)
    print(res)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
