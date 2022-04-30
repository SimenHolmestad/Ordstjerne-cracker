import click
import time
import pyautogui
from tqdm import tqdm


def word_consist_only_of_chars(word, chars):
    for char in word:
        if char not in chars:
            return False
    return True


def get_all_possible_words(main_char, available_chars, words_to_check):
    possible_words = []

    for word in tqdm(words_to_check):
        if len(word) < 4:
            continue
        if main_char not in word:
            continue
        if not word_consist_only_of_chars(word, available_chars):
            continue
        possible_words.append(word)

    return possible_words


def convert_norwegian_word_to_english_keyboard_codes(word):
    """This is required for Pyautogui to write the letters correctly"""
    word = word.replace("ø", ";")
    word = word.replace("æ", "'")
    word = word.replace("å", "[")
    return word


def write_words_using_keyboard(possible_words):
    for word in possible_words:
        word = convert_norwegian_word_to_english_keyboard_codes(word)
        pyautogui.write(word)
        time.sleep(0.2)
        pyautogui.press('enter')
        time.sleep(2)


@click.command()
@click.argument("available_chars", type=str)
@click.argument("main_char", type=str)
def main(available_chars, main_char):
    assert len(available_chars) == 7, "Ordstjernen har 7 mulige bokstaver"
    assert len(main_char) == 1, "Det skal bare være 1 hovedbokstav"

    with open("nsf2021.txt", "r") as f:
        scrabble_words = [line.strip() for line in f.readlines()]

    available_chars = [char for char in available_chars]
    possible_words = get_all_possible_words(main_char, available_chars, scrabble_words)

    print("----------------------------------------------------")
    print(f"Fant {len(possible_words)} ord. Disse er:")
    for word in possible_words:
        print(word)
    print("----------------------------------------------------")

    print("Trykk på skrivefeltet i Ordstjernen!!!")
    print("Du har 5 sekunder: ", end="", flush=True)
    for second in range(5):
        time.sleep(1)
        print(str(5 - second), end="...", flush=True)

    write_words_using_keyboard(possible_words)


if __name__ == '__main__':
    main()
