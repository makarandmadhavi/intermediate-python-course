import random
def main():
  dicerolls = 2
  dice_sum = 0
  for i in range(0,dicerolls):
    roll= random.randint(1,6)
    dice_sum += roll
    print(f'You rolled a {roll}')
  print(f'You have rolled a total of {dice_sum}')
if __name__== "__main__":
  main()