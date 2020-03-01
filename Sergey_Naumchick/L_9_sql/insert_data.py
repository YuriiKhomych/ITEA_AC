def insert_data(*args, connection, table_name):
    with connection.cursor() as cursor:
        cursor.execute(f"""insert into {table_name} (
                    name,
                    contact_name,
                    address,
                    city,
                    postal_code,
                    country)
                    values {args};
                    """)
