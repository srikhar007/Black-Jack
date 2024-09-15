print("WELCOME TO THE BLACK JACK GAME ♠️ ♥️ ♦️ ♣️:\n")

#to take random cards we use random module.
#to take random card in list we use random.choice() function.
#return is the output of the function.
#we can use return to save the output of the function in a variable.

import random

from art import logo

def deal_card():
  cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
  card=random.choice(cards)
  return card

#now the players come in.
#the user and computer.
#we can use list to save the cards of the players.
#append() function is used to add items in list.



#now we should calculate the score of the player.
#it will cal all numbers of the users.
#sum() will add the numbers.
#to cal the score the function is replaced here.from below.
def calculate_score(cards):
#if ace and 10 is in the list return 0.
  if sum(cards)==21 and len(cards)==2:
    return 0
  #if the sum >21 with ace,then remove 11 and add 1.
  if 11 in cards and sum(cards)>21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

#now we need to comparethe scores.
#compare() function is used. 
def compare(user_score,computer_score):
  if user_score==computer_score:
    return "draw match😂"
  elif computer_score==0:
    return "you lose,computer has black jack..😒"
  elif user_score==0:
    return "you win,you have the black jack😎😎"
  elif user_score>21:
    return "you lose,the score went high..😒😒"
  elif computer_score>21:
    return "you win,commputer went high..😎😎"
  elif user_score>computer_score:
    return "you win..😎😎"
  else:
    return "you lose..😒😒"
    
def play_game():
  print(logo)

  user_cards=[]
  computer_cards=[]
  is_game_over=False
  for _ in range(2):
  
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  #to continue many times while loop used.
  while not is_game_over:
  
    user_score=calculate_score(user_cards)
    computer_score=calculate_score(computer_cards)
    #printing the cards and score to see.
    print(f"your cards:{user_cards},current score:{user_score}")
    print(f"computer first card: {computer_cards[0]}")
    #check for user and computer has blackjack '0' and >21 the game ends.
    if user_score==0 or computer_score==0 or user_score > 21:
      is_game_over=True
      #to continue further with cards,ask user to draw the cards.
    else:
      user_should_deal=input("type 'y' to get another card,type 'n' to pass:")
      if user_should_deal=='y':
        user_cards.append(deal_card())
      else:
        is_game_over=True
  
  #now the computers turn..
  #while is used to pick n number of cards.
  while computer_score!=0 and computer_score<17:
    computer_cards.append(deal_card())
    computer_score=calculate_score(computer_cards)
  #now call the compare function.and print it.
  print(f"your final hand:{user_cards},final score:{user_score}")
  print(f"computer final hand:{computer_cards},final score:{computer_score}")
  print(compare(user_score,computer_score))

#ask the user to play again.
# if yes the screen clears and starts over.
#if no game ends.
while input("type 'yes' to play black jack,type 'no' to end the game:")=='yes':

  play_game()