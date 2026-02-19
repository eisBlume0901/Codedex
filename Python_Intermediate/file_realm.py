# Write code below 💖

liked_songs = {
    "A Million Miles Away": "Kaho Nakamura",
    "WORK": "millenium parade and Sheena Ringo",
    "world.execute(me)": "Mili",
    "One Last Kiss": "Hikaru Utada",
    "Be a flower": "Ryokuoushoku Shakai",
    "Again": "Yui"
}


def write_liked_songs_to_file(liked_songs, file_name):
    with open("songs.txt", "w") as file:
        try:
            file.write("Liked Songs:\n")
            for title, artist in liked_songs.items():
                file.write(f"{title} by {artist}\n")
            print(f"Successfully added songs to {file_name}")
        except IOError:
            print("Songs not added to file because the file is not found")
        finally:
            file.close()


write_liked_songs_to_file(liked_songs, "songs.txt")

file = open("songs.txt", "r")
lines = file.readlines()

for line in lines:
    print(line, end="")

