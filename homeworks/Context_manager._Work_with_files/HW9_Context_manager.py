# TASK 1
# Створити логер який дозволяє працювати з файлами як звичайний open,
# але разом з тим в файл logs.txt записує:
# коли був відкритий файл, назва файла, коли закритий файл
# для інформації про час можемо використати datetime.now()
# приклад відпрацювання
# with my_custom_manager('file.txt', 'r') as f:
#     f.read()
# В файл буде записано
# 2022-07-11 22:17:59.782551 file.txt OPEN
# 2022-07-11 22:18:00.782551 file.txt CLOSE

from datetime import datetime as dt
from csv import writer, reader
from json import dump, load

class my_loger:
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.file = open(file_name, mode)
        with open("logs.txt", 'a') as self.log:
            self.log.write(f"{dt.now()} {self.file_name} OPEN\n")

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open("logs.txt", 'a') as self.log:
            self.log.write(f"{dt.now()} {self.file_name} CLOSE\n")
        self.file.close()


with my_loger("file1.txt", 'w') as file1:
    file1.write("Hello word")

# TASK 2
# Написати ф-цію яка переводить файл logs.txt в logs.csv
# Приклад такого файлу
# 2022-07-11 22:17:59.782551, file.txt, OPEN
# 2022-07-11 22:18:00.782551, file.txt, CLOSE


def txt2csv():
    with open("logs.txt", "r") as logs_txt:
        with open("logs.csv", "w") as logs_csv:
            write = writer(logs_csv, delimiter=',')
            for line in logs_txt:
                write.writerow([line[:25], line[26:36], line[36:-1]])


txt2csv()
with open("logs.csv", "r") as log:
    print(log.read())
# 2022-07-12 01:50:56.23462, file1.txt, OPEN
# 2022-07-12 01:50:56.23479, file1.txt, CLOSE
# 2022-07-12 01:50:57.90161, file1.txt, OPEN
# 2022-07-12 01:50:57.90175, file1.txt, CLOSE


# TASK 3 (з зірочкою)
# Написати ф-цію, яка обраховує з файла logs.csv скільки раз був відкритий файл і його остання дата відкриття.
# Цю інформацію записати в logs.json. Приклад:
# {
#     "file.txt": {
#         "count": 2,
#         "last_time_opened": "2022-07-11 22:17:59.782551"
#     }
# }
# P.S. Якщо щось не зрозуміло по умові задачі, то робіть як вважаєте за доцільно,
# користуючись здоровим глуздом звичайно ж)


def logs_json():
    with open("logs.csv", "r") as logs_csv:
        read = reader(logs_csv, delimiter=',')
        counrer = 0
        res = {"file.txt": {"count": 0, "last_time_opened": ""}}
        for i in read:
            if i[-1] == " OPEN":
                res["file.txt"]["count"] += 1
                res["file.txt"]["last_time_opened"] = i[0]
    with open("logs.json", "w") as logs_json:
        dump(res, logs_json, indent=4)
        
        
logs_json()
with open("logs.json", "r") as lj:
    print(load(lj))
# {'file.txt': {'count': 2, 'last_time_opened': '2022-07-12 01:44:54.92845'}}
