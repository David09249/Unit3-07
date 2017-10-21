# Created by : David Wang
# Created on : 20 Oct 2017
# Created for : ICS3UR
# Daily Assignment - Unit3-07
# This program displays the factorial program but with for loops.

import ui

def calculate_touch_up_inside(sender):
    
    number = 1
    user = int(view['user_input_textbox'].text)
    
    if user < 1:
        view['answer_label'].text = "Please enter a valid number."
    
    else:         
        integer = user
        integer = int(integer) + 1
        for i in range(1, integer):
            number = number * i
        view['answer_label'].text = "The factorial is: " + str(number)

view = ui.load_view()
view.present('full_screen')
