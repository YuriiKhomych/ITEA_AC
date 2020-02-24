import creating_db
import psycopg2


def insert_data(
        table_name,
        customer_name,
        contact_name,
        address,
        city,
        postal_code,
        country,
):
    creating_db.conn = psycopg2.connect(
        dbname="my_shop", user="postgres", password="12011985", host="localhost",
    )
    creating_db.conn.autocommit = True
    creating_db.cursor = creating_db.conn.cursor()
    creating_db.cursor.execute(f"""
    insert into {table_name} (
                        customer_name,
                        contact_name,
                        address,
                        city,
                        postal_code,
                        country)
    values ('{customer_name}',
            '{contact_name}',
            '{address}',
            '{city}',
            '{postal_code}',
            '{country}');
                 """)
    creating_db.cursor.close()
    creating_db.conn.close()
