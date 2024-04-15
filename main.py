import time

def introduction():
    print(
        "Добро пожаловать в подземелье! Ты отважился войти в темные глубины, "
        "где могут произойти ужасные вещи.")
    time.sleep(1)
    print("Твоя задача - дойти до конца подземелья, преодолевая препятствия на своем пути.")
    time.sleep(1)
    print("Выбирай свои действия осторожно, и помни, что каждое решение влияет на твое приключение!\n")

def make_choice(question, options):
    print(question)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

    while True:
        try:
            choice = int(input("Выбери номер действия: "))
            if 1 <= choice <= len(options):
                return choice
            else:
                print("Пожалуйста, введите число от 1 до", len(options))
        except ValueError:
            print("Пожалуйста, введите число.")


if __name__ == "__main__":
    dungeon_quest()