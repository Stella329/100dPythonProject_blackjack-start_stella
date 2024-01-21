#准备条件
import replit  #clear()
import random
#创建：仓
user_cards = [] #玩家仓_list
computer_cards = [] #电脑仓_list


#**************创建：各种游戏函数
#抽牌函数
def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] #Ace=11 or 1
  chosed_card = random.choice(cards)
  return chosed_card

#添牌入牌仓函数
def cardset_fun(c, whose_cards): #whose_card=list name仓名
  whose_cards.append(c)  #添牌
  return whose_cards

#算分函数:直接cardset中数字相加
def score_fun(whose_cards):
  score = 0 
  for card in whose_cards: #加总分
    score += card
  if 11 in whose_cards: #如果有ace,判断ace算11 or 1
    if score >= 10 and score != 21: 
      score -= 10
  return score

#比分函数:
def scorecheck_fun(user_cards,user_score, computer_cards,computer_score):
  #结果展示
  print('\n🤑Here is the result!!!:')
  print(f'😈Your card set is {user_cards}; Your currect score is {user_score}')
  print(f'👺Computer\'s card set is {computer_cards}; Computer\'s score is {computer_score}.\n')


  if user_score < 21 and computer_score <= 21: #a. 小于21
    if user_score < computer_score:
      print(f'Computer gets a higher score. You lose.😥')
    elif user_score > computer_score:
      print('You get a higher score, you win.🎈')
    elif user_score == computer_score:
      print('It is a draw.🎭')
  elif user_score == 21: #c.玩家等于21
    print('You reach 21!!!! You absolutely win!! 🎈🎈🎈')
  else: #b. 大于21
    if user_score > 21:
      print('Your scores went over 21, blast!🎇')
    elif computer_score > 21: 
      print('Computer\'s scores went over 21, blast! You win!🎈')
    elif computer_score > 21 and user_score > 21:
      print('You both went over 21. Blast! It\'s a draw.🎭')

#if_continue: var = continue_play
def if_continue():
  continue_play = True
  user_input = input('\nDo you want another card? Type y or n: ').lower()
  if user_input == 'n':
    continue_play = False
  return continue_play


#***********游戏规则函数（game-playing-related) 

def game_playing():
  user_cards = [] #玩家仓_list
  computer_cards = [] #电脑仓_list

  #User
  c1=deal_card()
  c2=deal_card()

  user_cards = cardset_fun(c=c1, whose_cards=user_cards) #第1轮抽牌
  user_cards = cardset_fun(c=c2, whose_cards=user_cards)
  user_score = score_fun(user_cards)
  print(f'Your card set is {user_cards}; Your currect score is {user_score}')

  #Computer
  cc1=deal_card()
  cc2=deal_card()
  computer_cards = cardset_fun(c=cc1, whose_cards=computer_cards)
  computer_cards = cardset_fun(c=cc2, whose_cards=computer_cards)
  computer_score = score_fun(computer_cards)

  while computer_score < 16:
    cc3 = deal_card()
    computer_cards = cardset_fun(c=cc3, whose_cards=computer_cards)
    computer_score = score_fun(computer_cards)

  print(f'Computer\'s first card is {cc1}.\n')

  #user是否继续摸牌
  continue_play = if_continue()
  while continue_play == True:
    c3 = deal_card() #2+轮抽牌
    user_cards = cardset_fun(c=c3, whose_cards=user_cards)
    user_score = score_fun(whose_cards=user_cards)
    print(f'Your card set is {user_cards}; Your currect score is {user_score}') #user最新比分
    print(f'Computer\'s first card set is {cc1}.\n')
    continue_play = if_continue() #直到‘n’后才结束

  #比分
  scorecheck_fun(user_cards,user_score, computer_cards,computer_score)
  #游戏结束后：判定是否继续
  continue_play = input('Do you want another round? y or n: ').lower()
  if continue_play == 'y':
    continue_play = True
    replit.clear()
  else:
    continue_play = False
  return continue_play



#*************游戏进行函数（flow-related）
def game_running():
  wanna_play = input('Do you want to play BlackJack? (y or n): ').lower()

  if wanna_play == 'n': #游戏结束
    continue_play = False

  else: #游戏继续进行
    from art import logo
    print(logo)

    continue_play=game_playing() #********引用游戏函数******

  #!!!完成一轮：反馈给while loop，否则error：返回none!!!
  return continue_play


#**********开始游戏*********
#game_status
continue_play = True 

#游戏进行：call the function
while continue_play == True:
  continue_play = game_running() #call func +用变量take the return value

#结束：while loop结束
print('\nGoodbye! 👹') 
