def read_files(file_name1, file_name2):
    with open(file_name1, mode='r') as f1:
        for line in f1.readlines():
            print(line.strip())
    with open(file_name2, mode='r') as f2:
        for line in f2.readlines():
            print(line.strip())

def read_files2(file_name1, file_name2):
    with open(file_name1, mode='r', encoding="utf-8") as f1, open(file_name2, mode='r', encoding="utf-8") as f2:
        f1_content = f1.readlines()
        f2_content = f2.readlines()
        if len(f1_content) > len(f2_content):
            longer = f1_content
            smaller = f2_content
        else:
            longer = f2_content
            smaller = f1_content
        for index, value in enumerate(longer):
            print(longer[index].strip())
            if index < len(smaller):
                print(smaller[index].strip())

# read_files("w1.txt", "w2.txt")
read_files2("w1.txt", "w2.txt")