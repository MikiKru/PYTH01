from os import chdir


def read_files_and_write_all_content(file1, file2, file):
    with open(file1, mode = 'r', encoding="utf-8") as f1, open(file2, mode = 'r', encoding="utf-8") as f2:
        f1_content = f1.readlines()
        f2_content = f2.readlines()
    with open(file, mode = 'w') as f:
        f.writelines(f1_content)
        f.writelines("\n")
        f.writelines(f2_content)

def read_file(file):
    with open(file, mode='r') as f:
        for line in f.readlines():
            print(line.strip())


read_files_and_write_all_content(r'C:\Users\Student\PycharmProjects\PYTH01\d5\exercises\ex_7_1\w1.txt',
                                 r'C:\Users\Student\PycharmProjects\PYTH01\d5\exercises\ex_7_1\w2.txt',
                                 "file.txt")

read_file("file.txt")
