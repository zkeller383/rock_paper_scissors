import time #Used for sleep commands.
import random #Used for computer's choice.

yes_list = ['yes', 'Yes', 'y', 'Y']
no_list = ['no', 'No', 'n', 'N']
play_list = ['rock', 'paper', 'scissors']

i = 1
while i <= 1:
    
    wanna_play = input("Wanna play rock paper scissors?(Y/N)\n")

    if wanna_play in yes_list:
        print("Then show me what you've got!\n")
        time.sleep(1)
        
        user_choice = input("rock, paper, or scissors?:\n") #prompt user for their choice
        comp_choice = random.choice(play_list) #computer randomly selects one of the three choices
            
            
        print("Alright here we go!\n")
        time.sleep(0.5)
        print('rock!')
        time.sleep(0.5)
        print('paper!')
        time.sleep(0.5)
        print('scissors!')
        time.sleep(0.5)
        print('shoot!\n')
        time.sleep(0.5)
        print("You chose", user_choice, "and I chose", comp_choice, '\n')
        time.sleep(1.5)
            
        if user_choice == comp_choice:
            print("Darn! We tied!\n")
            time.sleep(1)
            play_again = input("Wanna try again?(Y/N)\n")
            if play_again in yes_list:
                continue
            else:
                print("Then see you later!\n")
                break
        elif user_choice == 'rock':
            if comp_choice == 'scissors':
                print("Rock breaks scissors! You Win!\n")
                break
            else:
                print("Paper covers rock! You Lose! Better luck next time!\n")
                time.sleep(1)
                play_again = input("Wanna try again?(Y/N)\n")
                if play_again in yes_list:
                    continue
                else:
                    print("Then see you later!\n")
                    break
        elif user_choice == 'paper':
            if comp_choice == 'rock':
                print("Paper covers rock! You Win!\n")
                break
            else:
                print("Scissors cuts paper! You Lose! Better luck next time!\n")
                time.sleep(1)
                play_again = input("Wanna try again?(Y/N)\n")
                if play_again in yes_list:
                    continue
                else:
                    print("Then see you later!\n")
                    break
        elif user_choice == 'scissors':
            if comp_choice == 'paper':
                print("Scissors cuts paper! You Win!\n")
                break
            else:
                print("Rock breaks scissors! You Lose! Better luck next time!\n")
                time.sleep(1)
                play_again = input("Wanna try again?(Y/N)\n")
                if play_again in yes_list:
                    continue
                else:
                    print("Then see you later!\n")
                    break
                    
    
    
    elif wanna_play in no_list:
        print("Stop wasting my time!\n")
        time.sleep(1)
        continue
