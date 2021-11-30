import mysql_staff
import searching_engine

registered_users_list = searching_engine.search_logs()
mysql_staff.create_table()
mysql_staff.insert_values(registered_users_list)
