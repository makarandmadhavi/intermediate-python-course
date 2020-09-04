import random
def main():
  dice_sum = 0
  pname = [0,0]
  pscore = [0,0]
  pname[0] = input('Player 1 what is your name? ')
  pname[1] = input('Player 2 what should we call you? ')
  dicerolls = int(input('How many dice would you like to roll? '))
  dice_size = int(input('How many sides are the dice? '))
  for j in range(0,2):
    for i in range(0,dicerolls):
      roll= random.randint(1,dice_size)
      pscore[j] += roll
      if roll == 1:
        print(f'{pname[j]} rolled a {roll}! Critical Fail')
      elif roll == dice_size:
        print(f'{pname[j]} rolled a {roll}! Critical Success!')
      else:
        print(f'{pname[j]} rolled a {roll}')
    print(f'{pname[j]} have rolled a total of {dice_sum}')
  if(pscore[0]>pscore[1]):
    print(f'{pname[0]} Wins!')
  else:
    print(f'{pname[1]} Wins!')
if __name__== "__main__":
  main()