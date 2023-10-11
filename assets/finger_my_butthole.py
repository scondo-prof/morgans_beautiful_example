from text_scrambler import Scrambler

src = Scrambler()


def scramble_my_eggs_baby(string_to_scramble):
    scrambled_eggs = src.scramble(string_to_scramble, level=4)
    return scrambled_eggs