def creating_table(table_name, connection):
    with connection.cursor() as cursor:
        cursor.execute(f"""drop table if exists {table_name} cascade""")

        cursor.execute(f"""create table if not exists {table_name} (
             id            serial primary key,
             name          varchar,
             contact_name  varchar,
             address       varchar,
             city          varchar,
             postal_code   varchar,
             country       varchar
         )""")
