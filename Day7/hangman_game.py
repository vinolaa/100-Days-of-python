import random
from Modulos import hangman_words
from Modulos import hangman_stages

print(hangman_stages.logo)
chosen_word = random.choice(hangman_words.word_list)

life = 6
end_game = False
used_words = []
word_size = len(chosen_word)
display = []

for underscore in range(word_size):
    display.append("_")

print(hangman_stages.stages[life])
print(display)

while not end_game:
    guess = input("Chose a letter: ").lower()
    if guess not in used_words:
        used_words.append(guess)

        for char in range(word_size):
            if chosen_word[char] == guess:
                display[char] = guess

        if guess not in chosen_word:
            life -= 1
            print(hangman_stages.stages[life])
    else:
        print("You have already tried this letter. Please select another char!")

    print(display)
    if "_" not in display:
        end_game = True
        print("\n\nCongrats, you win =D")
    elif life == 0:
        end_game = True
        print("\n\nSorry, you lose:(")
