# -*- coding:utf-8 -*-
import os
import xlrd
import xlwt
from xlutils import copy
"""xlrd和xlwt处理的是xls文件，单个sheet最大行数是65535，如果有更大需要的，建议使用openpyxl函数，最大行数达到1048576"""


def write_excel(filename,data):
    """创建/写入Excel"""
    workbook = xlwt.Workbook(encoding='utf-8')  # 创建一个Excel
    sheet = workbook.add_sheet('Sheet1')  # 在其中创建一个名为Sheet1的sheet
    # 设置字体
    font = xlwt.Font()  # 为样式创建字体
    font.colour_index = 0
    # 设置单元格样式
    style = xlwt.XFStyle()  # 初始化样式
    style.font = font  # 设定样式
    for row in range(len(data)):
        for cell in range(len(data[row])):
            sheet.write(row, cell, data[row][cell], style)  # 往sheet里第i行第j列写入数据
    workbook.save(filename)


def read_excel(file_name):
    """读取Excel"""
    data_list = []
    if os.path.exists(file_name):
        workbook = xlrd.open_workbook(file_name)
        # sheet=workbook.sheet_by_name("Sheet1") #读取名字是Sheet1的工作表
        sheet = workbook.sheet_by_index(0)  # 读取第一个工作表
        cell_00 = sheet.cell_value(0, 0)  # 读取第1行第1列数据
        print(cell_00)
        rows = sheet.nrows  # 获取总行数
        for i in range(rows):
            value = sheet.row_values(i)
            data_list.append(value)
    return data_list


def update_excel(file_name, data):
    """修改/新增Excel"""
    if not os.path.exists(file_name):
        workbook = xlwt.Workbook(encoding='utf-8')
        workbook.add_sheet('Sheet1')
        workbook.save("excel_file.xlsx")
    workbook = xlrd.open_workbook(file_name, formatting_info=True)
    # formatting_info=True: 保留原数据格式
    new_wb = copy.copy(workbook)
    sheet = new_wb.get_sheet(0)
    old_sheet = workbook.sheet_by_index(0)
    old_rows = old_sheet.nrows
    for i in range(len(data)):
        for j in range(len(data[i])):
            sheet.write(old_rows + i, j, data[i][j])
    new_wb.save(file_name)


if __name__ == '__main__':
    data = [["初一", "初二", "初三"], ["高一", "高二", "高三"], ["六年级", "七年级",
                                                     "八年级", "九年级"], ("2019-07-23 08:00:00", "2019/07/23 08:00:00")]
    write_excel(data)
    filename = "excel_file.xlsx"
    update_excel(filename, data)
    datas = read_excel(filename)
    for temp in datas:
        print(temp)
