def delete_data(table_name, conn, **kwargs):
    with conn.cursor() as cursor:
        for key, value in kwargs.items():
            cursor.execute(
                f"""
                DELETE from {table_name}
                WHERE {key} = '{value}'
                """)
            print(cursor.rowcount)
