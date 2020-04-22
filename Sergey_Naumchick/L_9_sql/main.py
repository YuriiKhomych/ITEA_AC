from contextlib import closing
import psycopg2
from creating_table import creating_table
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

        '''creating table'''

        creating_table(table_name='customers', connection=conn, data={
            'customer_id': 'varchar',
            'customer_name': 'varchar',
            'address': 'varchar',
            'city': 'varchar',
            'country': 'varchar',
        })

        '''inserting data *args in table_name'''

        insert_data(table_name='products', connection=conn, data={
            'category_id': '2',
            'product_name': 'microwave oven LG',
            'price': '2000 grn',
            'product_code': '120021',
        })

        '''updating data in table'''

        updating_table(table_name='customers', conn=conn,
                       new_value='John Backer',
                       data={'customer_name': 'John Morgan'}, )

        '''deleting data'''

        delete_data(table_name='customers', conn=conn, data={'customer_name': 'John Backer'})

        '''selecting data'''

        print(select_data(table_name='customers', conn=conn, row_name='address'))

        '''Joining tables'''

        join_tab(connection=conn, tab_1='categories', category='category_id', tab_2='products', )


if __name__ == '__main__':
    main()
