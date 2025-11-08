import psycopg2
def create():
	# připojení k SQL databázi
	connection = psycopg2.connect(
		dbname='student',
		user='postgres',
		password='admin',
		host='localhost',
		port='5432'
	)
	# SQL příkazy
	cur = connection.cursor()
	cur.execute('''CREATE TABLE teacher(
							ID SERIAL,
							NAME TEXT,
							AGE INT,
							ADDRESS TEXT
	)''')
	# uloženi SQL příkazů do databáze
	connection.commit()
	# vypnutí připojeni
	connection.close

def insert_data(teacher_name, teacher_age, teacher_address):
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
	cur.execute(query, (teacher_name, teacher_age, teacher_address))
	connection.commit()
	connection.close()
insert_data('Lockhart', 45, 'Bradavice')