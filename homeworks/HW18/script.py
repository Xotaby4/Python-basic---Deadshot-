'''Написати скрипт який дозволяє:
1. При виклику python script.py -c – рахує скільки файлів знаходиться всередині неї
2. При виклику python script.py --last або python script.py -l – виводить назву останнього файла
3. При виклику python script.py -c -d “/home/olmaks” – рахує к-сть файлів за шляхом (в мене це для
прикладу /home/olmaks у вас може бути C:/Program Files)
P.S.
Якщо щось не дуже зрозуміло робите на свій погляд)'''
import os, argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--count', action='store_true', help='count the number of files in a directory')
    parser.add_argument('-l', '--last', action='store_true', help='print the name of the last file')
    parser.add_argument('-d', '--path', type=str, help='path to the directory')
    args = parser.parse_args()
    if args.path:
        path = args.path
    else:
        path = os.getcwd()
    file_l = list_file(path)
    if args.count:
        print(len(file_l))
    if args.last:
        print(file_l[-1])

def list_file(path):
    file_list = []
    with os.scandir(path) as listOfEntries:
        for entry in listOfEntries:
            if entry.is_file():
                file_list.append(entry.name)
        return file_list

if __name__ == '__main__':
    main()
