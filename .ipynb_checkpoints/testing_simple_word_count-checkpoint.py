#simple testing word count in a string

string = "Szeth-son-son-Vallano, Truthless of Shinovar, wore white on the day he was to kill a king. The white clothing was a Parshendi tradition, foreign to him. But he did as his masters required and did not ask for an explanation."

words = []
words = string.split()
total = 0
for words in words:
    total = total + 1
print("The total number of words in example sentence is ", total)