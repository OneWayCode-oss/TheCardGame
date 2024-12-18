import pygame   
import random  
import sys  
import textwrap



cardsit = [                                     
    "КОРОЛЬ ПИК", "ДАМА ПИК", "ВАЛЕТ ПИК", 
    "КОРОЛЬ ТРЕФ", "ДАМА ТРЕФ", "ВАЛЕТ ТРЕФ",
    "КОРОЛЬ БУБЕН", "ДАМА БУБЕН", "ВАЛЕТ БУБЕН", 
    "КОРОЛЬ ЧЕРВЕЙ", "ДАМА ЧЕРВЕЙ", "ВАЛЕТ ЧЕРВЕЙ"          #создание рандомных карт для выбора
]

cardsit1 = random.choice(cardsit)

cardsit2 = random.choice(cardsit)

formula = pygame.image.load("formula.jpg")
formula = pygame.transform.scale(formula, (600, 300))



backimage = pygame.image.load("images.jpg")                       
backimage = pygame.transform.scale(backimage, (1920, 1080))
                                                                    #картинки для заднего фона и карты
card_image = pygame.image.load("card.jpg")
card_image = pygame.transform.scale(card_image, (100, 150))

# Инициализация Pygame  
pygame.init()  

# Константы  
WIDTH, HEIGHT = 1920, 1080  
CARD_WIDTH, CARD_HEIGHT = 100, 150  
FPS = 60  

# Цвета  
WHITE = (255, 255, 255)  
BLACK = (0, 0, 0)  
GREEN = (0, 255, 0)  
RED = (255, 0, 0)  
BLUE = (66, 135, 245)
PURPLE = (142, 4, 201)
LIGHT_GREEN = (2, 250, 40)

# Переменные для анимации переворота
flipped_cards = []
flip_animation = False
flip_card_index = -1
flip_progress = 0  # Прогресс анимации



# Создание окна  
screen = pygame.display.set_mode((WIDTH, HEIGHT))  
pygame.display.set_caption("Вытягивание карточек")  

# Шрифт  
font = pygame.font.Font(None, 60)  

# Функция для отображения текста  
def draw_text(text, color, x, y):  
    text_surface = font.render(text, True, color)  
    screen.blit(text_surface, (x, y))  


def flip_card(index):
    global flip_animation, flip_card_index, flip_progress
    flip_animation = True
    flip_card_index = index
    flip_progress = 0

def outro_animation():
    screen.blit(backimage, (0, 0))  # Отображаем фон
    draw_text("Поздравляем! Вы нашли нужную карту!", GREEN, WIDTH // 2 - 250, HEIGHT // 2 - 50)
    draw_text("Нажмите 'N', чтобы начать игру заново.", WHITE, WIDTH // 2 - 250, HEIGHT // 2 + 50)
    draw_text("Формула для нахождения вероятности:", PURPLE, WIDTH // 2 - 900, HEIGHT // 2 + -500)
    screen.blit(formula, (WIDTH // 2 - 900, HEIGHT // 2 - 420))
    pygame.display.flip()  # Обновляем экран

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Нажатие 'R' для выхода
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_n:  # Нажатие 'N' для новой игры
                    waiting = False  # Выход из цикла ожидания
                    main()  # Запускаем игру заново


def update_flip_animation():
    global flip_animation, flip_progress
    if flip_animation:
        flip_progress += 1
        if flip_progress >= 10:
            flip_animation = False

# Функция для создания колоды карточек  
def create_deck(num_cards, target_card):  
    # Создаем колоду с уникальными картами  
    cards = [f"" for i in range(num_cards - 0)]  
    cards.append(target_card)  # Добавляем целевую карту  
    random.shuffle(cards)  # Перемешиваем колоду  
    return cards  

# Функция для отображения карточек  
def draw_cards(selected_card=None):  
    screen.blit(backimage, (0, 0))  
    for i, card in enumerate(cards):  
        x = (i % 6) * (CARD_WIDTH + 10) + 50  
        y = (i // 6) * (CARD_HEIGHT + 10) + 50  
        if card == selected_card:
            pygame.draw.rect(screen, GREEN, (x, y, CARD_WIDTH, CARD_HEIGHT))
        else:
            pygame.draw.rect(screen, BLACK, (x, y, CARD_WIDTH, CARD_HEIGHT))

        screen.blit(card_image, (x + 0, y + 0))



        #draw_text(card, WHITE, x + 10, y + 10)  
    draw_text("Нажмите на карточку, чтобы выбрать ее", BLACK, 1000, HEIGHT - 300)  
     
    if message:  
        draw_text(message, GREEN, WIDTH // 2 - 240, HEIGHT - 400) 

    if flip_animation and flip_card_index == i:
        pygame.draw.rect(screen, WHITE, (x, y, CARD_WIDTH, CARD_HEIGHT))
        draw_text(card, WHITE, x + 10, y + 10)
    else:
        pygame.draw.rect(screen, BLACK, (x, y, CARD_WIDTH, CARD_HEIGHT))
        screen.blit(card_image, (x + 0, y + 0))

    update_flip_animation()
    pygame.display.flip()  

# Вступительная анимация  
def draw_multiline_text(text, color, x, y, max_width):
    """Функция для отображения многострочного текста."""
    lines = textwrap.fill(text, width=max_width)  # Разбиваем текст на строки
    for line in lines.splitlines():
        draw_text(line, color, x, y)  # Отображаем каждую строку
        y += font.get_height()  # Увеличиваем y для следующей строки

def intro_animation():  
    screen.blit(backimage, (0, 0))  
    draw_text(f"Ваша карта - '{cardsit1}'.", LIGHT_GREEN, WIDTH // 2 - 275, HEIGHT // 2 - -10)  
    draw_text(f"Что-бы продолжить - нажмите ЛЮБУЮ кнопку.", PURPLE, WIDTH // 2 - 500, HEIGHT // 2 - -250)
    draw_text(f"ПРАВИЛА:", BLACK, WIDTH // 2 - 150, HEIGHT // 2 - 350)
    
    # Используем новую функцию для многострочного текста
    long_text = "Дорогой друг, добро пожаловать в игру 'узнай вероятность' , чтобы её пройти тебе нужно нажать на нужную карту выбранную случайным образом и открыть для себя формулу вероятности ,не бойся ошибаться ведь в конце тебе будет показана нужная формула"
    draw_multiline_text(long_text, BLACK, WIDTH // 2 - 500, HEIGHT // 2 + -300, max_width=50)  # max_width - максимальная ширина строки в символах

    pygame.display.flip() 
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                waiting = False

        pygame.time.Clock().tick(FPS)
                

# Функция для текстового ввода  
def get_input(prompt):  
    input_box = pygame.Rect(800, 500, 200, 50)  
    color_inactive = pygame.Color('lightskyblue3')  
    color_active = pygame.Color('dodgerblue2')  
    color = color_inactive  
    active = False  
    text = ''  
    done = False  
    

    while not done:  
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:  
                pygame.quit()  
                sys.exit()  
            if event.type == pygame.MOUSEBUTTONDOWN:  
                if input_box.collidepoint(event.pos):  
                    active = not active  
                else:  
                    active = False  
                color = color_active if active else color_inactive  
            if event.type == pygame.KEYDOWN:  
                if active:  
                    if event.key == pygame.K_RETURN:  
                        done = True  
                    elif event.key == pygame.K_BACKSPACE:  
                        text = text[:-1]  
                    else:  
                        text += event.unicode  

        screen.blit(backimage, (0, 0))  
        draw_text(prompt, BLACK, 800, 450)  
        txt_surface = font.render(text, True, color)  
        width = max(200, txt_surface.get_width()+10)  
        input_box.w = width  
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))  
        pygame.draw.rect(screen, color, input_box, 2)  

        pygame.display.flip()  
        pygame.time.Clock().tick(FPS)  

    return text  

# Основной игровой цикл  
def main():  
    global cards, target_card, message  
    intro_animation()  
    
    # Получаем количество карт от пользователя  
    num_cards_str = get_input("Введите количество карт: ")  
    num_cards = int(num_cards_str) if num_cards_str.isdigit() else 5  # Устанавливаем значение по умолчанию  

    # Выбираем целевую карту  
    target_card = f"{random.randint(0, num_cards)}"  # Генерируем целевую карту  
    cards = create_deck(num_cards, target_card)  # Создаем колоду карточек  
    message = f"Ваша задача, найти загаданную карту - это {cardsit1}!"  

    clock = pygame.time.Clock()  
    while True:  
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:  
                pygame.quit()  
                sys.exit()  
            elif event.type == pygame.MOUSEBUTTONDOWN:  
                mouse_x, mouse_y = event.pos  
                for i, card in enumerate(cards):  
                    x = (i % 6) * (CARD_WIDTH + 10) + 50  
                    y = (i // 6) * (CARD_HEIGHT + 10) + 50  
                    if x < mouse_x < x + CARD_WIDTH and y < mouse_y < y + CARD_HEIGHT:  
                        selected_card = card  
                        flip_card(i)
                        if selected_card == target_card:  
                            outro_animation()
                            
                            
                        else:  
                            message = f"Попробуйте снова! Вы вытянули не ту карту."  
            elif event.type == pygame.KEYDOWN:  
                if event.key == pygame.K_n:  # Нажатие 'N' для новой игры  
                    num_cards_str = get_input("Введите количество карт: ")  
                    num_cards = int(num_cards_str) if num_cards_str.isdigit() else 5  
                    target_card = f" {random.randint(0, num_cards)}"  
                    cards = create_deck(num_cards, target_card)  
                    message = ""  
                    


        draw_cards()  

        clock.tick(FPS)  

if __name__ == "__main__":  
    main()

    


    