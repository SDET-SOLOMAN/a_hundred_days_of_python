import pandas

names_data = pandas.read_csv('nato_phonetic_alphabet.csv')

name = input("Please type your name: ").upper()

names = {row.letter: row.code for index, row in names_data.iterrows()}

print([names[k] if k in names else " " for k in name])
