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

cursor.close()
conn.close()
