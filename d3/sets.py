s1 = set(['cool', 1, 3.14])
s2 = set('cool')
s1.add(5)
s1.add("aaa")
s1.add((1, 2, 3))
s1.remove('cool')

print(s1, s2)

A = set([1, 2, 3, 4, 5])
B = set([3, 4, 5, 6, 7, 8, 9])

union = A | B
intersection = A & B
difference = A - B
sym_difference = A ^ B
print(f"suma: {union}")
print(f"część wspólna: {intersection}")
print(f"różnica: {difference}")
print(f"różnica symetryczna: {sym_difference}")


sentence = 'to be or not to be'
words = sentence.split(" ")
init = set(words)
print(init)

numbers = [1,2,3,4,4,32,2,13,4,5,3,1]
set_of_even_numbers = set([number for number in numbers if number % 2 == 0])
print(set_of_even_numbers)