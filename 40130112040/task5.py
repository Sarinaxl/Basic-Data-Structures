s = input("enter array : ")

s = s[1:len(s) - 1]

a = []

for i in s.split(','):
    a.append(int(i.strip()))

size = len(a)

max_so_far = a[0]
max_ending_here = 0
start = 0
end = 0
s = 0

for i in range(0,size):

    max_ending_here += a[i]

    if max_so_far < max_ending_here:
        max_so_far = max_ending_here
        start = s
        end = i

    if max_ending_here < 0:
        max_ending_here = 0
        s = i+1


print(max_so_far)
print(a[start:end+1])