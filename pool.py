import psycopg2
from psycopg2 import pool

# Inicializace poolu
db_pool = pool.SimpleConnectionPool(1, 10,
																		dbname='student',
																		user='postgres',
																		password='admin',
																		host='localhost',
																		port='5432')

def create_table():
	with db_pool.getconn() as conn:
		with conn.cursor() as cur:
			cur.execute('''CREATE TABLE test(
				ID SERIAL,
				NAME TEXT,
				AGE INT,
				ADDRESS TEXT
			)''')
			conn.commit()
		db_pool.putconn(conn)

# create_table()

def insert_data(teacher_name, teacher_age, teacher_address):
	with db_pool.getconn() as conn:
		with conn.cursor() as cur:
			query = '''INSERT INTO test(name, age, address)
			  VALUES (%s, %s, %s)'''
			cur.execute(query, (teacher_name, teacher_age, teacher_address))
			conn.commit()
		db_pool.putconn(conn)

insert_data('Brumal', 45, 'Bradavice')