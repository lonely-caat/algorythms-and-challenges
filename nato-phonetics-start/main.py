import pandas as pd
data = pd.read_csv('nato_phonetic_alphabet.csv')


# Keyword Method with iterrows()
meow = {row['letter']:row['code'] for (row, row) in data.iterrows()}


def name_substitute(name):
    print([meow[letter.title()] for letter in name])
    # for letter in name:
        # print(meow[letter.upper()])


name_substitute('Kate')