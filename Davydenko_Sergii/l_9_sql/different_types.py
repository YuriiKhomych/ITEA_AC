import psycopg2
from contextlib import closing


def different_types(table_name, **kwargs):
    with closing(psycopg2.connect(
            dbname='home_base',
            user='postgres',
            password='paradise',
            host='localhost'
    )) as conn:
        print(f"Database opened successfully")
        conn.autocommit = True

        with conn.cursor() as cursor:
            for key, value in kwargs.items():
                cursor.execute(f''' SELECT {key} FROM {table_name}
                ''')
            rows = cursor.fetchall()

            for row in rows:
                print('Customer_name is ', row[0])
                # print('City', row[0])