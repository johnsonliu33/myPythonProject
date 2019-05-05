from copy import copy

import pymysql

import xlrd
import xlwt
from  xlrd import open_workbook
from xlutils.copy import copy


def write_data(data):
    k = 0
    rexcel = open_workbook("abcde.xls")  #
    rows = rexcel.sheets()[0].nrows
    excel = copy(rexcel)  # 用xlutils提供的copy方法将xlrd的对象转化为xlwt的对象
    table = excel.get_sheet(0)
    for i in range(len(data)):
        k += 1
        print("==", k, "===")
        print(data)
        table.write(rows, i, data[i])
    excel.save("abcde.xls")


def select_mysql(sql_str):
    conn = pymysql.connect(host="192.168.20.156", port=3306, user="test_user", passwd="test_user!@#123", db="mmall")
    cursor = conn.cursor()
    try:
        cont = cursor.execute(sql_str)
        if cont <= 0:
            return "*** SQL ERROR ***"
        res = cursor.fetchall()
        return res
    except:
        print("  Error: unable to fecth data")
    finally:
        cursor.close()
        conn.close()


def get_segment_info(parent_id, text_book_data):
    print(text_book_data)
    segment_data = ()
    sql_txt = "SELECT id, segmentname, parentid, textbookid, type, childorder, keypoint, plantime from  W_SegmentInfo WHERE parentid = '%s'"

    sql_two = sql_txt % parent_id

    data_two = select_mysql(sql_two)
    if len(data_two) > 0:
        for segment_one in data_two:
            segment_o = (segment_one[1], segment_one[5], segment_one[6], segment_one[7])
            segment_data1 = text_book_data + segment_o
            if segment_one[4] == 0:
                parent_id = segment_one[0]

                sql_two = sql_txt % parent_id
                data_three = select_mysql(sql_two)
                if len(data_three) > 0:
                    for segment_two in data_three:
                        segment_t = (segment_two[1], segment_two[5], segment_two[6], segment_two[7])
                        segment_data2 = segment_data1 + segment_t
                        if segment_two[4] == 0:
                            parent_id = segment_two[0]

                            sql_two = sql_txt % parent_id
                            data_four = select_mysql(sql_two)
                            if len(data_four) > 0:
                                for segment_three in data_four:
                                    segment_f = (segment_three[1], segment_three[5], segment_three[6], segment_three[7])
                                    segment_data = segment_data2 + segment_f

                                    write_data(segment_data)


def get_text_book():
    sql_one = "SELECT id, subject, term, pubshort, grades  FROM W_TextBookInfo WHERE studyyear = '2018-2019' AND standard = '2' GROUP BY subjectid, term"
    data_one = select_mysql(sql_one)
    for text_book_one in data_one:
        parent_ids = text_book_one[0]
        text_book_data = (text_book_one[1], text_book_one[2], text_book_one[3], text_book_one[4])
        get_segment_info(parent_ids, text_book_data)


if __name__ == "__main__":
    get_text_book()
