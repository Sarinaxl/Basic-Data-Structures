s = input("enter array : ")

s = s[1:len(s) - 1]

array = []

for i in s.split(','):
    array.append(int(i.strip()))

n = len(array) + 1

check = []

for i in range(n):
    check.append(False)

for i in array:
    check[i] = True

for i in check:
    if(i == False):
        print(check.index(i))
        break