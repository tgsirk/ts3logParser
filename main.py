import mysql_staff
import searching_engine

mysql_staff.create_table()
start_query_date = mysql_staff.get_last_existing_timestamp()
registered_users_list = searching_engine.search_logs(start_query_date)
mysql_staff.insert_values(registered_users_list)

mysql_staff.database.close()
