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