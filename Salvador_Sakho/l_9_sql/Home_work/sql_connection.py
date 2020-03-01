import psycopg2


def connection_factory(data_name=None):
    try:
        connection = psycopg2.connect(
            dbname=data_name, user='postgres', password='admin'
        )
        return connection
    except:
        raise Exception()
