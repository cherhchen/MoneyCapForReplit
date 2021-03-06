from tkinter import *
import tkinter as tk
import webbrowser
from tkinter import font
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from tkcalendar import Calendar, DateEntry, tooltip
import matplotlib.pyplot as plt
import numpy as np
from PIL import ImageTk, Image

list_of_entries = []
total = 0
housing = 0
transportation = 0
food = 0
utilities = 0
entertainment = 0
medical = 0
clothing = 0
insurance = 0
charity = 0
savings = 0
other = 0
dollars_each_category = {}

def buttonClicked(date_entry, category_entry, item_entry, expense_entry):
    global total, housing, transportation, food, utilities, entertainment, medical, clothing, insurance, charity, savings, other, dollars_each_category

    if expense_entry.strip() != '' and expense_entry.isdecimal() == True:
        list_of_entries.append(AnEntry(date_entry, category_entry, item_entry, expense_entry))
        #print("Button is clicked!")

        for widget in scrollable_frame.winfo_children():
            widget.destroy()

        for widget in errorFrame.winfo_children():
            widget.destroy()

        for widget in stats_frame.winfo_children():
            widget.destroy()
        

        rownum = 0
        total = 0
        for i in list_of_entries:
            i.displayDate().grid(row = rownum, column=0, padx=15, pady=5)
            i.displayCategory().grid(row = rownum, column=1, padx=15, pady=5)
            i.displayName().grid(row = rownum, column=2, padx=15, pady=5)
            i.displayExpense().grid(row = rownum, column=3, padx=15, pady=5)
            total += float(i.expense)
            #print(total)
            rownum += 1

        if category_entry == 'Housing':
            housing += round(float(expense_entry),2)
        elif category_entry == 'Transportation':
            transportation += round(float(expense_entry),2)
        elif category_entry == "Food":
            food += round(float(expense_entry),2)
        elif category_entry == 'Utilities':
            utilities += round(float(expense_entry),2)
        elif category_entry == 'Entertainment':
            entertainment += round(float(expense_entry),2)
        elif category_entry == 'Medical':
            medical += float(expense_entry)
        elif category_entry == 'Clothing':
            clothing += float(expense_entry)
        elif category_entry == 'Insurance':
            insurance += float(expense_entry)
        elif category_entry == 'Charity':
            charity += float(expense_entry)
        elif category_entry == 'Savings':
            savings += float(expense_entry)
        elif category_entry == 'Other':
            other += float(expense_entry)

        stats_frame.place(relx=0.68, rely=0.58, relwidth= 0.28, relheight= 0.4)
        var = StringVar()
        stats_label = Label(stats_frame, relief=RAISED, textvariable=var, bg='#bfe9f5', font=('Courier', 8))
        var.set("Housing: $" + str(round(housing,2)) + "\n Transportation: $" + str(round(transportation,2)) + "\n Food: $" + str(round(food,2)) + "\n Utilities: $" + str(round(utilities,2)) + "\n Entertainment: $" + str(round(entertainment,2)) + "\n Medical: $" + str(round(medical,2)) + "\n Clothing: $" + str(round(clothing,2)) + "\n Insurance: $" + str(round(insurance,2)) + "\n Charity: $" + str(round(charity,2)) + "\n Savings: $" + str(round(savings,2)) + "\n Other: $" + str(round(other,2)))
        stats_label.pack(fill=X)

        totalvar = StringVar()
        total_label = Label(stats_frame, relief=RAISED, textvariable=totalvar, bg='#bfe9f5', font=('Courier', 9 ,'bold'))
        totalvar.set("Total: $" + str(total))
        total_label.pack(pady=1, fill=BOTH)

        dollars_each_category = {'Housing':housing, 'Transportation':transportation, 'Food':food, 'Utilities':utilities, 'Entertainment':entertainment, 'Medical':medical, 'Clothing':clothing, 'Insurance':insurance, 'Charity':charity, 'Savings':savings, 'Other':other}
    else:
        errorMessage = tk.Label(errorFrame, text='Error: Please input the appropriate values.', font=('Courier', 11), fg='red')
        errorMessage.place(relx=0.5, rely=0.5, anchor=CENTER)

class AnEntry():
    def __init__(self, date, category, name, expense):
        self.date = date
        self.category = category
        self.name = name
        self.expense = expense
    
    def displayDate(self):
        label = tk.Label(scrollable_frame, text=self.date, font=('Courier', 10), relief=RAISED)
        #print(self.date, self.category, self.name, self.expense)
        return label

    def displayCategory(self):
        label = tk.Label(scrollable_frame, text=self.category, font=('Courier', 10), relief=RAISED)
        return label
    
    def displayName(self):
        label = tk.Label(scrollable_frame, text=self.name, font=('Courier', 10))
        return label
    
    def displayExpense(self):
        label = tk.Label(scrollable_frame, text=self.expense, font=('Courier', 10))
        return label

root = tk.Tk()
root.title('Money Cap')
root.geometry('600x450+0+0')

HEIGHT = 450
WIDTH = 600

canvas = tk.Canvas(root, height = HEIGHT, width= WIDTH)
canvas.pack()

title_frame = tk.Frame(root)
title_frame.place(relwidth=1, relheight=0.13)
title_img = tk.PhotoImage(file='MoneyCapBanner.gif')
title_label = tk.Label(title_frame, image=title_img)
title_label.place(relx=0, rely=0, relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#05FF70', bd=10)
frame.place(relx=0.05, rely=0.15, relwidth=0.6, relheight=0.65)

entry_canvas = tk.Canvas(frame)
scrollbar = tk.Scrollbar(frame, orient="vertical", command=entry_canvas.yview)
scrollable_frame = tk.Frame(entry_canvas)

scrollable_frame.bind("<Configure>", lambda e: entry_canvas.configure(scrollregion=entry_canvas.bbox("all")))
entry_canvas.create_window((0, 0), window=scrollable_frame, anchor='nw')
entry_canvas.configure(yscrollcommand=scrollbar.set)

entry_canvas.pack(side=LEFT, fill=BOTH, expand=True)
scrollbar.pack(side=RIGHT, fill = Y)

#LOWER USER ENTRY SECTION
lower_frame = tk.Frame(root, bg='#C6FFBD', bd=5)
lower_frame.place(relx=0.05, rely=0.8, relwidth=0.6, relheight=0.12)

cal = DateEntry(lower_frame, background='white', foreground='black', selectforeground='red', font=('Arial', 11))
cal.place(relx=0.025,rely=0.4, relwidth=0.2)
date_label = tk.Label(lower_frame, text="Date:", font=('Courier', 7), bg='#C6FFBD')
date_label.place(relx=-0.03, rely=0.1, relwidth=0.2, relheight=0.2)

category = StringVar()
dropdown_options = ["Housing", "Transportation", "Food", "Utilities", "Entertainment", "Medical", "Clothing", "Insurance", "Charity", "Savings", "Other"]
category_dropdown = OptionMenu(lower_frame, category, *dropdown_options)
category_dropdown.place(relx=0.25, rely=0.4, relwidth=0.22, relheight=0.5)
category.set(dropdown_options[10])
category_label = tk.Label(lower_frame, text="Category:", font=('Courier', 7), bg='#C6FFBD')
category_label.place(relx=0.22, rely=0.1, relwidth=0.2, relheight=0.2)

item = tk.Entry(lower_frame, highlightbackground='#C6FFBD')
item.place(relx=0.5, rely =0.4, relwidth=0.2, relheight=0.5)
item_label = tk.Label(lower_frame, text="Item Name:", font=('Courier', 7), bg='#C6FFBD')
item_label.place(relx=0.47, rely=0.1, relwidth=0.2, relheight=0.2)

expense = tk.Entry(lower_frame, highlightbackground='#C6FFBD')
expense.place(relx=0.74, rely=0.4, relwidth=0.125, relheight=0.5)
expense_label = tk.Label(lower_frame, text="Expense($):", font=('Courier', 7), bg='#C6FFBD')
expense_label.place(relx=0.71, rely=0.1, relwidth=0.2, relheight=0.2)

button = tk.Button(lower_frame, text="+", highlightbackground='#C6FFBD', command=lambda: buttonClicked(cal.get_date(), category.get(), item.get(), expense.get()))
button.place(relx=0.91, rely=0.2, relwidth=0.08, relheight=0.5)

#PIE CHART
def filterZeroNames(dict):
    newNameList = []
    for key in dict:
        if dict[key] != 0:
            newNameList.append(key)
    return newNameList

def filterZeroValues(dict):
    newValueList = []
    for value in dict.values():
        if value != 0:
            newValueList.append(value)
    return newValueList

def plot():
    fig = Figure(figsize = (5, 5,), dpi =60)
    y = filterZeroValues(dollars_each_category)
    plot1 = fig.add_subplot(111)
    plot1.pie(y, labels = filterZeroNames(dollars_each_category), shadow=True, textprops={'fontsize': 11})
    plt.show()
    canvas = FigureCanvasTkAgg(fig, master=chart_frame)
    canvas.draw()
    canvas.get_tk_widget().place(relx=0, rely=0.05, relwidth=1, relheight=0.8)
    toolbar = NavigationToolbar2Tk(canvas, chart_frame)
    toolbar.update()
    toolbar.place(relx=0, rely=0.85, relwidth=1, relheight=0.15)

chart_frame = tk.Frame(root, bd=7, bg='#05FF70')
chart_frame.place(relx=0.68, rely=0.15, relwidth=0.28, relheight=0.4)
plot_button = Button(master=root, command=plot, text='Display Pie Chart', font=('Courier', 9), highlightbackground='#05FF70')
plot_button.place(relx=0.82,rely=0.15, anchor='n')

#Error Message
errorFrame = tk.Frame(root)
errorFrame.place(relx=0.05, rely=0.95, relwidth=0.6, relheight=0.03)

#Statistics/Summary Frame
stats_frame = tk.Frame(root, bd=7, bg='#05FF70')

#NAV BAR
def go_about():
    advice_frame.place(rely=0.13, relwidth=1, relheight=0.9)
    moreinfo_frame.place_forget()

def go_home():
    advice_frame.place_forget()
    moreinfo_frame.place_forget()

def go_moreinfo():
    moreinfo_frame.place(rely=0.13, relwidth=1, relheight=0.9)
    advice_frame.place_forget()

percentage = 0.2
def calculate_recommendation(question):
    recommended_savings = round(question * percentage, 2)
    sentence = "Your recommended savings based on the amount you entered is:\n $" + str(recommended_savings)
    recommendation_sentence = tk.Label(advice_frame,text=sentence, bg='white', anchor="n")
    recommendation_sentence.place(relx=0.22, rely=0.61, relheight=0.1, relwidth=0.55)

# Advice Button
advice_frame = tk.Frame(root, bg= '#32739c')
advice_button = Button(root, text="Advice", command=go_about, font=('Arial', 9))
advice_button.place(relx=0.83, rely=0.05, relwidth=0.07, relheight=0.05)

savings_frame = tk.Frame(advice_frame, bd=12, bg='#6bf5ff')
savings_frame.place(relx=0.5, rely=0.08, relwidth=0.68, relheight=0.8, anchor='n')
savings2_frame = tk.Frame(savings_frame)
savings2_frame.place(relwidth=1, relheight=1)
savings_img = ImageTk.PhotoImage(Image.open('savingsbg.gif'))
#src https://www.switchtv.ke/Uploads/f85c15c1-4e06-4762-babf-13209be71567.jpg
savings_bg = tk.Label(savings_frame, image=savings_img)
savings_bg.pack()

advice = tk.Entry(advice_frame, highlightthickness=0)
advice.place(relx = 0.45, rely = 0.5, anchor="n")
advice2_button = Button(advice_frame, text="Enter", highlightbackground='#6bf5ff', command=lambda:calculate_recommendation(float(advice.get())))
advice2_button.place(relx = 0.57, rely = 0.497)
advice_title = tk.Label(advice_frame, text= "Savings Advice", font=('Courier', 20, 'bold'), bg='white',  anchor='n')
advice_title.place(relx=0.37, rely=0.12)
question = tk.Label(advice_frame, text="Please enter your monetary limit/income in the entry bar below.", bg='white')
question.pack(pady=150)


# Home Button
home_button = Button(root, text="Home", command=go_home, font=('Arial', 9))
home_button.place(relx=0.77, rely=0.05, relwidth=0.06, relheight=0.05)

# More info Button
moreinfo_frame = tk.Frame(root, bg= '#239e5c')
moreinfo_button = Button(root, text="More Info", command=go_moreinfo, font=('Arial', 9))
moreinfo_button.place(relx=0.9, rely=0.05, relwidth=0.09, relheight=0.05)

aboutFrame = tk.Frame(moreinfo_frame, bg='#05FF70', bd=10)
aboutFrame.place(relx=0.08, rely=0.05, relwidth=0.85, relheight=0.3)
aboutFrame2 = tk.Frame(aboutFrame, bg='white')
aboutFrame2.place(relwidth=1, relheight=1)
about_label = tk.Label(aboutFrame2, text="About Money Cap", font=('Courier', 9, 'bold'), bg='white')
about_text = tk.Label(aboutFrame2, text="It???s easy to spend money, but when it comes to saving, budgeting, and planning???well...that other part can be a little complicated.\n Introducing Money Cap: \n A tool to organize monetary expenses and learn how to budget. \n This app allows you to input your purchases, organize your items into categories, and allocate your savings. With a simple and systematic layout and personalized financial advice, Money Cap is an effective tool to advance your financial literacy skills.", font=('Arial', 8), wraplength=790, justify=CENTER, bg='white')
about_label.pack()
about_text.pack()

linksFrame = tk.Frame(moreinfo_frame, bg='#05FF70', bd=10)
linksFrame.place(relx=0.08, rely=0.4, relwidth=0.5, relheight=0.55)
linksFrame2 = tk.Frame(linksFrame, bg='white')
linksFrame2.place(relwidth=1, relheight=1)
links_label = tk.Label(linksFrame2, text="Links to Learn More", font=('Courier', 9, 'bold'), bg='white')
links_label.pack()

def callback(url):
    webbrowser.open_new_tab(url)

# Link 1 - 50/30/20 rule
link1 = Label(linksFrame2, text = "50/30/20 Rule:", fg = "blue", cursor = "hand2", font=('Arial', 10), bg='white')
actual_link1 = Label(linksFrame2, text = "https://www.nerdwallet.com/article/finance/how-to-budget" , fg = "blue", cursor = "hand2", font=('Arial', 6), bg='white')
link1.pack()
actual_link1.pack(pady=3)
link1.bind("<Button-1>", lambda e: callback("https://www.nerdwallet.com/article/finance/how-to-budget"))

# Link 2 - Budgeting for college students
link2 = Label(linksFrame2, text = "Budgeting For College Students:" , fg = "blue", cursor = "hand2", font=('Arial', 10), bg='white')
actual_link2 = Label(linksFrame2, text = "https://college.lovetoknow.com/Amount_of_Spending_Money_a_College_Student_Needs" , fg = "blue", cursor = "hand2", font=('Arial', 6), bg='white')
link2.pack()
actual_link2.pack(pady=3)
link2.bind("<Button-1>", lambda e: callback("https://college.lovetoknow.com/Amount_of_Spending_Money_a_College_Student_Needs"))

# Link 3 - 5 Ways Teens Can Start Building Credit Right Now
link3 = Label(linksFrame2, text = "5 Ways Teens Can Start Building Credit Right Now:", fg = "blue", cursor = "hand2", font=('Arial', 10),  bg='white')
actual_link3 = Label(linksFrame2, text = "https://www.credit.com/blog/how-high-school-students-can-start-building-credit-asap-166771/", fg = "blue", cursor = "hand2", font=('Arial', 6),  bg='white')
link3.pack()
actual_link3.pack(pady=3)
link3.bind("<Button-1>", lambda e: callback("https://www.credit.com/blog/how-high-school-students-can-start-building-credit-asap-166771/"))

# Link 4 - How to Invest Money
link4 = Label(linksFrame2, text = "How to Invest Money:", fg = "blue", cursor = "hand2", font=('Arial', 10), bg='white')
actual_link4 = Label(linksFrame2, text = "https://www.nerdwallet.com/article/investing/how-to-invest-money", fg = "blue", cursor = "hand2", font=('Arial', 6), bg='white')
link4.pack()
actual_link4.pack()
link4.bind("<Button-1>", lambda e: callback("https://www.nerdwallet.com/article/investing/how-to-invest-money"))

imgFrame = tk.Frame(moreinfo_frame, bd=10, bg='#05FF70')
imgFrame.place(relx=0.62, rely=0.4, relwidth=0.28, relheight=0.55)
topicsimg = ImageTk.PhotoImage(Image.open('financial-literacy.gif'))
moneyTopics = tk.Label(imgFrame, image=topicsimg, anchor='n')
moneyTopics.pack()

root.mainloop()