import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")

# Another form of doing it
# data = {}
# for (index, row) in df.iterrows():
#     data[row.letter] = row.code
data = {row.letter: row.code for (index, row) in df.iterrows()}


word = input("Input a word pls: ").upper()
output = []

for ch in word:
    pre_output = {output.append(value) for (key, value) in data.items() if ch == key}

print(output)
# Soy ADMIN
