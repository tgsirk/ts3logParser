import time

import configuration
import mysql_staff
import searching_engine


def parsing_cycle():
    mysql_staff.create_table()
    start_query_date = mysql_staff.get_last_existing_timestamp()
    registered_users_list = searching_engine.search_logs(start_query_date)
    if len(registered_users_list) > 1:
        mysql_staff.insert_values(registered_users_list)


while True:
    parsing_cycle()
    time.sleep(configuration.PERIOD)
