from Salvador_Sakho.l_9_sql.Home_work.sql_connection import \
    ConnectionFactoryClass
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import re


# task 7
def select_join(connection, table_1, table_2, column_tab_1, column_tab_2):
    cursor = connection.cursor()
    cursor.execute(
        sql.SQL(f'select * '
                f'from {table_1} as tab1 '
                f'join '
                f'{table_2} as tab2 '
                f'on tab1.{column_tab_1} = tab2.{column_tab_2}')
    )
    result_set = cursor.fetchall()
    cursor.close()
    return result_set


# task 6
def multiple_selects(connection, table_1, columns='*', where_condition=''):
    cursor = connection.cursor()
    cursor.execute(sql.SQL(f'select {columns} '
                           f'from {table_1} as tab1 '
                           f'{where_condition}'))
    result_set = cursor.fetchall()
    cursor.close()
    return result_set


#  task 7/ task 6
# Нету смысла выписывать 5 разных видов селекта
# , когда мы можем дать возможность пользователю
# самому поределять какой селект он хочет
def select_data(connection, query=''):
    if any(
            word for word in query.split(' ')
            if (
                    word.lower() in
                    ['delete', 'drop', 'truncate', 'insert', 'update', 'grant']
            )
    ):
        raise Exception(
            'Данный метод предназначен исключительно для получения данных'
        )
    else:
        cursor = connection.cursor()
        cursor.execute(sql.SQL(query))
        result_set = cursor.fetchall()
        cursor.close()
        return result_set


# task 5
def delete_data(connection, table_name, condition_column, condition):
    cursor = connection.cursor()
    condition = condition if isinstance(condition, int) \
        else "'" + condition + "'"
    cursor.execute(
        f"delete from {table_name} "
        f"where {condition_column} = {condition}"
    )
    cursor.close()
    connection.commit()


# task 4
def update_data(connection, table_name, column_name, value
                , condition_column, condition):
    cursor = connection.cursor()
    condition = condition if isinstance(condition, int) \
        else "'" + condition + "'"
    value = value if isinstance(value, int) \
        else "'" + value + "'"
    cursor.execute(
        f"update {table_name} "
        f"set {column_name} = {value}"
        f"where {condition_column} = {condition}"
    )
    cursor.close()
    connection.commit()


# task 3
def insert_data(connection, table_name, data_collection):
    cursor = connection.cursor()
    cursor.execute(f"Select * FROM {table_name} LIMIT 0")
    column_names_list = \
        [
            desc[0] for desc in cursor.description
            if re.search('_id', desc[0]) is None
        ]
    column_names = ', '.join(column_names_list)
    query_string = f"""INSERT INTO {table_name} ({column_names}) values (%s"""
    i = 1
    while i < len(data_collection[0]):
        query_string += ',%s'
        i += 1
    query_string += ')'
    cursor.executemany(query_string, data_collection)
    connection.commit()
    cursor.close()


# task 2
def create_db(db_name):
    with ConnectionFactoryClass() as connection:
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()
        cursor.execute(sql.SQL(f"CREATE DATABASE {db_name}"))
        connection_object = connection(db_name)
        cursor = connection_object.cursor()
        cursor.execute(open("create_db_structure.sql", "r").read())
        cursor.close()
        connection_object.commit()


def main():
    #create_db('my_shop_test')
    with ConnectionFactoryClass('my_shop_test') as connection:
        # insert_data(connection, 'categories',
        #             [['2121 category name', 'some ditch']
        #                 , ['some another category name', 'some another ditch']]
        #             )
        # update_data(connection, 'categories', 'categoryname'
        # , 'New column name' ,'category_id', 24)
        # delete_data(connection, 'categories', 'category_id', 23)

        result_set = multiple_selects(connection, 'orders'
                                      , 'customer_id, employeeid'
                                      , 'where customer_id in  (1,2)')
        for data in result_set:
            print(data)


if __name__ == '__main__':
    main()
