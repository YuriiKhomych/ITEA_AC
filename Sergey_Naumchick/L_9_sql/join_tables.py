def join_tab(connection, tab_1, tab_2):
    with connection.cursor() as cursor:
        cursor.execute(f""" SELECT * FROM {tab_1}
                        INNER JOIN {tab_2}
                        ON {tab_1}.contact_name = {tab_2}.contact_name
             """)
        a = cursor.fetchall()
        for i in a:
            print(i)
