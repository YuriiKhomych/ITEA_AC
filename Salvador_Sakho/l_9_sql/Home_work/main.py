from Salvador_Sakho.l_9_sql.Home_work.sql_connection import connection_factory
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import re


# task 7
def select_join(db_name, table_1, table_2, column_tab_1, column_tab_2):
    connection_object = connection_factory(db_name)
    cursor = connection_object.cursor()
    cursor.execute(sql.SQL(f'select * '
                           f'from {table_1} as tab1 '
                           f'join '
                           f'{table_2} as tab2 '
                           f'on tab1.{column_tab_1} = tab2.{column_tab_2}'))
    result_set = cursor.fetchall()
    cursor.close()
    connection_object.close()
    return result_set


# task 6
def multiple_selects(db_name, table_1, columns='*', where_condition=''):
    connection_object = connection_factory(db_name)
    cursor = connection_object.cursor()
    cursor.execute(sql.SQL(f'select {columns} '
                           f'from {table_1} as tab1 '
                           f'{where_condition}'))
    result_set = cursor.fetchall()
    cursor.close()
    connection_object.close()
    return result_set


#  task 7/ task 6
# Нету смысла выписывать 5 разных видов селекта
# , когда мы можем дать возможность пользователю
# самому поределять какой селект он хочет
def select_data(db_name, query=''):
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
        connection_object = connection_factory(db_name)
        cursor = connection_object.cursor()
        cursor.execute(sql.SQL(query))
        result_set = cursor.fetchall()
        cursor.close()
        connection_object.close()
        return result_set


# task 5
def delete_data(db_name, table_name, condition_column, condition):
    connection_object = connection_factory(db_name)
    cursor = connection_object.cursor()
    condition = condition if isinstance(condition, int) \
        else "'" + condition + "'"
    cursor.execute(
        f"delete from {table_name} "
        f"where {condition_column} = {condition}"
    )
    cursor.close()
    connection_object.commit()


# task 4
def update_data(db_name, table_name, column_name, value
                , condition_column, condition):
    connection_object = connection_factory(db_name)
    cursor = connection_object.cursor()
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
    connection_object.commit()


# task 3
def insert_data(db_name, table_name, data_collection):
    connection_object = connection_factory(db_name)
    cursor = connection_object.cursor()
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
    cursor.close()
    connection_object.commit()


# task 2
def create_db(db_name):
    connection_object = connection_factory()
    connection_object.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connection_object.cursor()
    cursor.execute(sql.SQL(f"CREATE DATABASE {db_name}"))
    connection_object = connection_factory(db_name)
    cursor = connection_object.cursor()
    cursor.execute(open("create_db_structure.sql", "r").read())
    cursor.close()
    connection_object.commit()
    connection_object.close()


def main():
    # create_db(connection, 'my_shop_test')
    # insert_data('my_shop_test', 'categories',
    #             (['some category name', 'some ditch']
    #              , ['some another category name', 'some another ditch']))
    # update_data('my_shop_test', 'categories', 'categoryname'
    # , 'New column name' ,'category_id', 2)
    # delete_data('my_shop_test', 'categories', 'category_id', 2)

    result_set = multiple_selects('my_shop_test', 'orders'
                                  , 'customer_id, employeeid'
                                  ,'where customer_id in  (1,2)')
    for data in result_set:
        print(data)


if __name__ == '__main__':
    main()
