from Salvador_Sakho.l_9_sql.Home_work.sql_connection import connection_factory
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import re


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
    delete_data('my_shop_test', 'categories', 'category_id', 2)


if __name__ == '__main__':
    main()
