import psycopg2
from contextlib import closing
from psycopg2.extras import DictCursor

# with closing(psycopg2.connect(
#         dbname='home_base',
#         user='postgres',
#         password='paradise',
#         host='localhost'
# )) as conn:
#     # print(f"Database opened successfully")
#     with conn.cursor() as cursor:
#
#         cursor.execute("""CREATE TABLE IF NOT EXISTS branch(
#         id            serial primary key,
#         customer_name varchar,
#         contact_name  varchar,
#         address       varchar,
#         city          varchar,
#         postal_code   varchar,
#         country       varchar
#     )""")
#         # print("Table created successfully")


con = psycopg2.connect(
    dbname='home_base',
    user='postgres',
    password='paradise',
    host='localhost'
)

print("Database opened successfully")
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS lakes  
     (id            serial primary key,
      customer_name varchar,
      contact_name  varchar,
      address       varchar,
      city          varchar,
      postal_code   varchar,
      country       varchar);
      ''')

print("Table created successfully")
con.commit()
con.close()
