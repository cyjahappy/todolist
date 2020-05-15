from tkinter import ttk
from tkinter import *

root = Tk()  # 初始框的声明
todoList = []
statusList = []

columns = ("任务内容", "状态")
treeview = ttk.Treeview(root, height=18, show="headings", columns=columns)  # 表格

treeview.column("任务内容", width=300, anchor='center')  # 表示列,不显示
treeview.column("状态", width=100, anchor='center')

treeview.heading("任务内容", text="任务内容")  # 显示表头
treeview.heading("状态", text="状态")

treeview.pack(side=LEFT, fill=BOTH)

file = open('list.txt', 'r')

try:
    text_lines = file.readlines()
    for line in text_lines:
        # 任务内容
        todoList.append(line.split(',')[0])
        # 是否完成
        statusList.append(line.split(',')[-1])
finally:
    file.close()

for i in range(min(len(todoList), len(statusList))):  # 写入数据
    treeview.insert('', i, values=(todoList[i], statusList[i]))

def treeviewClick(event):  # 单击
    for item in treeview.selection():
        item_text = treeview.item(item, "values")
        print(item_text[2])

root.mainloop()  # 进入消息循环
