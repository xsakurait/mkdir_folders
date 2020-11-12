#これを実行することで、フォルダにexcelに書いたフォルダ名を持つ複数のフォルダを作ることができる
import os
import csv

path = "読み込むexcelファイル名"   #excelファイルを読み込む

with open(path, encoding="cp932") as f:
    reader= csv.reader(f)
    for row in  reader:
        folder_name  = row[0] + '_' + row[1]
        if not os.path.exists( folder_name):
            os.mkdir( folder_name)
