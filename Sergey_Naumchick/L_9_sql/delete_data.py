def delete_data(table_name, conn, data):
    with conn.cursor() as cursor:
        for key, value in data.items():
            cursor.execute(
                f"""
                DELETE from {table_name}
                WHERE {key} = '{value}'
                """)
            print(cursor.rowcount)
