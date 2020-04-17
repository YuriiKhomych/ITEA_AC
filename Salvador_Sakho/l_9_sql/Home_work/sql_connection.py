import traceback

import psycopg2


class ConnectionFactoryClass:
    def __init__(self, data_name=None):
        self.data_name = data_name

    def __enter__(self):
        try:
            self.connection = psycopg2.connect(
                dbname=self.data_name, user='postgres', password='admin'
            )
            return self.connection
        except:
            raise Exception()

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self.connection.close()
        except Exception:
            print(traceback.print_stack())
