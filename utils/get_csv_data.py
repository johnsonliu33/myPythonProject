import csv


def get_csv_data(file_name, line):
    with open(file_name, 'r', encoding='utf-8-sig')as file:
        read = csv.reader(file)
        for row in enumerate(read, line):  # index为行号，row是该行内容.  # line表示读第几行数据
            return row


if __name__ == '__main__':
    csv_file = "../app_project/data/loginUser.csv"
    data = get_csv_data(csv_file, 3)
    print(data)
