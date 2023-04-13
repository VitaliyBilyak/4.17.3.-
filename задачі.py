#1
print('Завдання 1')
Мова = ["Ukrainian", "French", "Bulgarian", "Norwegian", "Latvian"]
print(Мова)
print(sorted(Мова))
Мова.reverse()
print(Мова)
Мова.sort()
print(Мова)

#2
print('Завдання 2')
N='2 -1 9 6'
numbers = list(map(int, N.split()))
print(sum(numbers))

#3
print('Завдання 3')
cities = ['Budapest', 'Rome', 'Istanbul', 'Sydney', 'Kyiv', 'Hong Kong']
# з командою join для об'єднання елементів і пропусків ,
print(", ".join(cities[:-1]) + " and " +  cities[-1])
# sep у нас ставляє замість пропусків кому а and обєднує print і добавляє між німи and
print(cities[0],cities[1],cities[2],cities[3],cities[4], sep=',',end=' and ')
print(cities[5])

#4
print('Завдання 4')
W='1 2 3 4 5'
reversed_digits = sorted(W, reverse=True)
print("".join(map(str, reversed_digits)))

#5
print('Завдання 5')
a=['doctor','programmer','actor','artist']
a.append('baker')
print(a)
a.insert(1,'coach')
print(a)
a.remove('programmer')
print(a)
a[2] = 'fisherman'
print(a)
a.extend(['composer','farmer'])
print(a)
a.sort()
print(a)
a.reverse()
print(a)
a.pop(-1)
print(a)
a.clear()
print(a)
print(a.count('coach'))
print(len(a))

#6
print('Завдання 6')
h=['12']
for i in h:
    if i is '12' :
        print('Є цифра 12')
    else:
        print('Цифри немає або інша цифри')