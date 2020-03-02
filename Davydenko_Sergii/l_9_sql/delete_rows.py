import psycopg2
from contextlib import closing


def delete_rows(table_name, **kwargs):
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
                cursor.execute(f''' DELETE from {table_name} where {key} ='{value}';
                    ''')
                print("Total deleted rows:", cursor.rowcount)
