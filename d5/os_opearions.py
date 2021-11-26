from os import listdir, chdir

print(listdir("."))     # listowanie zawartości aktualnego katalogu
chdir("files")          # zmiana katalogu
print(listdir("."))

for file in listdir("."):
    with open(file, "r", encoding="utf-8") as f:
        for line in f.readlines():
            print(line.strip())