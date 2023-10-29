import random
from tkinter import *
from tkinter import messagebox
from typing import List, Dict
import matplotlib.pyplot as plt

phone = [
    "I'm not sure but I think the correct answer is...", 
    "I am pretty sure that the answer is...", 
    "This question is very easy, the correct answer is..."
]

def popup(text) -> None:
    top = Tk() # to hide the main window
    top.wm_withdraw()
    messagebox.showinfo(title='Phone-a-Friend', message=text)

def use_audience(question) -> List[int]:
    if (question.option_A == '-' or question.option_B == '-' or question.option_C == '-' or question.option_D == '-'):
        correct = random.randint(51,99)
        wrong_one = 100 - correct
        return [correct, wrong_one]
    else:
        correct = random.randint(51,70)
        diff = 100 - correct
        wrong_one = random.randint(1, diff - 2)
        diff = 100 - correct - wrong_one
        wrong_two = random.randint(1, diff - 1)
        diff = 100 - correct - wrong_one - wrong_two
        wrong_three = diff
        return [correct, wrong_one, wrong_two, wrong_three]
    
def evaluate_audience(question, values) -> Dict[str, int]:
    options = ["A", "B", "C", "D"]
    my_dict = {}

    if len(values) == 4:
        my_dict[question.correct_answer] = values[0]
        options.remove(question.correct_answer)
        values.pop(0)

        for i in range(0, 3):
            answer = random.choice(options)
            number = random.choice(values)
            my_dict[answer] = number
            options.remove(answer)
            values.remove(number)
    return my_dict

def diagram(values) -> None:
    names = values.keys()
    val = values.values()

    plt.figure(figsize=(6, 5))
    plt.ylabel('Percentage (%)', fontsize=16)
    plt.xlabel('Options', fontsize=16)
    plt.bar(names, val)
    plt.suptitle('Audience results', fontsize=20)
    plt.show()

def phone_call(question) -> str:
    text = random.choice(phone)
    complete_text = f"""*ringing sound*
Let me hear the question.
*thinking*
{text} {question.correct_answer}"""
    return complete_text
