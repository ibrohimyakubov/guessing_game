import random

GAME_OVER = ValueError


def random_number():
    return random.randint(1, 10)


def check_number(number, user):
    message = "Men o'ylagan son "
    if number < user:
        return f"Men o'ylagan son {user} dan kichikroq"
    elif number > user:
        return f"Men o'ylagan son {user} dan kattaroq"
    raise GAME_OVER


def main():
    number = random_number()
    print(f"Men 1-10 sonlar oralig'ida bir son o'yladim {number}")

    for guess in range(1, 4):
        user = int(input(f"{guess} - tahminingizni kiriting: "))
        try:
            message = check_number(number, user)
            print(message)
        except GAME_OVER:
            print(f"Siz o'yinni yutdingiz! ☑️")
            try_again = input("Yana o'ynashni istaysizmi ?: ")
            print(try_again)

            if try_again == "ha":
                return main()
            elif try_again == "yo'q":
                return None
    else:
        print('')
        print(f"Siz yutqazdingiz, men o'ylagan son - {number} edi!")

    try_again = str(input("Yana o'ynashni istaysizmi ?: "))
    print(try_again)

    if try_again == "ha":
        return main()
    elif try_again == "yo'q":
        return None

if __name__ == '__main__':
    main()
