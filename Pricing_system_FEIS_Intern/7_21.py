# 先把介面寫出來

import tkinter as tk
from tkinter import ttk
import tkinter.font as tkfont
import pandas as pd

file_path = "ISIN_code_test.xlsx"  # 記得替換成你的Excel檔案路徑
df = pd.read_excel(file_path, engine="openpyxl")

def search_button_clicked():
    search_input = input_entry.get()  # Get the user input from the Entry widget

    if search_input in df["ISIN"].values:  # Assuming you have some criteria to check if BOOL is true or false
        # BOOL is true, show a new window with checkboxes and a "Delete ISIN" button
        new_window = tk.Toplevel(root)
        new_window.title("編輯現有ISIN")
        new_window.geometry("800x600")

        # Create five checkboxes for a bank, b bank, c bank, d bank, and e bank
        a_bank_var = tk.BooleanVar()
        a_bank_var.set(1)
        b_bank_var = tk.BooleanVar()
        c_bank_var = tk.BooleanVar()
        d_bank_var = tk.BooleanVar()
        e_bank_var = tk.BooleanVar()

        a_bank_checkbox = tk.Checkbutton(new_window, text='全選', variable=a_bank_var, font=("微軟正黑體", 16))
        b_bank_checkbox = tk.Checkbutton(new_window, text='玉山', variable=b_bank_var, font=("微軟正黑體", 16))
        c_bank_checkbox = tk.Checkbutton(new_window, text='星展', variable=c_bank_var, font=("微軟正黑體", 16))
        d_bank_checkbox = tk.Checkbutton(new_window, text='國泰', variable=d_bank_var, font=("微軟正黑體", 16))
        e_bank_checkbox = tk.Checkbutton(new_window, text='富邦', variable=e_bank_var, font=("微軟正黑體", 16))

        a_bank_checkbox.pack()
        b_bank_checkbox.pack()
        c_bank_checkbox.pack()
        d_bank_checkbox.pack()
        e_bank_checkbox.pack()

        # Add a "Delete ISIN" button
        delete_button = tk.Button(new_window, text="Delete ISIN", font=("微軟正黑體", 16))
        delete_button.pack()

    else:
        # BOOL is false, show a new window with checkboxes and an "Add ISIN" button
        new_window = tk.Toplevel(root)
        new_window.title("新增ISIN")
        new_window.geometry("800x600")

        # Create five checkboxes for a bank, b bank, c bank, d bank, and e bank
        a_bank_var = tk.BooleanVar()
        b_bank_var = tk.BooleanVar()
        c_bank_var = tk.BooleanVar()
        d_bank_var = tk.BooleanVar()
        e_bank_var = tk.BooleanVar()

        a_bank_checkbox = tk.Checkbutton(new_window, text='全選', variable=a_bank_var, font=("微軟正黑體", 16))
        b_bank_checkbox = tk.Checkbutton(new_window, text='玉山', variable=b_bank_var, font=("微軟正黑體", 16))
        c_bank_checkbox = tk.Checkbutton(new_window, text='星展', variable=c_bank_var, font=("微軟正黑體", 16))
        d_bank_checkbox = tk.Checkbutton(new_window, text='國泰', variable=d_bank_var, font=("微軟正黑體", 16))
        e_bank_checkbox = tk.Checkbutton(new_window, text='富邦', variable=e_bank_var, font=("微軟正黑體", 16))

        a_bank_checkbox.pack()
        b_bank_checkbox.pack()
        c_bank_checkbox.pack()
        d_bank_checkbox.pack()
        e_bank_checkbox.pack()

        # Add an "Add ISIN" button
        add_button = tk.Button(new_window, text="Add ISIN", font=("微軟正黑體", 16))
        add_button.pack()

# ... (rest of the code)


def generate_report_button_clicked():
    # 在這裡寫第二個分頁的製作報表功能
    pass
def generate_bank_report_button_clicked(bank_name):
    # 在這裡寫第三和第四個分頁的製作按鈕功能
    pass

def search_report_button_clicked():
    # 在這裡寫第五個分頁的搜尋功能
    pass

def load_excel_file():
    file_path = "ISIN_code_test.xlsx"  # 記得替換成你的Excel檔案路徑
    df = pd.read_excel(file_path, engine="openpyxl")

    # 建立新的視窗顯示股票代碼
    display_window = tk.Toplevel(page1)
    display_window.title("股票代碼一覽")

    # 使用Treeview元件顯示股票代碼
    tree = ttk.Treeview(display_window, columns=("ISIN"), show="headings")
    tree.heading("ISIN", text="ISIN --- code")
    tree.pack(fill="both", expand=True)

    for item in df["ISIN"]:
        stock_code = item
        tree.insert("", "end", values=(stock_code,))

# 建立主視窗
root = tk.Tk()
root.geometry("1080x720+400+200")
root.config(bg="gray")
root.title("證券經濟部報價平台")
# 設定視窗的icon
root.iconbitmap('feis_logo.ico')  # 將 'path/to/your/icon.ico' 替換為您的圖標檔案的路徑


# 建立分頁
notebook = ttk.Notebook(root)
#
# 第一個分頁
page1 = ttk.Frame(notebook)
notebook.add(page1, text='更新及刪除ISIN-code')

# 自定義第一個分頁的風格
style = ttk.Style()
style.configure("Page1.TFrame", background="white")
page1.configure(style="Page1.TFrame")



# 搜尋框和搜尋按鈕
input_entry = tk.Entry(page1,bg="white",font=("微軟正黑體",18))
search_button = tk.Button(page1, text='搜尋',fg='black',bg="grey",font=('微軟正黑體',18), command=search_button_clicked)
#
garbage1 = tk.Label(page1,text="請輸入ISIN-code",bg="white",font=('微軟正黑體',18))
load_button = tk.Button(page1, text="查看ISIN_CODE",font=('微軟正黑體',18) ,command=load_excel_file)
#
garbage1.grid(row=0,column=0,columnspan=5,padx = 50)
input_entry.grid(row=0, column=6, padx=10, pady=10)  # columnspan=2 讓 widget 佔據兩個 column，使其置中
search_button.grid(row=0, column=7, padx=10, pady=10)#
load_button.grid(row=0,column=8,padx=10,pady=10)






#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 第二個分頁
page2 = ttk.Frame(notebook)
notebook.add(page2, text='製作先備報表')
# 自定義第2個分頁的風格
page2.configure(style="Page1.TFrame")

# 自定義第二個分頁按鈕的風格

# 製作報表按鈕
report_button = tk.Button(page2, text='製作報表', command=generate_report_button_clicked)
report_button.config(font=("微軟正黑體", 16), foreground="black", background="grey")  # 設定按鈕字型和顏色
report_button.pack(padx=30, pady=300)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 第三個分頁
page3 = ttk.Frame(notebook)
notebook.add(page3, text='選擇報價銀行')
page3.configure(style="Page1.TFrame")

# 自訂字型大小和樣式
checkbox_font = tkfont.Font(family="微軟正黑體", size=16)

all_bank_var = tk.BooleanVar() # all bank button
bank_Eusan_var = tk.BooleanVar()
bank_Sbc_var = tk.BooleanVar()
bank_Catchy_var = tk.BooleanVar()
bank_Fubon_var = tk.BooleanVar()

all_bank_checkbox = tk.Checkbutton(page3, text='全選', variable=all_bank_var, font=checkbox_font)
bank_Eusan_checkbox = tk.Checkbutton(page3, text='玉山銀行', variable=bank_Eusan_var, font=checkbox_font)
bank_Sbc_checkbox = tk.Checkbutton(page3, text='星展銀行', variable=bank_Sbc_var, font=checkbox_font)
bank_Catchy_checkbox = tk.Checkbutton(page3, text='國泰銀行', variable=bank_Catchy_var, font=checkbox_font)
bank_Fubon_checkbox = tk.Checkbutton(page3, text='富邦銀行', variable=bank_Fubon_var, font=checkbox_font)

all_bank_checkbox.pack()
bank_Eusan_checkbox.pack()
bank_Sbc_checkbox.pack()
bank_Catchy_checkbox.pack()
bank_Fubon_checkbox.pack()
generate_bank_report_button = tk.Button(page3, text='製作', command=lambda: generate_bank_report_button_clicked("bank1" if bank1_var.get() else "bank2"))
generate_bank_report_button.config(font=("微軟正黑體", 16), foreground="black", background="grey")  # 設定按鈕字型和顏色
generate_bank_report_button.pack()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 第四個分頁
page4 = ttk.Frame(notebook)
notebook.add(page4, text='郵寄至銀行窗口')
page4.configure(style="Page1.TFrame")

all_bank_checkbox = tk.Checkbutton(page4, text='全選', variable=all_bank_var, font=checkbox_font)
bank_Eusan_checkbox = tk.Checkbutton(page4, text='玉山銀行', variable=bank_Eusan_var, font=checkbox_font)
bank_Sbc_checkbox = tk.Checkbutton(page4, text='星展銀行', variable=bank_Sbc_var, font=checkbox_font)
bank_Catchy_checkbox = tk.Checkbutton(page4, text='國泰銀行', variable=bank_Catchy_var, font=checkbox_font)
bank_Fubon_checkbox = tk.Checkbutton(page4, text='富邦銀行', variable=bank_Fubon_var, font=checkbox_font)

all_bank_checkbox.pack()
bank_Eusan_checkbox.pack()
bank_Sbc_checkbox.pack()
bank_Catchy_checkbox.pack()
bank_Fubon_checkbox.pack()

send_report_button = tk.Button(page4, text='寄出報表', command=lambda: generate_bank_report_button_clicked("bank3" if bank3_var.get() else "bank4"))
send_report_button.config(font=("微軟正黑體", 16), foreground="black", background="grey")  # 設定按鈕字型和顏色
send_report_button.pack()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Banks_Chinese_en = {"玉山":'Eusan',"星展":'Sbc',"國泰":'Catchy',"富邦":'Fubon'}
# 第五個分頁
page5 = ttk.Frame(notebook)
notebook.add(page5, text='編輯銀行郵寄窗口')
page5.configure(style="Page1.TFrame")


# 新增四個按鈕 (玉山、星展、國泰、富邦)
def bank_button_clicked(bank_name):
    bank_str = Banks_Chinese_en[bank_name]
    bank_str = bank_str+"_mail.xlsx"

    temp_df = pd.read_excel(bank_str, engine="openpyxl")

    # 建立新的視窗顯示股票代碼
    display_window = tk.Toplevel(page5)
    display_window.title(bank_str+"信箱")

    # 使用Treeview元件顯示股票代碼
    tree = ttk.Treeview(display_window, columns=("account"), show="headings")
    tree.heading("account", text="account")
    tree.pack(fill="both", expand=True)

    for item in temp_df["account"].values:
        account = item
        tree.insert("", "end", values=(account,))


    # 在這裡寫處理按下按鈕的功能，您可以根據 bank_name 來辨別使用者按下了哪個按鈕
    pass

bank_buttons_frame = tk.Frame(page5)  # 建立一個 Frame 放置按鈕
bank_buttons_frame.pack(pady=20)

banks = ["玉山", "星展", "國泰", "富邦"]
for bank in banks:
    bank_button = tk.Button(bank_buttons_frame, text=bank, command=lambda b=bank: bank_button_clicked(b))
    bank_button.config(font=("微軟正黑體", 16), foreground="black", background="grey")  # 設定按鈕字型和顏色
    bank_button.pack(side=tk.LEFT, padx=10)


# 設定分頁的頁籤大小
style = ttk.Style()
style.configure("TNotebook.Tab", font=('微軟正黑體', 16), padding=[20, 8])  # 設定頁籤的字型和內部padding

notebook.pack(expand=True, fill='both')


root.mainloop()