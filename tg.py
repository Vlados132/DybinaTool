#Работа с файлами - Видео с ютуба,
#Работа с ткинтером - Документация
#интересно кто нибудь увидит этот код?

#доделать рамку снизу экрана про выводимую строку и всё готово

from tkinter import *

def auth():
    def document():
        top = Tk()
        top.geometry("800x800")
        top.title("Documentation")
        l2 = Label(top,text="Чтобы вставить свою базу данных нужен файл который вы вставите в ту папку где у \n вас находится это приложение, если у вас файл не .txt тогда вам нужно указать полное \n название например: Bd.xls и тд\n так же настоятельно не рекомендую выводить большое количество данных на экран так как\n максимальный вывод 86 заглавных букв ", font=20)
        l2.place(relx=0, rely=0)

    def SearchStr():
        Search = Sear.get()
        BdName = Bd.get()

        f = open(BdName + '.txt', 'r', encoding='utf-8')

        for line in f:
            if Search.lower() in line.lower():
                print(line.strip())
                Info = Label(text=line ,background='#333333' ,foreground='#FF1493', font=12) #justify=CENTER - растяжка на центр экрана
                Info.place(rely=0.65, relx=0.04)
        f.close()

    keyCheck = Key.get()

    if int(keyCheck[0]) == 1: # + int(keyCheck[1]) + int(keyCheck[2]) ==13 and int(keyCheck[3]) + int(keyCheck[4]) + int(keyCheck[5]) == 7 and int(keyCheck[6]) + int(keyCheck[7]) + int(keyCheck[8]) == 9:

        print('Terminated')

        reg.destroy()
        root = Tk()

        root.title('Dybinka')
        root.minsize(900, 510)
        root.resizable(width=True, height=True)
        root.configure(bg='#333333', borderwidth=3)

        BdText = Label(text='Введите сюда файл который мы будем открывать например:"Bd.txt": ', bg='#333333', fg='#FF1493',font=15)
        BdText.place(relx=0.01, rely=0.02)

        Bd = Entry(width=65,borderwidth=5, highlightthickness=3, highlightcolor='#FF1493',fg='#333334')
        Bd.grid(row= 1, column=0, sticky='ns')

        #bt1 = Button(text='Search Directory', command=?)
        #bt1.grid(row=1, column=1)

        root.grid_rowconfigure(0, minsize=45)

        root.grid_columnconfigure(0, minsize=460)
        root.grid_columnconfigure(1, minsize=255)

        SearchText = Label(text='Введи сюда искомую строку например-"кола": ', bg='#333333',
                       fg='#FF1493', font=15)
        SearchText.place(relx=0.025, rely=0.23)

        Sear = Entry(width=65, borderwidth=5, highlightthickness=3, highlightcolor='#FF1493',fg='#333334')
        Sear.place(rely=0.3, relx = 0.028, height=33)

        bt2 = Button(text='Search in Bd', command=SearchStr)
        bt2.place(rely=0.17, relx=0.6201)

        DocumentationButton = Button(text='Documentation', command=document, bg='#FF1493')
        DocumentationButton.place(relx=0.02, rely=0.93)



    else:
        label = Label(text='Вы неправильно ввели ключ')
        label.pack()
        reg.after(1000, lambda: DeleteMessage())

        def DeleteMessage():
            label.destroy()


reg = Tk()

reg.title('Auth')
reg.minsize(450, 260)
reg.resizable(width=False, height=False)
reg.configure(bg='#333333',borderwidth=3)

Text = Label(text='Введите ключ активации приложения', font=25,bg='#333333', fg='#FFAACC')
Text.pack(pady=5)
Key = Entry(bg='#d4d4d4', width=45, borderwidth=7, highlightthickness=3.5, highlightcolor='red',fg='#333334')
Key.pack(pady=20)
btn = Button(text='Проверка ключа', command=auth, width=15, bg='#FF1493')
btn.pack(pady=10)

reg.mainloop()