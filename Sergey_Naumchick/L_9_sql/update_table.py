import psycopg2
from contextlib import closing


def updating_table(*args, **kwargs, ):
    with closing(psycopg2.connect(dbname="my_shop",
                                  user="postgres",
                                  password="12011985",
                                  host="localhost", )) as conn:
        conn.autocommit = True
        with conn.cursor() as cursor:
            for key, value in kwargs.items():
                for arg in args:
                    cursor.execute(f""" update curs set {key} = '{arg}' WHERE {key} = '{value}'""")
