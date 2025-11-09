from tkinter import *
import psycopg2

root = Tk()
root.title('Škola a databáze.')
root.geometry('340x280')
root.resizable(False, False) # změna velikosti okna

# FUNCTION
def insert_data(name, age, address):
	connection = psycopg2.connect(
		dbname='student',
		user='postgres',
		password='admin',
		host='localhost',
		port='5432'
	)

	cur = connection.cursor()
	query = '''INSERT INTO teacher(name, age, address)
						  VALUES (%s, %s, %s)'''
	cur.execute(query, (name, age, address))
	connection.commit()
	connection.close()


def search(id):
	connection = psycopg2.connect(
		dbname='student',
		user='postgres',
		password='admin',
		host='localhost',
		port='5432'
	)

	cur = connection.cursor()
	query = '''SELECT * FROM teacher WHERE id=%s'''
	cur.execute(query, (id))
	row = cur.fetchone()
	display_search(row)
	connection.commit()
	connection.close()

def display_search(data):
	listbox = Listbox(root, width=20, height=1)
	listbox.grid(row=8, column=1)
	listbox.insert(0, data)

def display_all():
	connection = psycopg2.connect(
		dbname='student',
		user='postgres',
		password='admin',
		host='localhost',
		port='5432'
	)

	cur = connection.cursor()
	query = '''SELECT * FROM teacher'''
	cur.execute(query)
	all_data = cur.fetchall()
	listbox = Listbox(root, width=30, height=5)
	listbox.grid(row=9, column=1)
	for one_row in all_data:
		listbox.insert(0, one_row)

display_all()

# LABELS, ENTRIES
label_general = Label(root, text="Add data")
label_general.grid(row=0, column=1)

# name section
label_name = Label(root, text="Name: ")
label_name.grid(row=1, column=0)

entry_name = Entry(root)
entry_name.grid(row=1, column=1)

# age section
label_age = Label(root, text="Age: ")
label_age.grid(row=2, column=0)

entry_age = Entry(root)
entry_age.grid(row=2, column=1)

# address section
label_address = Label(root, text="Addres: ")
label_address.grid(row=3, column=0)

entry_address = Entry(root)
entry_address.grid(row=3, column=1)

# button
button = Button(root, text='Add', command=lambda:insert_data(entry_name.get(), entry_age.get(), entry_address.get()))
button.grid(row=4, column=1)

# SEARCH SECTION
# general label
label_search = Label(root, text='Search data')
label_search.grid(row=5, column=1)

# ID section
label_id = Label(root, text='Search by ID: ')
label_id.grid(row=6, column=0)

entry_id = Entry(root)
entry_id.grid(row=6, column=1)

# button
button_search = Button(root, text='Search', command=lambda:search(entry_id.get()))
button_search.grid(row=6, column=2)

root.mainloop()