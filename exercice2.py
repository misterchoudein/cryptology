#exercices
V = ['car','plane','train','bike','boat','car']
V.remove('train')
#print(V)


V.pop(2)
#print(V)


#print(V.count('car'))

#/counting using a loop
count = 0
for i in V:
    if i == 'car':
        count += 1
#print("the result using a loop is", count)

#same thing using format string
#print("the result using format string is {0}".format(count))

#generate a list of 10 elements of random number. the value of each element should be between 0 and 100, using comprehension syntax, 3 lines of code max
import random
L = [random.randint(0,100) for i in range(10)]
#print("ma liste random: {0}".format(L))

#generate a list of 10 random elements 'sup' or 'inf', to do that generate a random value between 0 and 100 and add 'sup' if the value is greater than 50, 'inf' otherwise, using comprehension syntax, 3 lines of code max
L = ['sup' if random.randint(0,100) > 50 else 'inf' for i in range(10)]
#print("ma liste random: {0}".format(L))




#calculate the number of each letter in the text file lorem.txt, 6 lines max

with open('lorem.txt', 'r') as file:
    text = file.read()
    print({i:text.count(i) for i in text})
    