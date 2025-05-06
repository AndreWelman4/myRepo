import random

def guess(x):
    randomNumber = random.randint(1, x)
    guess = 0
    while guess != randomNumber:
        guess = int(input(f'Guess a number inbetween 1 and {x}: '))
        if guess < randomNumber:
            print('Sorry. Guess again, to low')
        elif guess > randomNumber:
            print('Sorry. Guess again, to high')
    print(f'Congrats, you have guessed the number {randomNumber} correctly')

def computerGuess(x):
  low = 1
  high = x
  feedback = ''
  while feedback != 'c':
        if low != high:
           guess = random.randint(low, high)
        else:
            guess = low  
        feedback = input(f'Is {guess} too high (H), too low (L), correct (C)??').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
            print(f'I won, because I guessed the number {guess}, correctly')

#guess(10)   
computerGuess(10)