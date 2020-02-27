from contextlib import closing

import psycopg2


def delete_data(table_name, **kwargs):
    with closing(psycopg2.connect(dbname="my_shop",
                                  user="postgres",
                                  password="12011985",
                                  host="localhost", )) as conn:
        conn.autocommit = True
        with conn.cursor() as cursor:
            for key, value in kwargs.items():
                cursor.execute(
                    f"""
                    DELETE from {table_name}
                    WHERE {key} = '{value}'
                    """)
                print(cursor.rowcount)
