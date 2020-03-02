import psycopg2
from contextlib import closing


def select_join_data(table_name, table_name2, cloud):
    with closing(psycopg2.connect(
            dbname='home_base',
            user='postgres',
            password='paradise',
            host='localhost'
    )) as conn:
        print(f"Database opened successfully")
        conn.autocommit = True

        with conn.cursor() as cursor:
            cursor.execute(f''' SELECT * from {table_name} 
        INNER JOIN {table_name2} 
        on {table_name}.{cloud}={table_name2}.{cloud};
                ''')
            print("Select is :", cursor.fetchone())
