import psycopg2

conn = psycopg2.connect(
    dbname="my_shop",
    user="postgres",
    password=12011985,
    host="localhost",
)
conn.autocommit = True
cursor = conn.cursor()

# cursor.execute("""drop table if exists curs""")

cursor.execute("""create table if not exists curs(
    id            serial primary key,
    customer_name varchar,
    contact_name  varchar,
    address       varchar,
    city          varchar,
    postal_code   varchar,
    country       varchar
)""")

# cursor.execute(
#     """
# insert into curs (customer_name,
#                        contact_name,
#                        address,
#                        city,
#                        postal_code,
#                        country)
# values ('Alfreds Futterkiste ', 'Maria Anders',
#         'Obere Str. 57', 'Berlin', '12209',
#         'Germany');
# """
# )


# cursor.execute(
#     """
#     insert into curs (customer_name,
#                         contact_name,
#                         address,
#                         city,
#                         postal_code,
#                         country)
# values ('Sergy Davidenko','Sergey Svay','zabluda strasse','Brovary', '14000','Ukraine');""")

cursor.close()
conn.close()
