s1 = input("enter array : ")
s2 = input("enter array : ")

s1 = s1[1:len(s1) - 1]
s2 = s2[1:len(s2) - 1]

array1 = []
array2 = []

for i in s1.split(','):
    array1.append(int(i.strip()))
for i in s2.split(','):
    array2.append(int(i.strip()))

n1 = len(array1)
n2 = len(array2)

i = 0 
j = 0

res = []

while i < n1 and j < n2:

    if(array1[i] <= array2[j]):
        res.append(array1[i])
        i += 1
    else:
        res.append(array2[j])
        j += 1

while i < n1:
    res.append(array1[i])
    i += 1

while j < n2:
    res.append(array2[j])
    j += 1

print(res)