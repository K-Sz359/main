# _*_ coding: utf-8 _*_

from Tkinter import *
import sys
import tkMessageBox
#ダイアログメッセージ

my_window = Tk()


# Print
def say_url():
    #ここで，urlにEntryの中身が入る
    url = TextBox.get()
    print url
    tkMessageBox.showinfo('Info', 'スクレイピングを開始します．')


# window close
def window_close():
    tkMessageBox.showinfo('Info', 'タブを閉じます．')
    my_window.quit()
    print "Exit"


#Title_var
my_window.title(u"XSS")


# label
my_label = Label(master=my_window,text="URL")
my_label.place(x=30,y=30)


# box
TextBox = Entry(master=my_window, width=30)
TextBox.place(x=95,y=30)




# button
url_button = Button(master=my_window, text="Go!!",command=say_url)
url_button.place(x=400, y=30)


my_button = Button(master=my_window, text="Exit!!",command=window_close)
my_button.place(x=220, y=200)


# window size
my_window.geometry("500x250")


my_window.mainloop()
