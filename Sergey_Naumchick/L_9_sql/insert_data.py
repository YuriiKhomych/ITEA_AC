def insert_data(connection, table_name, data):
    with connection.cursor() as cursor:
        column = ', '.join(data.keys())
        meaning = ''
        for value in data.values():
            meaning += f"'{value}',"
        print(f"table {table_name} is successfully inputed by data:\n{', '.join(data.values())}")
        cursor.execute(f"""insert into {table_name} ({column}) 
                        values ({meaning.rstrip(',')});""")
