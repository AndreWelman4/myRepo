import random

def play():
    user = input("'r' for rock, 'p' for paper, 's' for scissors")
    computer = random.choice(['r', 'p', 's'])

    if user == computer;
        return 'tie'
    #r>s, s>p, p>r
    
def isWin(player, opponent):
    #return true if player wins
    #r>s, s>p, p>r
    if(player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r ')
        return True
    #https://www.youtube.com/watch?v=8ext9G7xspg