# def creating_table(table_name, connection):
#     with connection.cursor() as cursor:
# cursor.execute(f"""drop table if exists {table_name} cascade""")

# cursor.execute(f"""create table if not exists {table_name} (
#      id            serial primary key,
#      name          varchar,
#      contact_name  varchar,
#      address       varchar,
#      city          varchar,
#      postal_code   varchar,
#      country       varchar
#  )""")

def creating_table(table_name, connection, data):
    with connection.cursor() as cursor:
        #-> This will delete table:

        # cursor.execute(f"""drop table if exists {table_name} cascade""")

        # creating table
        text_columns = ''
        for key, value in data.items():
            text_columns += (f"{key} {value},")
        cursor.execute(f"""create table if not exists {table_name} ({text_columns.rstrip(',')})""")
