#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import xlrd  # 读取excel文件
import xlwt
import difflib
import time


def Similarity_match():  # 相似度匹配
    excle_A = xlrd.open_workbook('A.xls')  # 待填表
    table_A = excle_A.sheets()[1]  # 第几个表
    print(excle_A.sheets())
    row_A = table_A.nrows  # excel中有效行数
    col_A = table_A.ncols  # 获取列表的有效列数
    data_A = [[0 for i in range(col_A)] for i in range(row_A)]
    for i in range(row_A):
        for j in range(col_A):
            data_A[i][j] = table_A.cell(i, j).value

    excle_B = xlrd.open_workbook('B.xls')  # 模板表
    table_B = excle_B.sheets()[2]
    print(excle_B.sheets())
    row_B = table_B.nrows  # excel中有效行数
    col_B = table_B.ncols  # 获取列表的有效列数
    data_B = [[0 for i in range(col_B)] for i in range(row_B)]
    for i in range(row_B):
        for j in range(col_B):
            data_B[i][j] = table_B.cell(i, j).value

    excel_save = 'C.xls'  # 文件储存位置

    print(data_B[6][2])

    start = 6  # 从第几行开始
    ok_j = 0  # 匹配行
    time_start = time.time()

    for i in range(start, row_A):
        a = data_A[i][2]
        max_seq = 0  # 最大相似度
        for j in range(start, row_B):
            b = data_B[j][2]
            seq = difflib.SequenceMatcher(None, a, b).ratio()
            if seq > max_seq:
                data_A[i][5] = data_B[j][5]
                max_seq = seq
                ok_j = j
        print('A表'+str(i + 1) + '行与B表' + str(ok_j + 1) + '行相似度' + str(max_seq))

    time_end = time.time()
    print('运行时间', time_end - time_start)

    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('计算结果')  # 工作表名称
    for i in range(len(data_A)):
        for j in range(len(data_A[0])):
            worksheet.write(i, j, label=data_A[i][j])
    workbook.save(excel_save)


if __name__ == "__main__":
    Similarity_match()
