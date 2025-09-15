numbers_100 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
unique_numbers_100 = set(numbers_100)
for i in unique_numbers_100 :
    print(i, end = " , ")


    #membership checking
favourite_animals = {'cat', 'dog', 'lion', 'elephant', 'hippopotamus', 'tiger', 'deer', 'giraffe', 'monkey', 'cheetah'}
guessed_animal = input("guess one of my favourite animals:")
if guessed_animal in favourite_animals:
    print("hurray, you have guessed it right!")
else:
    print("you have failed in guessing !!! try again")
