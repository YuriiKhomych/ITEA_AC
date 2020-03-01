from contextlib import closing
import psycopg2
from creating_db import creating_table
from insert_data import insert_data
from update_table import updating_table
from delete_data import delete_data
from selecting_data import select_data
from join_tables import join_tab


def main():
    with closing(psycopg2.connect(dbname="my_shop",
                                  user="postgres",
                                  password="12011985",
                                  host="localhost", )) as conn:
        conn.autocommit = True

        # creating table with columns *args and table_name,
        creating_table(
            table_name='customers',
            connection=conn)

        # inserting data *args in table_name
        insert_data(
            'hhhasdsa',
            'Andrey',
            'Shevchenko_str',
            'Kiev',
            '1400000000',
            'Ukraine',
            connection=conn,
            table_name='customers',
        )

        # updating data in table
        updating_table(
            'Andre',
            table_name='curs',
            conn=conn,
            contact_name='Andrey',
        )

        # deleting data
        delete_data(table_name='curs', conn=conn, contact_name='Kiril')

        # selecting data
        select_data(table_name='curs', conn=conn, row_name='contact_name')

        # Joining tables
        join_tab(conn, 'curs', 'customers')


if __name__ == '__main__':
    main()
