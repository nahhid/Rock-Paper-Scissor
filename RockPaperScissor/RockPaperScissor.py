from tkinter import *
from random import choice

global userWinCounter
userWinCounter = 0
global computerWinCounter
computerWinCounter = 0

def choose_option(user_choice):
    options = ['سنگ', 'کاغذ', 'قیچی']
    computer_choice = choice(options)
    result = determine_winner(user_choice, computer_choice)
    result_label.config(text=f'انتخاب کاربر: {user_choice}\nانتخاب کامپیوتر: {computer_choice}\nنتیجه: {result}')

def determine_winner(user, computer):
    global userWinCounter
    global computerWinCounter
    
    if user == computer:
        text1 = "امتیاز شما: {} ".format(userWinCounter)
        text2 = "\n امتیاز کامپیوتر: {}".format(computerWinCounter)
        return "مساوی \n\n" + text1 + text2
    
    elif (user == 'سنگ' and computer == 'قیچی') or (user == 'کاغذ' and computer == 'سنگ') or (user == 'قیچی' and computer == 'کاغذ'):
        userWinCounter += 1
        uText1 = "امتیاز شما: {} ".format(userWinCounter)
        uText2 = "\n امتیاز کامپیوتر: {}".format(computerWinCounter)
        return "شما برنده شدید \n\n" + uText1 + uText2
    
    else:
        computerWinCounter += 1
        cText1 = "امتیاز شما: {} ".format(userWinCounter)
        cText2 = "\n امتیاز کامپیوتر: {}".format(computerWinCounter)
        return "کامپیوتر برنده شد \n\n" + cText1 + cText2

# main window
root = Tk()
root.title('سنگ کاغذ قیچی')

root.geometry("400x400")

# buttons
rock_button = Button(root, text = 'سنگ', command=lambda: choose_option('سنگ'))
rock_button.pack(pady = 5)
paper_button = Button(root, text = 'کاغذ', command=lambda: choose_option('کاغذ'))
paper_button.pack(pady = 5)
scissors_button = Button(root, text = 'قیچی', command=lambda: choose_option('قیچی'))
scissors_button.pack(pady = 5)


# show result
result_label = Label(root, text='')
result_label.pack()
result_label.pack(pady=20)


root.mainloop()