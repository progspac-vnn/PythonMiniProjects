# Converter ---> progspacvnn

print('/////// BINARY TO DECIMAL CONVERTER ///////')
a = int(input('Enter 1st digit\n'))
b = int(input('Enter 2nd digit\n'))
c = int(input('Enter 3rd digit\n'))
d = int(input('Enter 4th digit\n'))
e = int(input('Enter 5th digit\n'))
f = int(input('Enter 6th digit\n'))
g = int(input('Enter 7th digit\n'))

l = [a,b,c,d,e,f,g]
s = 0

for i in range(0,7):
    l[i] = l[i] * (2**(6-i))
for i in range(0,7):
    s = s + l[i]

print('/////// HERE IS YOUR RESULT ///////')
print(f'---------> {s}')