n = input().strip()

i = 0
length = len(n)

while i < length:
    if i + 2 < length and n[i:i+3] == '144':
        i += 3 
    elif i + 1 < length and n[i:i+2] == '14':
        i += 2  
    elif n[i:i+1] == '1':
        i += 1  
    else:
        print("NO")
        break
else:
    print("YES")
