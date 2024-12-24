import random
from words import film_listesi ,renk_listesi ,marka_listesi ,isim_listesi

hangman_art = {
    0: ("    -----   ",
        "    |       ",
        "    |       ",
        "    |       "),
    1: ("    -----   ",
        "    |   o   ",
        "    |       ",
        "    |       "),
    2: ("    -----   ",
        "    |   o   ",
        "    |   |   ",
        "    |       "),
    3: ("    -----   ",
        "    |   o   ",
        "    |  /|   ",
        "    |       "),
    4: ("    -----   ",
        "    |   o   ",
        "    |  /|\\  ",
        "    |       "),
    5: ("    -----   ",
        "    |   o   ",
        "    |  /|\\  ",
        "    |  /    "),
    6: ("    -----   ",
        "    |   o   ",
        "    |  /|\\  ",
        "    |  / \\  "),
}


def select_word(category):
    if category == "film":
        return random.choice(film_listesi)
    elif category == "color":
        return random.choice(renk_listesi)
    elif category == "brand":
        return random.choice(marka_listesi)
    elif category == "name":
        return random.choice(isim_listesi)
    elif category == "hard":
        all_words = film_listesi + renk_listesi + marka_listesi + isim_listesi
        return random.choice(all_words)
    else:
        return None

def main():
    print("Categories:")
    print("1. Film")
    print("2. Color")
    print("3. Brand")
    print("4. Name")
    print("5. Hard (No category specified)")

    category_choice = input("Select a category (film/color/brand/name/hard): ").lower()

    answer = select_word(category_choice)
    if not answer:
        print("Invalid selection! Please restart the game.")
        return

    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    MAX_WRONG_GUESSES = 6
    is_running = True

    while is_running:
        print("**********")
        print("\n".join(["  ".join(hint)]))
        print("**********")
        print("\n".join(hangman_art[wrong_guesses]))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please enter a letter.")
            continue

        if guess in guessed_letters:
            print(f"You've already guessed the letter {guess}.")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1
            print(f"Wrong guess! Remaining attempts: {MAX_WRONG_GUESSES - wrong_guesses}")

        if "_" not in hint:
            print("CONGRATULATIONS! You won!")
            print(f"The answer was: {answer}")
            is_running = False
        elif wrong_guesses >= MAX_WRONG_GUESSES:
            print("GAME OVER! You lost.")
            print(f"The answer was: {answer}")
            is_running = False

if __name__ == "__main__":
    main()
