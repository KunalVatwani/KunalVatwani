import random
def print_scores(use_score,cpu_score):
    print("Your score = {}".format(user_score))
    print("Computer's score = {}".format(cpu_score))

cpu = ['stone','paper','scissor']
print('Enter the number of times you want to play.')
chances = int(input())
user_score = 0
cpu_score = 0
for i in range(chances):
# while (user_score!=5 or cpu_score!=5):
    print('Enter your move')
    user_move = input()
    cpu_move = random.choice(cpu)
    print("Computer's move : {}".format(cpu_move) )
    if (user_move==cpu_move):
        print_scores(user_score,cpu_score)    
    elif (user_move=='scissor' and cpu_move=='stone'):
        cpu_score+=1
        print_scores(user_score,cpu_score)
    elif (user_move=='scissor' and cpu_move=='paper'):
        user_score+=1
        print_scores(user_score,cpu_score)
    elif (user_move=='stone' and cpu_move=='scissor'):
        user_score+=1
        print_scores(user_score,cpu_score)
    elif (user_move=='stone' and cpu_move=='paper'):
        cpu_score+=1
        print_scores(user_score,cpu_score)
    elif (user_move=='paper' and cpu_move=='scissor'):
        cpu_score+=1
        print_scores(user_score,cpu_score)
    elif (user_move=='paper' and cpu_move=='stone'):
        user_score+=1
        print_scores(user_score,cpu_score)
    else :
        print("Invalid Input. Try again")
    print('')
        
if (user_score>cpu_score):
    print('You won!!')
elif (user_score==cpu_score):
    print('It is a tie!!')
else :
    print('Sorry you lost.')