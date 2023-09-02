import tkinter as tk
from tkinter import ttk
import tkinter.font as tkfont
import pandas as pd

file_path = "ISIN_code_test.xlsx"  # 記得替換成你的Excel檔案路徑
df = pd.read_excel(file_path, engine="openpyxl")


def delete_isin(index):
    global df
    df = df.drop(index) # 去掉搜尋ISIN那一列
    # 設定輸出Excel檔案的路徑和檔名
    output_file = 'ISIN_code_test.xlsx' # 覆蓋掉原先ISIN_code_test.clsx檔案
    df.to_excel(output_file, index=False)# 將DataFrame輸出成Excel檔案

def update_company(index,esun_var,dbs_var,cathay_var,sunny_var):
    df.iloc[index,1:] = [int(esun_var.get()),int(dbs_var.get()),int(cathay_var.get()),int(sunny_var.get())]

    output_file = 'ISIN_code_test.xlsx' # 覆蓋掉原先ISIN_code_test.clsx檔案
    df.to_excel(output_file, index=False)# 將DataFrame輸出成Excel檔案

def insert_new_isin(isin,esun_var,dbs_var,cathay_var,sunny_var):
    global df
    # 新的資料
    new_data = {
        'ISIN': isin, 
        'ESUN': [int(esun_var.get())],
        'dbs': [int(dbs_var.get())],
        'CATHAY': [int(cathay_var.get())],
        'sunny': [int(sunny_var.get())],
    }

    # 新增新的列
    new_row_df = pd.DataFrame(new_data)
    # 合併原始DataFrame和新的DataFrame
    df = pd.concat([df, new_row_df], ignore_index=True)
    output_file = 'ISIN_code_test.xlsx' # 覆蓋掉原先ISIN_code_test.clsx檔案
    df.to_excel(output_file, index=False)# 將DataFrame輸出成Excel檔案
    
def search_button_clicked():

    file_path = "ISIN_code_test.xlsx"  # Excel path
    df = pd.read_excel(file_path, engine="openpyxl")
    

    search_input = input_entry.get()  # Get the user input from the Entry widget
    new_window = tk.Toplevel(root)
    new_window.title("刪除更新ISIN/新增ISIN")
    new_window.geometry("800x600")

    # 自訂字型大小和樣式
    checkbox_font = tkfont.Font(family="微軟正黑體", size=16)
    
      

    if search_input in df["ISIN"].values:
        text_isin_exist = tk.Label(new_window,text="ISIN-code已存在",font=('微軟正黑體',18))
        text_isin_exist.pack()
        # BOOL is true, show a new window with checkboxes and a "Delete ISIN" button

        # Get the row corresponding to the searched ISIN
        row = df[df["ISIN"] == search_input].iloc[0]
        #index = list(df["ISIN"] == search_input).index(True)
        index = df[df["ISIN"]==search_input].index[0]
        
        global esun_var 
        esun_var = tk.BooleanVar()
        esun_var.set(int(row["ESUN"]==1))
        esun_cb = tk.Checkbutton(new_window,text="玉山",variable=esun_var,font=checkbox_font)
        esun_cb.pack()

        global dbs_var 
        dbs_var = tk.BooleanVar()
        dbs_var.set(int(row["dbs"]==1))
        dbs_cb = tk.Checkbutton(new_window,text ="星展",variable=dbs_var,font=checkbox_font)
        dbs_cb.pack()

        global cathay_var 
        cathay_var = tk.BooleanVar()
        cathay_var.set(int(row["CATHAY"]==1))
        cathay_cb = tk.Checkbutton(new_window,text="國泰",variable=cathay_var,font=checkbox_font)
        cathay_cb.pack()

        global sunny_var 
        sunny_var = tk.BooleanVar()
        sunny_var.set(int(row["sunny"]==1))
        sunny_cb = tk.Checkbutton(new_window,text="陽信",variable=sunny_var,font=checkbox_font)
        sunny_cb.pack()

        # Add a "Delete ISIN" button
        delete_button = tk.Button(new_window, text="刪除此ISIN-code", font=("微軟正黑體", 16), command=lambda: delete_isin(index))

        #delete_button = tk.Button(new_window, text="刪除此ISIN-code", font=("微軟正黑體", 16),command=delete_isin(index))
        delete_button.pack()

        #add a "update company" button
        update_button = tk.Button(new_window, text="更新ISIN對應窗口", font=("微軟正黑體", 16),command=lambda: update_company(index,esun_var,dbs_var,cathay_var,sunny_var))
        update_button.pack()

    else:
        # BOOL is false, show a new window with checkboxes and an "Add ISIN" button
        text_isin_not_exist = tk.Label(new_window,text="ISIN-code目前不存在",bg="dark red",font=('微軟正黑體',18))
        text_isin_not_exist.pack()

        esun_var = tk.BooleanVar()
        dbs_var = tk.BooleanVar()
        cathay_var = tk.BooleanVar()
        sunny_var = tk.BooleanVar()

        eusan_checkbox = tk.Checkbutton(new_window, text='玉山', variable=esun_var, font=("微軟正黑體", 16))
        dbs_checkbox = tk.Checkbutton(new_window, text='星展', variable=dbs_var, font=("微軟正黑體", 16))
        catchy_checkbox = tk.Checkbutton(new_window, text='國泰', variable=cathay_var, font=("微軟正黑體", 16))
        sunny_checkbox = tk.Checkbutton(new_window, text='陽信', variable=sunny_var, font=("微軟正黑體", 16))

        eusan_checkbox.pack()
        dbs_checkbox.pack()
        catchy_checkbox.pack()
        sunny_checkbox.pack()

        # Add an "Add ISIN" button
        #def insert_new_isin(isin,esun_var,dbs_var,cathay_var,sunny_var):
        add_button = tk.Button(new_window, text="新增ISIN-code", font=("微軟正黑體", 16),command= lambda: insert_new_isin(search_input,esun_var,dbs_var,cathay_var,sunny_var))
        add_button.pack() # BOOL is true, show a new window with checkboxes and a "Delete ISIN" button
       


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
# 第一個分頁
page1 = ttk.Frame(notebook)
notebook.add(page1, text='更新及刪除ISIN-code')
# 自定義第一個分頁的風格
style = ttk.Style()
style.configure("Page1.TFrame", background="white")  #其他分業沿用
page1.configure(style="Page1.TFrame")


# ----------------------------------------------------------


# 搜尋框和搜尋按鈕
input_entry = tk.Entry(page1,bg="white",font=("微軟正黑體",18))
search_button = tk.Button(page1, text='搜尋',fg='black',bg="grey",font=('微軟正黑體',18), command=search_button_clicked)
#
text_p1 = tk.Label(page1,text="請輸入ISIN-code",bg="white",font=('微軟正黑體',18))
observe_isin_button = tk.Button(page1, text="查看ISIN_CODE",font=('微軟正黑體',18) ,command=load_excel_file)
#
text_p1.grid(row=0,column=0,columnspan=5,padx = 50)
input_entry.grid(row=0, column=6, padx=10, pady=10)  
search_button.grid(row=0, column=7, padx=10, pady=10)
observe_isin_button.grid(row=0,column=8,padx=10,pady=10)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 第二個分頁
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
page2 = ttk.Frame(notebook)
notebook.add(page2, text='製作先備報表')
# 自定義第2個分頁的風格
page2.configure(style="Page1.TFrame")

# 製作報表按鈕
report_button = tk.Button(page2, text='製作報表', command=generate_report_button_clicked)
report_button.config(font=("微軟正黑體", 16), foreground="black", background="grey")  # 設定按鈕字型和顏色
report_button.pack(padx=30, pady=300)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 第三個分頁
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
page3 = ttk.Frame(notebook)
notebook.add(page3, text='選擇報價銀行')
page3.configure(style="Page1.TFrame")

# 自訂字型大小和樣式
checkbox_font = tkfont.Font(family="微軟正黑體", size=16)

All_var_p3 = tk.BooleanVar() # all bank button
Esun_var_p3 = tk.BooleanVar()
dbs_var_p3 = tk.BooleanVar()
Cathay_var_p3 = tk.BooleanVar()
sunny_var_p3 = tk.BooleanVar()

all_bank_checkbox_p3 = tk.Checkbutton(page3, text='全選', variable=All_var_p3, font=checkbox_font)
Esun_cb_p3 = tk.Checkbutton(page3, text='玉山銀行', variable=Esun_var_p3, font=checkbox_font)
dbs_cb_p3 = tk.Checkbutton(page3, text='星展銀行', variable=dbs_var_p3, font=checkbox_font)
Cathay_cb_p3 = tk.Checkbutton(page3, text='國泰銀行', variable=Cathay_var_p3, font=checkbox_font)
sunny_cb_p3 = tk.Checkbutton(page3, text='陽信銀行', variable=sunny_var_p3, font=checkbox_font)

all_bank_checkbox_p3.pack()
Esun_cb_p3.pack()
dbs_cb_p3.pack()
Cathay_cb_p3.pack()
sunny_cb_p3.pack()
generate_bank_report_button = tk.Button(page3, text='製作', command=lambda: generate_bank_report_button_clicked("bank1" if bank1_var.get() else "bank2"))
generate_bank_report_button.config(font=("微軟正黑體", 16), foreground="black", background="grey")  # 設定按鈕字型和顏色
generate_bank_report_button.pack()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 第四個分頁
page4 = ttk.Frame(notebook)
notebook.add(page4, text='郵寄至銀行窗口')
page4.configure(style="Page1.TFrame")

all_bank_checkbox = tk.Checkbutton(page4, text='全選', variable=All_var_p3, font=checkbox_font)
bank_Eusan_checkbox = tk.Checkbutton(page4, text='玉山銀行', variable=Esun_var_p3, font=checkbox_font)
bank_dbs_checkbox = tk.Checkbutton(page4, text='星展銀行', variable=dbs_var_p3, font=checkbox_font)
bank_Catchy_checkbox = tk.Checkbutton(page4, text='國泰銀行', variable=Cathay_var_p3, font=checkbox_font)
bank_sunny_checkbox = tk.Checkbutton(page4, text='陽信銀行', variable=sunny_var_p3, font=checkbox_font)

all_bank_checkbox.pack()
bank_Eusan_checkbox.pack()
bank_dbs_checkbox.pack()
bank_Catchy_checkbox.pack()
bank_sunny_checkbox.pack()

send_report_button = tk.Button(page4, text='寄出報表', command=lambda: generate_bank_report_button_clicked("bank3" if bank3_var.get() else "bank4"))
send_report_button.config(font=("微軟正黑體", 16), foreground="black", background="grey")  # 設定按鈕字型和顏色
send_report_button.pack()

#############################################################################################################################################################
# 第五個分頁
Banks_Chinese_en = {"玉山":'玉山銀行',"星展":'DBS',"國泰":'國泰世華',"陽信":'陽信銀行'}
page5 = ttk.Frame(notebook)
notebook.add(page5, text='編輯銀行郵寄窗口')
page5.configure(style="Page1.TFrame")


# 新增四個按鈕 (玉山、星展、國泰、陽信)
def quick_ckeck(bank_name):
    global mail_df

    # 建立新的視窗顯示EMAIL
    display_window = tk.Toplevel(page5)
    display_window.title("快速查看"+bank_name+"信箱")

    # 使用Treeview元件顯示EMAIL欄位
    tree = ttk.Treeview(display_window, columns=("EMAIL",), show="headings")
    tree.heading("EMAIL", text="EMAIL")  # 設置EMAIL欄位的標題
    tree.pack(fill="both", expand=True)

    for item in mail_df[bank_name].values:
        mail = item
        tree.insert("", "end", values=(mail,))

def bank_button_clicked(bank_name):
    global mail_df
    # 重新讀入MAIL EXCEL檔案
    file_path = "test_mail.xlsx"  # 記得替換成你的Excel檔案路徑
    mail_df = pd.read_excel(file_path, engine="openpyxl")
    bank_str = Banks_Chinese_en[bank_name]
    #跳出銀行窗口 
    bank_window = tk.Toplevel(page5)
    bank_window.title(bank_str + " 郵件地址新增更改")
    bank_window.geometry("400x300")

    #快速查看
    quick_check_button = tk.Button(bank_window,text="快速查看EMAIL",fg="Black",bg="grey",font=("微軟正黑體",18),command= lambda b = bank_str: quick_ckeck(b))
    quick_check_button.pack()

    #請輸入EMAIL(文字))
    text_p5 = tk.Label(text = "請輸入EMAIL")

    #新增搜尋框
    entry_p5 = tk.Entry(bank_window,bg="white",font=("微軟正黑體",18))
    search_button = tk.Button(bank_window,text="搜尋EMAIL",fg="Black",bg="grey",font=("微軟正黑體",18))
    entry_p5.pack()
    search_button.pack()

    #存在

    #不存在 輸入名字 新增按鈕

def parse_input(input_str):
    # 尋找分號的位置
    semicolon_index = input_str.find(';')

    # 分割NAME和EMAIL
    name = input_str[:semicolon_index].strip()
    email = input_str[semicolon_index + 1:].strip()

    return name, email



bank_buttons_frame = tk.Frame(page5)  # 建立一個 Frame 放置按鈕
bank_buttons_frame.pack(pady=20)
file_path = "test_mail.xlsx"  # 記得替換成你的Excel檔案路徑
mail_df = pd.read_excel(file_path, engine="openpyxl")

banks = ["玉山", "星展", "國泰", "陽信"]
for bank in banks:
    bank_button = tk.Button(bank_buttons_frame, text=bank, command=lambda b=bank: bank_button_clicked(b))
    bank_button.config(font=("微軟正黑體", 16), foreground="black", background="grey")  # 設定按鈕字型和顏色
    bank_button.pack(side=tk.LEFT, padx=10)


# 設定分頁的頁籤大小
style = ttk.Style()
style.configure("TNotebook.Tab", font=('微軟正黑體', 16), padding=[20, 8])  # 設定頁籤的字型和內部padding

notebook.pack(expand=True, fill='both')


root.mainloop()