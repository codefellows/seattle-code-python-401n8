# Don't do this:
# file = open("example.txt")
# content = file.read()
# print(content)
# print("is the file closed?", file.closed)
# file.close()
#
# print("is the file closed?", file.closed)


# Do this instead:
# use a 'with' statement! will open and close the file for us
with open("example.txt", "r") as file:
    content = file.read()
    print(content)


# def open_file(path, mode):
#     with open(path, mode) as file:
#         content = file.read()
#         print(content)
#
# open_file("example.txt", "r")


with open("example.txt", "w") as file:
    file.write("Hello Class!")


with open("example2.txt", "w") as file:
    file.write("new content")


try:
    with open("example3.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError as e:
    print(e)
