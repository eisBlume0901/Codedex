message = "Hello, there! I am sending you this secret message."

with open("messages.txt", "w") as file:
    pass

def write_to_file(message: str):
    with open("messages.txt", "a") as file:
        try:
            file.write(message + "\n")
        except IOError:
            print("There is an issue writing the file")
        finally:
            file.close()

write_to_file(message)

messages = [
    "Learning Intermediate Python at Codédex",
    "Learning how to code without AI",
    "Building fundamental skills rather than becoming a vibe coder"
]

for i in messages:
    write_to_file(i)

def read_file(filename: str):
    with open(filename, "r+", encoding="utf-8") as file:
        try:
            lines = file.readlines()
            for line in lines:
                print(line, end="")
        except FileNotFoundError:
            print("There is an issue reading the file")
        finally:
            file.close()

read_file("messages.txt")

# with open("messages.txt", "a") as file:
#     file.truncate(10)

