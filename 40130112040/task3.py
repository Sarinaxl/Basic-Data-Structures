s = input("enter array : ")

s = s[1:len(s) - 1]

array = []

for i in s.split(','):
    array.append(int(i.strip()))

n = len(array)


for i in range(n-1):

    if array[i] == array[i+1]:
        
        for j in range(i+1, n-1):
            array[j] = array[j+1]
        n -= 1
        array.pop(n)

    if(i >= n-1):
        break



print(n)