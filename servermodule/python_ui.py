import tkinter as tk

# 기본 창 생성
uiapp = tk.Tk()
uiapp.title("Database")

# 레이블 생성
uilabel = tk.Label(uiapp, text="Enter date what you want")
uilabel.pack()

# 입력 상자 생성
uientry = tk.Entry(uiapp)
uientry.pack()

# 출력 상자 생성(진행중)
uioutput = tk.OUTSIDE()



# 버튼 생성
def button_click():
    text = entry.get()
    print(f"입력된 텍스트: {text}")

uibutton = tk.Button(uiapp, text="Submit", command=button_click)
uibutton.pack()

uiapp.mainloop()
