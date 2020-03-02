from insert_data import fill_insert
from update_rows import update_rows
from delete_rows import delete_rows
from different_types import different_types
from select_data import select_data
from select_join_data import select_join_data

# fill_insert(
#     'fishers',
#     'Sergey',
#     'som',
#     'somewhere else',
#     'Dnepr2',
#     '008756733322',
#     'Canada',
# )

# update_rows(
#     'fishers',
#     'Viktors',
#     'Oleh'
# )

# delete_rows('fishers', customer_name='Andrey')


# different_types(
#     'fishers',
#     customer_name = '',
# city = '',
# country = ''
# )


# select_data(
#     table_name='fishers',
# )

select_join_data(
    table_name='fishers',
    table_name2='lakes',
    cloud='customer_name'
)
