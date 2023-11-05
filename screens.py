import pygame
import sys
from rectangular import *
from constants import *
import button
import tkinter
from tkinter.simpledialog import askstring
from blur import blur

# Pygame has no opportunity to handle the messages it gets from your operation system. To avoid that, you should call pygame.event.pump()

pygame.font.init()

name = None

answer = None

fonts = [
    pygame.font.Font('freesansbold.ttf', 20),
    pygame.font.Font('freesansbold.ttf', 26),
    pygame.font.Font('freesansbold.ttf', 28),
    pygame.font.Font('freesansbold.ttf', 40),
    pygame.font.Font('freesansbold.ttf', 30),
    pygame.font.Font('freesansbold.ttf', 45)
]

def meets_name_criteria(your_name) -> bool:
    max_len = 16
    restricted_chars = {'`','~','!','@','#','$','%','^','&','*','(',')','_','-',
               '+','=','{','[','}','}','|','\\',':',';','"',"'",'<',',','>','.',
               '?','/'}
    if your_name is not None and your_name != "":
        if (len(your_name) < max_len and not any((char in your_name) for char in restricted_chars)):
            return True
        return False
    else:
        return False

def count_digits(number) -> int:
    count=0
    while(number > 0):
        number = number // 10
        count=count+1
    return count

def create_text(screen, text, pos, font) -> None:
    if text == "Game over!" or text == "The game has ended. You won!":
        font=fonts[font].render(text, False, RED, BLACK)
    else:
        font=fonts[font].render(text, False, WHITE, BLACK)
    screen.blit(font, (pos[0], pos[1]))
    pygame.display.update()
    pygame.time.delay(2000)
    pygame.event.pump()

def exit(screen):
    blur(screen)
    buttons = [
        button.Button(559, 552, 65, 15, WHITE, "yes"),
        button.Button(640, 552, 65, 15, WHITE, "no")
    ]
    for btn in buttons:
        btn.draw(screen)
    screen.blit(QUIT, (WIDTH / 2 - 125, HEIGHT / 2 - 70))
    pygame.display.update()

    pushed = False
    while(not pushed):
        for event in pygame.event.get():
            if buttons[0].isOver(pygame.mouse.get_pos()):
                pygame.draw.rect(screen, (0, 100, 255), (555, 548, 75, 23), 2)
                pygame.display.update()
            elif buttons[1].isOver(pygame.mouse.get_pos()):
                pygame.draw.rect(screen, (0, 100, 255), (635, 548, 75, 23), 2)
                pygame.display.update()
            else:
                screen.blit(QUIT, (WIDTH / 2 - 125, HEIGHT / 2 - 70))
                pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for btn in buttons:
                    if btn.isOver(pygame.mouse.get_pos()) and btn.type == "yes":
                        pygame.quit()
                        sys.exit()
                    if btn.isOver(pygame.mouse.get_pos()) and btn.type == "no":
                        pushed = True
            pygame.event.pump()

def stop_game(screen, money):
    blur(screen)
    buttons = [
        button.Button(559, 552, 65, 15, WHITE, "yes"),
        button.Button(640, 552, 65, 15, WHITE, "no")
    ]
    for btn in buttons:
        btn.draw(screen)
    screen.blit(STOP_GAME, (WIDTH / 2 - 125, HEIGHT / 2 - 70))
    pygame.display.update()

    pushed = False
    while(not pushed):
        for event in pygame.event.get():
            if buttons[0].isOver(pygame.mouse.get_pos()):
                pygame.draw.rect(screen, (0, 100, 255), (555, 548, 75, 23), 2)
                pygame.display.update()
            elif buttons[1].isOver(pygame.mouse.get_pos()):
                pygame.draw.rect(screen, (0, 100, 255), (635, 548, 75, 23), 2)
                pygame.display.update()
            else:
                screen.blit(STOP_GAME, (WIDTH / 2 - 125, HEIGHT / 2 - 70))
                pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for btn in buttons:
                    if btn.isOver(pygame.mouse.get_pos()) and btn.type == "yes":
                        gameover(screen, money)
                    if btn.isOver(pygame.mouse.get_pos()) and btn.type == "no":
                        pushed = True
            pygame.event.pump()

def menu(screen) -> None:
    running = True

    global answer

    screen.blit(BACKGROUND, (0, 0))

    while running:
        objects = [
            button.Button(315, 550, 600, 115, WHITE, "play","PLAY"),
            button.Button(315, 700, 600, 115, WHITE, "description","DESCRIPTION"),
            button.Button(315, 850, 600, 115, WHITE, "quit","QUIT")
        ]

        for obj in objects:
            obj.draw(screen)

        pygame.display.update()

        pushed = False
        while(not pushed):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for obj in objects:
                        value = obj.isOver(pygame.mouse.get_pos())
                        if (value and obj.type == "play"):
                            pushed = True
                            running = False
                        elif (value and obj.type == "description"):
                            description(screen)
                            pushed = True
                            running = False
                        elif (value and obj.type == "quit"):
                            exit(screen)
                            screen.blit(BACKGROUND, (0, 0))
                            for obj in objects:
                                obj.draw(screen)
                            pygame.display.update()

                if event.type == pygame.QUIT:
                    exit(screen)
                    screen.blit(BACKGROUND, (0, 0))
                    for obj in objects:
                        obj.draw(screen)
                    pygame.display.update()

    pygame.event.pump()

def description(screen) -> None:
    screen.blit(MAN, (0, 0))

    texts = [
        "The goal is to correctly answer 15 consecutive questions",
        "with each question having a higher prize value than the",
        "previous one, culminating in a grand prize of one million",
        "currency units.",
        "Choose from letters A, B, C or D to answer the question.",
        'Don\'t forget you have 3 jokers. "Ask the Audience",',
        'where the studio audience votes on the answer.',
        '"Phone-a-Friend", allowing contestants to make a call for',
        'help with the answer. "50:50", which removes two',
        'incorrect answers, leaving the correct answer and',
        'one remaining answer.',
        "You can stop and finish the game whenever you want to."
    ]

    start_screen = Rectangular(600, 20, 580, 500, WHITE)
    start_screen.draw(screen)

    for i in range(12):
        create_text(screen, texts[i], (605, (i + 1) * 40), 0)

    for _ in range(0, 8000, 1000):
        pygame.time.delay(1000)
        pygame.event.pump()

    menu(screen)


def start(screen) -> None:
    screen.blit(MAN, (0, 0))

    texts = [
        "Ladies and Gentlemen!",
        'Welcome to a new round of "Who wants to',
        'be a millionare!". We have a new candidate.'
    ]

    start_screen = Rectangular(600, 20, 580, 500, WHITE)
    start_screen.draw(screen)

    for i in range(3):
        if i == 0:
            create_text(screen, texts[i], (620, 40), 3)
        else:
            create_text(screen, texts[i], (620, 50 + (i * 60)), 1)
    global name
    my_w = tkinter.Tk()
    my_w.withdraw()
    name = askstring(title='Your name', prompt='What is your name?\n(max 16 character long and no special characters)')
    pygame.event.pump()
    crit = meets_name_criteria(name)
    while not crit:
        name = askstring(title='Your name', prompt='Please enter correct name!\n(max 16 character long and no special characters)')
        new_name = meets_name_criteria(name)
        if new_name:
            crit = True

    texts = [
        f"Welcome {name}!",
        "Everyone, a big round of applause.",
        "*applause*",
        "The game is about to begin in 5 seconds.",
        "Good luck!"
    ]
    for i in range(5):
        create_text(screen, texts[i], (620, 50 + ((i + 3) * 60)), 1)

    pygame.time.delay(2000)
    pygame.event.pump()

    my_w.destroy()

def gameover(screen, money) -> None:
    screen.blit(MAN, (0, 0))

    texts = [
        "Game over!",
        "Unfortunately you won no money.",
        f"You won {money}$.",
        "Thank you for playing!",
        "The game is about to quit in 5 seconds.",
        f"See you soon, bye {name}!"
    ]

    c = count_digits(money)

    end_screen = Rectangular(600, 20, 580, 500, WHITE)
    end_screen.draw(screen)

    create_text(screen, texts[0], (766, 90), 3)
    if money == 0:
        create_text(screen, texts[1], (660, 175), 2)
    else:
        create_text(screen, texts[2], (800 - c * 7, 175), 2)
    create_text(screen, texts[3], (730, 250), 2)
    create_text(screen, texts[4], (620, 325), 2)
    create_text(screen, texts[5], (750 - len(name) * 7 , 400), 2)

    pygame.time.delay(2000)
    pygame.event.pump()

    pygame.quit()
    sys.exit()

def winner(screen, money) -> None:
    screen.blit(MAN, (0, 0))

    texts = [
        "The game has ended. You won!",
        f"Your prize is {money}$.",
        "Thank you for playing!",
        "The game is about to quit in 5 seconds.",
        "See you soon, bye!"
    ]

    end_screen = Rectangular(600, 20, 580, 500, WHITE)
    end_screen.draw(screen)

    create_text(screen, texts[0], (680, 100), 2)
    create_text(screen, texts[1], (723, 175), 2)
    create_text(screen, texts[2], (730, 250), 2)
    create_text(screen, texts[3], (620, 325), 2)
    create_text(screen, texts[4], (750, 400), 2)

    pygame.time.delay(2000)
    pygame.event.pump()

    pygame.quit()
    sys.exit()

def audience_text(screen, font, text, pos):
    font = fonts[font].render(text, False, WHITE, BLACK)
    screen.blit(font, (pos[0], pos[1]))


def audience_diagram(screen, numbers):
    screen.blit(AUDIENCE, (0, 0))

    options = ["A", "B", "C" , "D"]

    objects = [
        Rectangular(300, 135, 600, 730, WHITE),
        Rectangular(325, 285, 550, 525, WHITE),
        Rectangular(355, 810 - numbers[0] * 5, 100, numbers[0] * 5, WHITE, color=BLUE),
        Rectangular(485, 810 - numbers[1] * 5, 100, numbers[1] * 5, WHITE, color=BLUE),
        Rectangular(615, 810 - numbers[2] * 5, 100, numbers[2] * 5, WHITE, color=BLUE),
        Rectangular(745, 810 - numbers[3] * 5, 100, numbers[3] * 5, WHITE, color=BLUE)
    ]

    for obj in objects:
        obj.draw(screen)

    audience_text(screen, 2, options[0], (390, 825))
    audience_text(screen, 2, options[1], (520, 825))
    audience_text(screen, 2, options[2], (650, 825))
    audience_text(screen, 2, options[3], (780, 825))

    audience_text(screen, 2, f"{str(numbers[0])}%", (390 - (count_digits(numbers[1]) + 1) * 3, 245))
    audience_text(screen, 2, f"{str(numbers[1])}%", (520 - (count_digits(numbers[1]) + 1) * 3, 245))
    audience_text(screen, 2, f"{str(numbers[2])}%", (650 - (count_digits(numbers[1]) + 1) * 3, 245))
    audience_text(screen, 2, f"{str(numbers[3])}%", (780 - (count_digits(numbers[1]) + 1) * 3, 245))

    screen.blit(ATA, (550, 150))

    pygame.display.update()

    for _ in range(0, 10000, 1000):
        pygame.time.delay(1000)
        pygame.event.pump()

def phone_screen(screen, text, correct_answer):
    screen.blit(PHONE, (0, 0))
    screen.blit(BUBBLE, (465,0))

    font = fonts[4]
    font2 = fonts[5]

    opening = font.render(text, True, BLACK)
    opening.set_alpha(127)

    answer = font2.render(f"{correct_answer}", True, RED)
    
    screen.blit(opening, (525, 80))
    screen.blit(answer, (680, 250))
    
    pygame.display.update()
    
    for _ in range(0, 15000, 1000):
        pygame.time.delay(1000)
        pygame.event.pump()