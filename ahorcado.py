import funciones
hanged_list = ["padel","programacion","wabi","tecnologia","python","java"]
choose_word = funciones.word_choose(hanged_list)
guess_word = funciones.generate_spaces(choose_word)
print(f"Estos seran los espacios a completar de la palabra: {guess_word}")
print("Tendras 10 intentos")
attempts = 10

while attempts != 0:
    attempts -= 1
    choose_letter = funciones.validation_letter()
    choose_letter = choose_letter.lower()
    guess_letter = funciones.letter_in_word(choose_letter,choose_word)

    if (guess_letter == True):
        guess_word = funciones.update_guess_word(choose_letter,choose_word,guess_word)
        print(f"La palabra con espacios actualizada queda asi: {guess_word}")
    else:
        if (attempts != 0):
            print(f"La letra no esta en la palabra te quedan {attempts} intentos")
        else:
            pass

    if (guess_word == choose_word):
        print("Te felicito has ganado!")
        break
    else:
        pass
if (guess_word != choose_word):
    print("Perdiste, te quedaste sin intentos")
    

