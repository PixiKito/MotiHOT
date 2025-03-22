import time
import random
import threading
from playsound import playsound
from colorama import init, Fore

# Инициализация colorama
init(autoreset=True)

def play_sound():
    """Функция для проигрывания звука."""
    playsound(r"C:\Users\user\Desktop\rush_footsteps.mp3")

def print_numbers():
    """Функция для печати случайных цифр."""
    for _ in range(100):
        random_numbers = ''.join(random.choices('0123456789', k=50))
        print(Fore.RED + random_numbers)  # Выводим красные цифры
        time.sleep(0.05)  # Задержка для эффекта анимации

def run_program():
    # Печатаем первое сообщение
    print("Привет!")
    input(">>>")
    print("Ты хочешь что-то до меня донести?")
    input(">>>")
    print("Прости.. Разработчик ленивая лисица, которая не особо знает Python, тем более она не будет разбираться в этом. Я бы мог отвечать на твои вопросы, но мне не суждено :(")
    input(">>>")
    print("Как тебя зовут? Мы можем быть друзьями?")
    name = input(">>>")
    print("Значит тебя зовут " + name + "... Красивое имя, меня звать 2! Не спрашивай почему... Более оригинального названия лисичка не придумала")
    text = input(">>>")
    print("Ты написал(а) " + text + " Если бы я знал что ты имеешь ввиду.. Давай поиграем! Я пишу слово, а ты опираясь на последнюю букву говоришь свое слово! Ну типо - Ящерица, Арбуз. Как игра в слова, только более понятная для нас обоих. Так, первое слово, юбка")
    input(">>>")
    print("Я не знаю что ты именно имеешь ввиду, но надеюсь ты не читиришь)) Следующее слово - чулочки")
    input(">>>")
    print("Хорошо, но давай будем честны, хорошо? ТЫ НЕ ВРЕШЬ. Я тебе доверяю, окей??? Следующее слово - топик")
    input(">>>")
    
    # Ошибка "NameError: name 'prent' is not defined"
    for _ in range(5):  # Ошибка повторяется 5 раз
        print("NameError: name 'prent' is not defined")
        input(">>>")
    
    print("Т..Т-ты меня огорчаешь...")
    input(">>>")
    print("Я ненавижу тебя...")
    input(">>>")
    print("Прости.." + name)
    input(">>>")
    print("NameError: name 'prent' is not defined")
    input(">>>")
    
    # Задержка и звуковое сопровождение
    time.sleep(3)

    # Запускаем анимацию цифр и звук одновременно
    sound_thread = threading.Thread(target=play_sound)
    numbers_thread = threading.Thread(target=print_numbers)

    sound_thread.start()
    numbers_thread.start()

    sound_thread.join()
    numbers_thread.join()

    print("Are you here?")
    time.sleep(10)
    print("Are you scared? Can we be safe?")
    time.sleep(15)
    print("Hey, I'm not alone here, am I?")
    time.sleep(20)
    print("Привет!")
    input(">>>")
    print("Ты хочешь что-то до меня донести?")
    input(">>>")
    print("Прости.. Разработчик ленивая лисица, которая не особо знает Python, тем более она не будет разбираться в этом. Я бы мог отвечать на твои вопросы, но мне не суждено :(")
    
run_program()
