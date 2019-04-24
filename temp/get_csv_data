import csv


def get_csv_data(file_name, line):
    with open(file_name, 'r', encoding='utf-8-sig')as file:
        read = csv.reader(file)
        for index, row in enumerate(read, 1):
            if index == line:
                return row


if __name__ == '__main__':
    csv_file = "../data/loginUser.csv"
    data = get_csv_data(csv_file, 3)
    print(data)
