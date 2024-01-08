import tkinter as tk                     
from tkinter import ttk 
import sqlite3
def click(*args): 
    date.delete(0, 'end') 

def leave(*args): 
    if date.get() == "":
        date.delete(0, 'end') 
        date.insert(0, 'YYYY-MM-DD') 
        root.focus() 

def name_query():
  nq = sqlite3.connect('train.db')

  nq_cur = nq.cursor()

  nq_cur.execute('''
  SELECT FIRST_NAME, LAST_NAME, TRAIN_NAME, T.TRAIN_NUMBER, SOURCE_STATION, DESTINATION_STATION
  FROM PASSENGER P, BOOKED B, TRAIN T
  WHERE P.SSN = B.PASSENGER_SSN
  AND B.TRAIN_NUMBER = T.TRAIN_NUMBER
  AND P.FIRST_NAME = ?
  AND P.LAST_NAME = ?;
  ''',
  (f_name.get(), l_name.get()))

  records_nq = nq_cur.fetchall()
  
  result_window = tk.Toplevel(root)
  result_window.title("Query Results")
  tree = ttk.Treeview(result_window, columns=("First Name", "Last Name", "Train Name", "Train Number", "Source Station", "Destination Station"), show="headings")
  tree.column("# 1", anchor="center", stretch="NO")
  tree.column("# 2", anchor="center", stretch="NO")
  tree.column("# 3", anchor="center", stretch="NO")
  tree.column("# 4", anchor="center", stretch="NO")
  tree.column("# 5", anchor="center", stretch="NO")
  tree.column("# 6", anchor="center", stretch="NO")
  tree.heading("First Name", text="First Name")
  tree.heading("Last Name", text="Last Name")
  tree.heading("Train Name", text="Train Name")
  tree.heading("Train Number", text="Train Number")
  tree.heading("Source Station", text="Source Station")
  tree.heading("Destination Station", text="Destination Station")

  for record in records_nq:
    tree.insert("", "end", values=record)
    
  tree.pack(expand=True, fill=tk.BOTH)  
  nq.commit()
  nq.close()

def date_query():
  dq = sqlite3.connect('train.db')

  dq_cur = dq.cursor()

  dq_cur.execute("""
  SELECT DISTINCT FIRST_NAME, LAST_NAME
  FROM PASSENGER P, BOOKED B, TRAIN T, TRAIN_STATUS S
  WHERE P.SSN = B.PASSENGER_SSN
  AND B.TRAIN_NUMBER = T.TRAIN_NUMBER
  AND T.TRAIN_NAME = S.TRAIN_NAME
  AND S.TRAIN_DATE = ?;
  """,
  (date.get(),))

  records_dq = dq_cur.fetchall()
  
  result_window = tk.Toplevel(root)
  result_window.title("Query Results")
  tree = ttk.Treeview(result_window, columns=("First Name", "Last Name"), show="headings")
  tree.column("# 1", anchor="center", stretch="NO")
  tree.column("# 2", anchor="center", stretch="NO")
  tree.heading("First Name", text="First Name")
  tree.heading("Last Name", text="Last Name")

  for record in records_dq:
    tree.insert("", "end", values=record)
    
  tree.pack(expand=True, fill=tk.BOTH)

  dq.commit()
  dq.close()

def train_query():
  tq = sqlite3.connect('train.db')

  tq_cur = tq.cursor()

  tq_cur.execute("""
  SELECT TRAIN_NAME, COUNT(PASSENGER_SSN)
  FROM BOOKED b, TRAIN t
  WHERE b.TRAIN_NUMBER = t.TRAIN_NUMBER
  AND STATUS = 'Booked'
  GROUP BY b.TRAIN_NUMBER;
  """)

  records_tq = tq_cur.fetchall()
  
  result_window = tk.Toplevel(root)
  result_window.title("Query Results")
  tree = ttk.Treeview(result_window, columns=("Train Name", "No. Passengers"), show="headings")
  tree.column("# 1", anchor="center", stretch="NO")
  tree.column("# 2", anchor="center", stretch="NO")
  tree.heading("Train Name", text="Train Name")
  tree.heading("No. Passengers", text="No. Passengers")

  for record in records_tq:
    tree.insert("", "end", values=record)
    
  tree.pack(expand=True, fill=tk.BOTH)
  
  tq.commit()
  tq.close()

def train_name_query():
  tnq = sqlite3.connect('train.db')

  tnq_cur = tnq.cursor()

  tnq_cur.execute("""
  SELECT FIRST_NAME, LAST_NAME
  FROM PASSENGER P, BOOKED B, TRAIN T
  WHERE P.SSN = B.PASSENGER_SSN
  AND B.TRAIN_NUMBER = T.TRAIN_NUMBER
  AND B.STATUS = 'Booked'
  AND T.TRAIN_NAME = ?;
  """, (train_name.get(),))

  records_tnq = tnq_cur.fetchall()
  result_window = tk.Toplevel(root)
  result_window.title("Query Results")
  tree = ttk.Treeview(result_window, columns=("First Name", "Last Name"), show="headings")
  tree.column("# 1", anchor="center", stretch="NO")
  tree.column("# 2", anchor="center", stretch="NO")
  tree.heading("First Name", text="First Name")
  tree.heading("Last Name", text="Last Name")

  for record in records_tnq:
    tree.insert("", "end", values=record)
    
  tree.pack(expand=True, fill=tk.BOTH)
  
  tnq.commit()
  tnq.close()

def del_ticket_query():
  dtq = sqlite3.connect('train.db')

  dtq_cur = dtq.cursor()

  dtq_cur.execute("""
  DELETE FROM BOOKED
  WHERE PASSENGER_SSN =
  (SELECT DISTINCT SSN
  FROM PASSENGER P, TRAIN T, BOOKED B
  WHERE P.SSN = B.PASSENGER_SSN
  AND B.TRAIN_NUMBER = T.TRAIN_NUMBER
  AND P.FIRST_NAME = ?
  AND P.LAST_NAME = ?
  AND T.TRAIN_NAME = ?)
  AND TRAIN_NUMBER =
  (SELECT TRAIN_NUMBER
  FROM TRAIN
  WHERE TRAIN_NAME = ?);
  """, (f_name.get(), l_name.get(), train_name.get(), train_name.get(),))
  
  dtq.commit()
  dtq.close()

  dtq = sqlite3.connect('train.db')

  dtq_cur = dtq.cursor()

  dtq_cur.execute("""
  SELECT FIRST_NAME, LAST_NAME, T.TRAIN_NAME, T.TRAIN_NUMBER, TICKET_TYPE, STATUS
  FROM BOOKED_LOGS B, PASSENGER P, TRAIN T
  WHERE B.PASSENGER_SSN = P.SSN
  AND B.TRAIN_NUMBER = T.TRAIN_NUMBER
  ORDER BY ID DESC
  LIMIT 1;
  """)

  records_dtq = dtq_cur.fetchall()
  result_window = tk.Toplevel(root)
  result_window.title("Query Results")
  tree = ttk.Treeview(result_window, columns=("First Name", "Last Name", "Train Name", "Train Number", "Ticket Type", "Status"), show="headings")
  tree.column("# 1", anchor="center", stretch="NO")
  tree.column("# 2", anchor="center", stretch="NO")
  tree.column("# 3", anchor="center", stretch="NO")
  tree.column("# 4", anchor="center", stretch="NO")
  tree.column("# 5", anchor="center", stretch="NO")
  tree.column("# 6", anchor="center", stretch="NO")
  tree.heading("First Name", text="First Name")
  tree.heading("Last Name", text="Last Name")
  tree.heading("Train Name", text="Train Name")
  tree.heading("Train Number", text="Train Number")
  tree.heading("Ticket Type", text="Ticket Type")
  tree.heading("Status", text="Status")

  for record in records_dtq:
    tree.insert("", "end", values=record)
    
  tree.pack(expand=True, fill=tk.BOTH)    
  
  dtq.commit()
  dtq.close()

root = tk.Tk() 
root.title("Railway Reservation System")
tabControl = ttk.Notebook(root) 
  
tab1 = ttk.Frame(tabControl) 
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl) 
  
tabControl.add(tab1, text ='Check Tickets') 
tabControl.add(tab2, text ='Train Status')
tabControl.add(tab3, text ='Cancel Ticket')

tabControl.pack(expand = 1, fill ="both") 

# TEXT BOXES
f_name = ttk.Entry(tab1, width = 30)
f_name.grid(row = 0, column = 1, padx = 20)

l_name = ttk.Entry(tab1, width = 30)
l_name.grid(row = 1, column = 1)

date = ttk.Entry(tab1, width = 30)
date.insert(0, "YYYY-MM-DD")
date.bind("<FocusIn>", click)
date.bind("<FocusOut>", leave)
date.grid(row = 2, column = 1)

train_name = ttk.Entry(tab2, width = 30)
train_name.grid(row = 0, column = 1)

f_name_cancel = ttk.Entry(tab3, width = 30)
f_name_cancel.grid(row = 0, column = 1, padx = 20)

l_name_cancel = ttk.Entry(tab3, width = 30)
l_name_cancel.grid(row = 1, column = 1)

train_name_cancel = ttk.Entry(tab3, width = 30)
train_name_cancel.grid(row = 2, column = 1)

# LABELS
f_name_label = ttk.Label(tab1, text = "First Name: ")
f_name_label.grid(row = 0, column = 0)

l_name_label = ttk.Label(tab1, text = "Last Name: ")
l_name_label.grid(row = 1, column = 0)

date_label =ttk.Label(tab1, text = "Departure Date: ")
date_label.grid(row = 2, column = 0)

train_name_label = ttk.Label(tab2, text = "Train Name: ")
train_name_label.grid(row = 0, column = 0)

f_name_cancel_label = ttk.Label(tab3, text = "First Name: ")
f_name_cancel_label.grid(row = 0, column = 0)

l_name_cancel_label = ttk.Label(tab3, text = "Last Name: ")
l_name_cancel_label.grid(row = 1, column = 0)

train_name_cancel_label = ttk.Label(tab3, text = "Train Name: ")
train_name_cancel_label.grid(row = 2, column = 0)

submit_button = ttk.Button(tab1, text = 'Search by Name', command = name_query)
submit_button.grid(row = 3, column = 0, columnspan = 2, padx = 10, ipadx = 100)

submit_button2 = ttk.Button(tab1, text = 'Search by Date', width = 10, command = date_query)
submit_button2.grid(row = 4, column = 0, columnspan = 2, padx = 10, ipadx = 100)

submit_button4 = ttk.Button(tab2, text = 'Check Train Capacity', width = 10, command = train_query)
submit_button4.grid(row = 2, column = 0, columnspan = 2, padx = 10, ipadx = 100)

submit_button5 = ttk.Button(tab2, text = 'Check Train Passengers', width = 10, command = train_name_query)
submit_button5.grid(row = 3, column = 0, columnspan = 2, padx = 10, ipadx = 100)

submit_button6 = ttk.Button(tab3, text = 'Delete Tickets', width = 10, command =  del_ticket_query)
submit_button6.grid(row = 4, column = 0, columnspan = 2, padx = 10, ipadx = 100)
  
root.mainloop()  