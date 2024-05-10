
def new_file():
    my_file = open("task_1_file.txt", "w+")
    my_file.write("Hello World\n")
    my_file.seek(0)
    print(my_file.read())
    my_file.close()


new_file()


def new_line():
    my_file = open("task_1_file.txt", "a+", encoding="utf-8")
    my_file.write("Who's the more foolish: the fool, or the fool who follows him? - Obi-Wan Kenobi")
    my_file.seek(0)
    for line in my_file.readlines():
        print(line, end="")
    print()
    my_file.close()


new_line()


def letter_count(letter):
    my_file = open("task_1_file.txt", "r+", encoding="utf-8")
    counter = 0
    for i in my_file.read():
        if i.lower() == letter.lower():
            counter += 1
    if letter == " ":
        print(f"There a re {counter + 1} words in the file")
    else:
        print(f"There are {counter} {letter}'s in the file")
    my_file.close()


letter_count("w")


def drawing():
    draw_file = open("drawing.txt", "w+")
    for i in range(10):
        j = 0
        while j < 10:
            for k in range(j):
                draw_file.write("-")
            draw_file.write("  ")
            for k in range(10 - j):
                draw_file.write("-")
            draw_file.write("\n")
            j += 1
        while j > 0:
            for k in range(j):
                draw_file.write("-")
            draw_file.write("  ")
            for k in range(10 - j):
                draw_file.write("-")
            draw_file.write("\n")
            j -= 1
    draw_file.seek(0)
    print(draw_file.read())


drawing()
