from insert_data import insert_data
from update_table import updating_table
from delete_data import  delete_data

insert_data(
    'curs',
    'hhhasdsa',
    'Kiril',
    'Shevchenko_str',
    'Kiev',
    '14000',
    'Ukraine',
)

updating_table(
    # set value
    'Andrey',
    # if row meaning = smth
    contact_name='Kiril',
)

    # deleting data
delete_data('curs',contact_name='Kiril')