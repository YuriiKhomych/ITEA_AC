from Salvador_Sakho.l_9_sql.Home_work.sql_connection import connection_factory
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT



def task3(connection, db_name):
    pass

def task2(connection, db_name):
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connection.cursor()
    cursor.execute(sql.SQL(f"CREATE DATABASE {db_name}"))
    connection = connection_factory(db_name)
    cursor = connection.cursor()
    cursor.execute(open("create_db_structure.sql", "r").read())
    cursor.close()
    connection.commit()


def main():
    connection = connection_factory()
    task2(connection, 'my_shop_test')


if __name__ == '__main__':
    main()
