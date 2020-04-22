import psycopg2
from contextlib import closing


def fill_insert(table_name, *args):
    with closing(psycopg2.connect(
            dbname='home_base',
            user='postgres',
            password='paradise',
            host='localhost'
    )) as conn:
        print(f"Database opened successfully")
        conn.autocommit = True

        with conn.cursor() as cursor:
            cursor.execute(f''' INSERT INTO {table_name}
                                            (customer_name,
                                            contact_name,
                                            address,
                                            city,
                                            postal_code,
                                            country)
            values {args};
            ''')
