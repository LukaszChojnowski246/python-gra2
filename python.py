import random
import os
import time

def numguesser():
    PLAYING = 1

    zakres = int(input('Wprowadz do jakiej liczby chcesz zgadywac: '))
    
    losowa = random.randint(1,zakres)

    liczba_prob = 0 # Jesli 3 to przegrywa    
    while(PLAYING == 1):
        if liczba_prob < 3 :
            if liczba_prob < 2:
                print("Liczba")
            wybor = int(input("Zgandij liczbe: "))

            if wybor == random:
                print(f"Zgadłeś ukrytą liczbe! to liczba {losowa}")
                PLAYING = 0
            else:
                liczba_prob += 1
                print(f"Pozostało Ci prób {3-liczba_prob}")
        else:
            print("Nie udało Ci się zgadnąć")
            PLAYING = 0


def PKN():

    SCORE = 0

    while(True):

        xd = random.randint(0,2)

        opcje = ['kamień','papier','nożyce']
    
        komputer = opcje[xd]
    
        wybor = input('Co wyrzucasz? [kamień,papier,nożyce]: ')
    
        wybor_lower = wybor.lower()
    
        if wybor_lower == komputer:
            SCORE -= 1
            print('Remis! -1')
        elif wybor == 'kamień' and komputer == 'papier':
            SCORE = 0
            print(f'Przegrałeś! Tracisz wszystkie {SCORE} punkty')
        elif wybor =='papier' and komputer == 'nożyce':
            SCORE = 0
            print(f'Przegrałeś! Tracisz wszystkie {SCORE} punkty')
        elif wybor == 'nożyce' and komputer == 'kamień':
            SCORE = 0
            print(f'Przegrałeś! Tracisz wszystkie {SCORE} punkty')
        else:
            SCORE += 1
            print(f'Wygrałeś! Zyskujesz 1 punkt do puli {SCORE}')


def color_text(text, color = "RED"):
    """
    Takes text as string,  and color as string, returns colored text, can be used in terminal.
    """
    # BLUE = '\033[94m'
    # CYAN = '\033[96m'
    # GREEN = '\033[92m'
    # ORANGE = '\033[93m'
    # RED = '\033[91m'
    if color == "RED":
        return '\033[91m'+text+'\033[0m'

    elif color == 'ORANGE':
        return '\033[93m'+text+'\033[0m'

    elif color == 'GREEN':
        return '\033[92m'+text+'\033[0m'

    elif color == 'CYAN':
        return '\033[96m'+text+'\033[0m'

    elif color == 'BLUE':
        return '\033[94m'+text+'\033[0m'

print(color_text('xd', 'GREEN'))

WIDTH = 20
HEIGHT = 10

snake = [(5, 5), (5, 4), (5, 3)] # długość początkowa
direction = 'd' # start: w prawo

food = (random.randint(0, HEIGHT-1), random.randint(0, WIDTH-1))
super_food = (random.randint(0, round((HEIGHT-1)/2)), random.randint(0, round((WIDTH-1)/2)))

# render_board() lub render_board(100, 50)

def render_board(HEIGHT = HEIGHT, WIDTH = WIDTH):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if(y,x) == food:
                print(color_text("@"), end="")
            elif (x,y) in snake:
                print(color_text("#", "BLUE"))
            else:
                print("", end="")
        print()

wartosc_proc = (random.randint(1, 100))

def superfut(warotsc_proc, super_food, proc):
    if warotsc_proc >= proc:
        return(super_food)
    else:
        pass

def draw():
    os.system('cls' if os.name == 'nt' else 'clear')

    render_board()


while True:
    draw()
    print("Sterowanie: w/s/a/d + Enter")

    move = input("Ruch: ").lower()
    if move in ['w', 's', 'a', 'd']:
        direction = move

    head_y, head_x = snake[0]

    if direction == 'w':
        head_y += 1
    elif direction == 's':
        head_y -= 1
    elif direction == 'a':
        head_x += 1
    elif direction == 'd':
        head_x -= 1

    new_head = (head_y, head_x)


    if (
        head_x < 0 or head_x >= WIDTH or
        head_y < 0 or head_y >= HEIGHT or
        new_head in snake
    ):
        draw()
        print('GAME OVER!')
        break

snake.insert(0, new_head)

if new_head == food:
    food = (random.randint(0, HEIGHT-1), random.randint(0, WIDTH-1))
elif new_head == super_food:
    super_food = (random.randint())

else:
    snake.pop()

time.sleep(0.1)

















print("> fajnecos")
print("> Wybierz opcje")
print("1) Snake")
print("2) Numguesser")
print("3) PKN")
Snake = input("Opcja nr : ")
if Snake == '1':
    print(draw())
if Snake == '2':
    print(numguesser())
if Snake == '3':
    print(PKN())