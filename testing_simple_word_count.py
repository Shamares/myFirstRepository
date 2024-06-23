# simple testing word count in a string
con = True
while con is True:
    print('Enter your text')
    string = input()
    words = string.split()
    total = 0
    for words in words:
        total = total + 1
    print("The total number of words in example sentence is ", total)
    ans = "lol"
    while ans != "y" and ans != "n":
        print("Do you wish to try again?(Y/N)")
        ans = str.lower(input())
        if ans == "n":
            con = False
else:
    print("Goodbye!")
