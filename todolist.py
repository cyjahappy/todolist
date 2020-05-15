from tkinter import ttk
from tkinter import *

root = Tk()  # 初始框的声明
root.title('任务清单')

# 滚动条
sb = Scrollbar(root)
sb.pack(side=RIGHT, fill=Y)

todoList = []
statusList = []
columns = ("任务内容", "状态")

treeview = ttk.Treeview(root, height=18, show="headings", columns=columns)  # 表格
treeview.column("任务内容", width=300, anchor='center')  # 表示列,不显示
treeview.column("状态", width=100, anchor='center')
treeview.heading("任务内容", text="任务内容")  # 显示表头
treeview.heading("状态", text="状态")
treeview['yscrollcommand'] = sb.set
treeview.pack(side=LEFT, fill=BOTH)
sb['command'] = treeview.yview

file = open('list.txt', 'r', encoding='utf-8')
text_lines = file.readlines()
for line in text_lines:
    # 任务内容
    todoList.append(line.split('，')[0])
    # 是否完成
    statusList.append(line.split('，')[-1])
file.close()

for i in range(min(len(todoList), len(statusList))):  # 写入数据
    treeview.insert('', i, values=(todoList[i], statusList[i]))


def set_finish(event):
    for item in treeview.selection():
        item_text = treeview.item(item, "values")
    row = treeview.identify_row(event.y)  # 行

    if item_text[1].strip() == '完成':
        treeview.set(item, column='#2', value='未完成')
        int_row = int(row.split('I')[-1])
        text_lines[int_row - 1] = text_lines[int_row - 1].split('，')[0] + '，未完成\n'
        file.close()
        f = open('list.txt', 'w+', encoding='utf-8')
        f.writelines(text_lines)
        f.close()
    if item_text[1].strip() == '未完成':
        treeview.set(item, column='#2', value='完成')
        int_row = int(row.split('I')[-1])
        text_lines[int_row - 1] = text_lines[int_row - 1].split('，')[0] + '，完成\n'
        file.close()
        f = open('list.txt', 'w+', encoding='utf-8')
        f.writelines(text_lines)
        f.close()


treeview.bind('<ButtonRelease-1>', set_finish)  # 设置为完成
root.mainloop()  # 进入消息循环
