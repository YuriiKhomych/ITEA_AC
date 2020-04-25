import psycopg2
from contextlib import closing


def update_rows(table_name, *args, **kwargs):
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
                for arr in args:
                    cursor.execute(f''' UPDATE {table_name} set 
                                                {key} = '{arr}' 
                                                where 
                                                {key} = '{value}'
                    ''')
                    print("Total updated rows:", cursor.rowcount)
