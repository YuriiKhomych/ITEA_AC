import psycopg2
from contextlib import closing


def insert_data(table_name, *args):
    with closing(psycopg2.connect(dbname="my_shop",
                                  user="postgres",
                                  password="12011985",
                                  host="localhost", )) as conn:
        conn.autocommit = True
        with conn.cursor() as cursor:
            cursor.execute(f"""insert into {table_name} (
                        customer_name,
                        contact_name,
                        address,
                        city,
                        postal_code,
                        country)
    values {args};
                 """)
