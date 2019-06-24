# -*- cocoding:utf-8 -*-
from openpyxl import load_workbook

class OpenpyxlUtil:
    def __init__(self, excel_path, sheet_name):
        # 加载Excel数据
        # self.wb=openpyxl.Workbook(excel_path) PS：Workbook和load_workbook相同，返回的都是一个Workbook对象。
        self.wb = load_workbook(excel_path)
        # 获取所有的sheet
        print(self.wb.sheetnames)
        # 获取当前活跃工作簿
        print(self.wb.active)
        #判断是否以只读模式打开Excel
        # 加载sheet_name工作表数据
        self.sheet = self.wb[sheet_name]
        # 获取sheet_name工作表中的最大行号
        self.row_num = self.sheet.max_row
    def getDataFromSheet(self):
        data_list = []
        # 去掉第一行标题
        for row in range(2, self.row_num + 1):
            temp_list = []
            temp_list.append(self.sheet.cell(row, 2).value)
            temp_list.append(self.sheet.cell(row, 3).value)
            data_list.append(temp_list)
        return data_list


if __name__ == '__main__':
    ou = OpenpyxlUtil("./ceshishuju.xlsx", "Sheet1")
    d_list = ou.getDataFromSheet()
    for data in d_list:
        print(data)