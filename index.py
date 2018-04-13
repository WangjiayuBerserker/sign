from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import requests
import re

# 模拟浏览器发送请求
def getImg():
    startUrl = 'http://www.uustv.com/'
    # 获取用户姓名
    name = entry.get()
    # 去空格
    name = name.strip()
    if name == '':
        messagebox.showinfo('提示：','请输入需签名内容！！！')
    else:
        data = {
            'word':name,
            'sizes':60,
            'fonts':'jfcs.ttf',
            'fontcolor':'#000000',
        }
        result = requests.post(startUrl,data =  data)
        result.encoding = 'utf-8'
        html = result.text
        # print(html)
        reg = '<div class="tu">﻿.*?<img src="(.*?)"/></div>'
        imgPath = re.findall(reg,html)
        # 图片完整路径
        imgUrl = startUrl + imgPath[0]
        response = requests.get(imgUrl).content
        with open('{}.gif'.format(name),'wb') as f:
            f.write(response)
        # 显示图片
        bm = ImageTk.PhotoImage(file = '{}.gif'.format(name))
        lable2 = Label(root,image = bm)
        lable2.bm = bm
        lable2.grid(row = 2,columnspan = 2)

# 创建窗口
root = Tk()
# 标题
root.title('签名设计')
# 窗口大小      宽   高
root.geometry('600x300')
# 窗口初始位置
root.geometry('+500+200')
# 标签控件
lable = Label(root,text = '签名',font = ('华文行楷',20),fg = 'red')
# 定位 grid pack place
lable.grid(row = 0, column = 0)
# 输入框
entry = Entry(root, font = ('微软雅黑',20))
entry.grid(row = 0, column = 1)
# 点击按钮
buttun = Button(root,text = '设计', font = ('微软雅黑',20),command = getImg)
buttun.grid(row = 1,column = 0)
# 消息循环  显示窗口
root.mainloop()