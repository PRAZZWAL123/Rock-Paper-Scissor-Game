"""
Workflow of project:
1- Input from user(Rock,paper,scissor)
2-computer choice (Computer will chosse randomly not conditionally)
3-Result prin

Case:
A-Rock
Rock - Rock = tie
Rock - Paper = Paper win
Rock -Scissor = Rock win

B- Paper
Paper - Paper = tie
Paper- Rock = Paper win
Paper - Scissor = Scissor win

C-Scissor
Scissor - Scissor = tie
Scissor - Rock = Rock win
scissor - Paper = Scissor win

"""

import random
item_list = ["Rock","Paper", "Scissor"]

user_choice = input("Enter you move = Rock, Paper, Scissor= ")
comp_choice = random.choice(item_list)

print(f"User choice ={user_choice}, Computer Choice ={comp_choice}")

if user_choice == comp_choice:
    print("Both choses same: = Math Tie")
elif user_choice == "Rock":
     if comp_choice =="Paper":
      print("Paper covers Rock = Computer Win")    
     else:
        print("Rock smashes Scissor = You Win")
elif user_choice == "Paper":
   if comp_choice == "Scissor":
      print("Scissor cuts paper, Computer Win")
   else:
        print("Paper covers rocks, You win")
elif user_choice == "Scissor":
    if comp_choice =="Paper":
        print("Scissor cuts paper, You win")    
    else:
        print("Rock smashes scissor, Computer win")        