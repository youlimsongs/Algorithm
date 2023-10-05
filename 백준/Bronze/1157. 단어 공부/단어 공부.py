cnt = [0]*26
s = input()

for i in range(len(s)):
    if( ord(s[i])>96):
        index = ord(s[i])-97
        cnt[index] += 1
    else:
        index = ord(s[i])-65
        cnt[index] += 1

max_index =cnt.index(max(cnt))


for i in cnt[max_index+1:]:
    if(max(cnt)!= i):
        continue

    else:
        print("?")
        exit(0)
        
        
print(chr(max_index+65))