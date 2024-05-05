import random

c = ['rock', 'paper', 'scissors']
u = input('Rock Paper Scissors: ')
p = random.choice(c)
print(p)

if p == 'rock' and u == 'paper':
    print('You Win!')
if p == 'rock' and u == 'rock':
    print('Draw')
if p == 'rock' and u == 'scissors':
    print('You Lose!')
if p == 'paper' and u == 'paper':
    print('Draw')
if p == 'paper' and u == 'rock':
    print('You Lose!')
if p == 'paper' and u == 'scissors':
    print('You Win!')
if p == 'scissors' and u == 'paper':
    print('You Lose:')
if p == 'scissors' and u == 'rock':
    print('You Win!')
if p == 'scissors' and u == 'scissors':
    print('Draw')
