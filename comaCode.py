spam = ['apples', 'bananas', 'tofu', 'cats']
spam_len = len(spam)
for i in range(0, spam_len - 1 ):
    print(spam[i] + ", ", end="")
print("and " + spam[-1])
