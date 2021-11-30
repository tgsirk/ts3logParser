# from mysql-connector-python
import mysql.connector

import configuration

database = mysql.connector.connect(
    host=configuration.MYSQL_HOST,
    user=configuration.MYSQL_USER,
    password=configuration.MYSQL_PASSWORD,
    database=configuration.MYSQL_DATABASE
)
cursor = database.cursor()


def create_table():
    cursor.execute("SHOW TABLES")
    table_exists = False
    for table in cursor:
        if configuration.MYSQL_TABLE_NAME in table:
            table_exists = True
    if not table_exists:
        cursor.execute(f"CREATE TABLE {configuration.MYSQL_TABLE_NAME} ("
                       "id INT AUTO_INCREMENT PRIMARY KEY, "
                       "date TIMESTAMP , "
                       "user_id INT UNIQUE , "
                       "adm_id INT, "
                       "adm_nickname VARCHAR(255))")


def insert_values(values):
    for item in values:
        sql = "INSERT INTO ts3_registered (date , user_id, adm_id, adm_nickname) VALUES (%s,%s,%s,%s)"
        val = (item["datetime"], item["user_id"], item["adm_user_id"], item["adm_nick"])
        try:
            cursor.execute(sql, val)
            database.commit()
        except:
            database.rollback()


create_table()
database.close()