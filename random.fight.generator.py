import random
fighter1 = input("enter the first fighter: ")
fighter2 = input('enter the second fighter: ')
BY = random.choice(['unanimous decision', 'split decision', 'TKO', 'submission'])
winner = random.choice([fighter1, fighter2])
print(f'And winner by', BY, 'is:', winner )