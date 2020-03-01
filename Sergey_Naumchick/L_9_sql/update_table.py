def updating_table(*args, table_name, conn, **kwargs):
    with conn.cursor() as cursor:
        for key, value in kwargs.items():
            for arg in args:
                cursor.execute(f""" update {table_name} set {key} = '{arg}' WHERE {key} = '{value}'""")
