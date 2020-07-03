import tkinter as tk
import re
from tkinter import messagebox
 #设置窗口大小
window = tk.Tk()
window.title('Simple Calculator')
window.geometry('500x500')
  #框架1 屏幕
frm = tk.Frame(window)
frm.pack()
frm1 = tk.Frame(frm)
frm2 = tk.Frame(frm)
frm1.pack(side='top')
frm2.pack()

var0 = tk.StringVar()   #文字变量储存器
t = tk.Label(frm1,textvariable=var0,bg='white', font=('Arial',12),width=50, height=3)                        #创建屏幕
t.pack()

    #框架2 按钮
ls = [['clear','=','+','-'],['0','1','2','*'],['3','4','5','/'],['6','7','8','**'],['9','.','√','//']]

    # 设置4x5个按钮
tk.Button(frm2, text=ls[0][0],width=10,height=2,command = lambda: insert_end(0,0)).grid(row=0, column=0, padx=20, pady=20)
tk.Button(frm2, text=ls[0][1],width=10,height=2,command = lambda: insert_end(0,1)).grid(row=0, column=1, padx=20, pady=20)
tk.Button(frm2, text=ls[0][2],width=10,height=2,command = lambda: insert_end(0,2)).grid(row=0, column=2, padx=20, pady=20)
tk.Button(frm2, text=ls[0][3],width=10,height=2,command = lambda: insert_end(0,3)).grid(row=0, column=3, padx=20, pady=20)

tk.Button(frm2, text=ls[1][0],width=10,height=2,command = lambda: insert_end(1,0)).grid(row=1, column=0, padx=20, pady=20)
tk.Button(frm2, text=ls[1][1],width=10,height=2,command = lambda: insert_end(1,1)).grid(row=1, column=1, padx=20, pady=20)
tk.Button(frm2, text=ls[1][2],width=10,height=2,command = lambda: insert_end(1,2)).grid(row=1, column=2, padx=20, pady=20)
tk.Button(frm2, text=ls[1][3],width=10,height=2,command = lambda: insert_end(1,3)).grid(row=1, column=3, padx=20, pady=20)

tk.Button(frm2, text=ls[2][0],width=10,height=2,command = lambda: insert_end(2,0)).grid(row=2, column=0, padx=20, pady=20)
tk.Button(frm2, text=ls[2][1],width=10,height=2,command = lambda: insert_end(2,1)).grid(row=2, column=1, padx=20, pady=20)
tk.Button(frm2, text=ls[2][2],width=10,height=2,command = lambda: insert_end(2,2)).grid(row=2, column=2, padx=20, pady=20)
tk.Button(frm2, text=ls[2][3],width=10,height=2,command = lambda: insert_end(2,3)).grid(row=2, column=3, padx=20, pady=20)

tk.Button(frm2, text=ls[3][0],width=10,height=2,command = lambda: insert_end(3,0)).grid(row=3, column=0, padx=20, pady=20)
tk.Button(frm2, text=ls[3][1],width=10,height=2,command = lambda: insert_end(3,1)).grid(row=3, column=1, padx=20, pady=20)
tk.Button(frm2, text=ls[3][2],width=10,height=2,command = lambda: insert_end(3,2)).grid(row=3, column=2, padx=20, pady=20)
tk.Button(frm2, text=ls[3][3],width=10,height=2,command = lambda: insert_end(3,3)).grid(row=3, column=3, padx=20, pady=20)

tk.Button(frm2, text=ls[4][0],width=10,height=2,command = lambda: insert_end(4,0)).grid(row=4, column=0, padx=20, pady=20)
tk.Button(frm2, text=ls[4][1],width=10,height=2,command = lambda: insert_end(4,1)).grid(row=4, column=1, padx=20, pady=20)
tk.Button(frm2, text=ls[4][2],width=10,height=2,command = lambda: insert_end(4,2)).grid(row=4, column=2, padx=20, pady=20)
tk.Button(frm2, text=ls[4][3],width=10,height=2,command = lambda: insert_end(4,3)).grid(row=4, column=3, padx=20, pady=20)

def sort_s(str):
    if str[0] == '√' and len(str) != 1: #输入内容如果只有根号的话，表达式错误，不需要在首位加1
        str = '1' + str
    #\D√num 的情形 (num可以小数也可以是整数)
    final_str = str
    ols = re.findall('\D(√\d+\.?\d*e?)',str) #把 √num 类的字符串放入列表ols
    nls = []
    for i in range(len(ols)):
        nls.append(ols[i].strip('√') + ols[i][0])     #将列表ols中每一个字符串的首位放到末位，再将新的字符串放入列表nls
    for i in range(len(nls)):
        final_str = final_str.replace(ols[i], nls[i])
                  #在str中,将列表ols中第i个字符串替换为列表nls中第i个字符串，得到final_str
                   #此时final_str中 √num 的顺序已被替换为 num√

#num√num的情形(num可以小数也可以是整数)
    ools = re.findall('\d+\.?\d*e?√\d+\.?\d*e?',str)
    nnls = re.findall('\d+\.?\d*e?√\d+\.?\d*e?',str)
#把 num√num 类的字符串放入列表ools和列表nnls
    for i in range(len(ools)):
        nnls[i] = nnls[i].replace('√','*')
        nnls[i] = nnls[i]+'√'      #将nnls中的每个字符串改为 num*num√形式

    for i in range(len(nnls)):
        final_str = final_str.replace(ools[i], nnls[i])
#在str中，将列表ools中的第i个字符串替换为列表nnls中的第i个字符串，得到final_str，此时final_str中的 num√num 的顺序已被改为num*num√
    return final_str

def change(str):
    str = str.replace('√','**(1/2)') #把√替换为**(1/2)
    return str

def insert_end(i,j):
    str = var0.get()
    if ls[i][j]!='clear' and ls[i][j]!='=':
        var0.set(var0.get()+ls[i][j])
    elif ls[i][j]=='clear':
        var0.set('')
    elif ls[i][j]=='=':
        isprime(str)

def isprime(str):
    if len(re.findall('√\D',str))>0 or str[-1] == '√':
        str = str + '***'      #使有 √\D 的表达式报错
    str = sort_s(str)     #使用sort_s函数，使字符串变为可计算的式子
    str = change(str)     #使用change函数将√与**(1/2)两字符替换，
    print(str)
    try:
        var0.set(round(eval(str),10)) #消除浮点数计算的误差，四舍五入到10位小数
    except:
        tk.messagebox.showwarning('Error','Wrong formula')

window.mainloop()
