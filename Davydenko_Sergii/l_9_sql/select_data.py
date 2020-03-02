import psycopg2
from contextlib import closing


def select_data(table_name):
    with closing(psycopg2.connect(
            dbname='home_base',
            user='postgres',
            password='paradise',
            host='localhost'
    )) as conn:
        print(f"Database opened successfully")
        conn.autocommit = True

        with conn.cursor() as cursor:
            cursor.execute(f''' SELECT * from {table_name};
                ''')
            print("Select is :", cursor.fetchone())
