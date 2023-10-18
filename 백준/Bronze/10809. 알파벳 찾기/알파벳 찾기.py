
alpha = [-1]*26
word = input()

alp = list(set(word))

for i in alp:
    alpha[ord(i)-97] = word.index(i)

for i in alpha:
    print(i, end=" ")