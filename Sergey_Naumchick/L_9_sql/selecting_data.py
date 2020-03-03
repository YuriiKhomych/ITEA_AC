from contextlib import closing

import psycopg2


def select_data(table_name, conn, row_name):
    with conn.cursor() as cursor:
        cursor.execute(
            f"""
                SELECT  {row_name}
                FROM {table_name}
                """)
        answers_cur = cursor.fetchall()

    answers = []
    for answer in answers_cur:
        answers.append(answer)
    return answers