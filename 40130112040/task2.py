s = input("enter array : ")
k = int(input("enter k : "))

s = s[1:len(s) - 1]

array = []

for i in s.split(','):
    array.append(int(i.strip()))

n = len(array)

for r in range(k):

    temp = array[n-1]
    for i in range(n-1, 0, -1):
        array[i] = array[i-1]
    array[0] = temp

print(array)