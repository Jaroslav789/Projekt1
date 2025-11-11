import psycopg2

def create():
	connection = psycopg2.connect(
		dbname='student',
		user='postgres',
		password='admin',
		host='localhost',
		port='5432'
	)

	cur = connection.cursor()
	cur.execute('''CREATE TABLE teacher(
							ID SERIAL,
							NAME TEXT,
							AGE INT,
							ADDRESS TEXT
	)''')
	connection.commit()
	connection.close

def insert_data():
	connection = psycopg2.connect(
		dbname='student',
		user='postgres',
		password='admin',
		host='localhost',
		port='5432'
	)

	teacher_name = input('Jméno učitele: ')
	teacher_age = input('Věk učitele: ')
	teacher_address = input('Adresa učitele: ')

	cur = connection.cursor()
	query = '''INSERT INTO teacher(name, age, address)
						  VALUES (%s, %s, %s)'''
	cur.execute(query, (teacher_name, teacher_age, teacher_address))
	connection.commit()
	connection.close()