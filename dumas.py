counter = 0
key = {}


with open("franklin.txt") as ft:
    for line in ft:
        stripped = line.strip()
        for ch in stripped:
            if ch != " ":
                counter += 1
                key[counter] = ch
            else:
                continue

while True:
    number = input("Code number: ")
    if number == "":
        break
    number = int(number)
    print(key[number])