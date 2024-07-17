
def read_file_first_way():
    file = open("data.txt", mode="r")
    contents = file.read()
    print(contents)
    file.close()


def read_file_better_way():
    with open("data.txt") as file:
        contents = file.read()
        print(contents)


def white_file():
    with open("data.txt", mode="w") as file:
        file.write("Hi! I'm new text")


def add_at_file():
    with open("data.txt", mode="a") as file:
        file.write("\nHi! I'm new text")


def absolute_path():
    with open("/home/daleale/Desktop/external.txt", mode="r") as file:
        print(file.read())


# file deleted already
def relative_path():
    with open("../../../../../../../Desktop/external.txt", mode="r") as file:
        print(file.read())


def main():
    # read_file_first_way()
    # read_file_better_way()
    # white_file()
    # add_at_file()

    relative_path()


main()
