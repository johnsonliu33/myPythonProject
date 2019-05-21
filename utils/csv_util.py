import csv


def get_csv_data(file_name, line):
    with open(file_name, 'r', encoding='utf-8-sig')as file:
        read = csv.reader(file)
        for index, row in enumerate(read):  # index为行号 # row是该行内容.  # enumerate(read,star=10)表示坐标从10开始计数,默认index从0开始
            if index == line:
                return row


def insert_csv_data(file_name, data_list):
    with open(file_name, "a", newline="") as file:
        csv_write = csv.writer(file, dialect="excle")
        for i in range(len(data_list)):
            csv_write.write(data_list[i])


if __name__ == '__main__':
    csv_file = "../app_project/src/data/loginUser.csv"
    data = get_csv_data(csv_file, 1)
    print(data)
    user1 = []
