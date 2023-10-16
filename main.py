import os


def txt_input(file):
    with open(file, 'r', encoding='utf-8') as f:
        full_txt = f.read()

    ls = full_txt.split(' ')
    ls = remove_words(ls)
    # tuples = translate(ls)
    flashcard(ls,'flashcards.txt')


def remove_words(ls):
    with open(os.path.join('data', 'settings', 'ignored-words.txt'), 'r', encoding='utf-8') as ignored:
        rem = ignored.read()

    new_ls = []
    for word in ls:
        if not word.isalpha():  # remove numerals, blank lines, etc.
            continue
        elif word.lower() in rem:  # remove articles and other simple words
            continue
        elif word.lower() not in new_ls:  # remove repeats
            new_ls.append(word.lower())

    return new_ls


def translate(ls):
    pass


def flashcard(list_tuples, save_as):
    f = open(os.path.join('data', 'flashcards', save_as), "x", encoding="UTF-8")
    f.write("ES,EN\n")
    f.close()

    with open(os.path.join('data', 'flashcards', save_as), 'a', encoding="UTF-8") as f:
        for word in list_tuples:
            # f.write(f"{word[0]}, {word[1]}\n")
            f.write(f"{word}\n")


# main
txt_input(os.path.join('data', 'sample.txt'))
