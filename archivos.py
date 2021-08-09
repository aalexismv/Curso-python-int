def read():
    numbers = []
    with open("./archivos/numbers.txt", "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)

def write():
    names = ["Yaril", "Alexis", "Michelle", "Erik", "Salazar"]
    with open ("./archivos/names.txt", "w", encoding="utf-8") as f:
        for names in names:
            f.write(names)
            f.write("\n")




def run():
    write()


if __name__ == "__main__":
    run()
