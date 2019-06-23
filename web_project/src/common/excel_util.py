# -*- coding:utf-8 -*-
from openpyxl import load_workbook
import pysnooper

class ParseExcel:
    def __init__(self, excel_path, sheet_name):
        # 加载Excel数据
        self.wb = load_workbook(excel_path)
        # 加载sheet_name工作表数据
        self.sheet = self.wb.get_sheet_by_name(sheet_name)
        # 获取sheet_name工作表中的最大行号
        self.max_row_num = self.sheet.rows

    @pysnooper.snoop()
    def getDataFromSheet(self):
        data_list = []
        # 去掉第一行标题
        for line in self.sheet.rows[1]:
            print(line[1].value)


if __name__ == '__main__':
    pe = ParseExcel("./ceshishuju.xlsx", "Sheet1")
    pe.getDataFromSheet()
