from src.entity.db_connection import DBConnection
from src.utils.common import Utils
import os
from datetime import datetime, timedelta


class Query(DBConnection):
    def __init__(self, connection_string):
        self.base_class = super().__init__(connection_string)

    def complete_query(is_commit=None, is_fetchall=None):
        def decorator(f):
            def wrapper(self, *args, **kwargs):
                conn = self.get_connection()

                cursor = self.get_cursor(conn)

                if is_commit:
                    f(self, *args, **kwargs, db=cursor)

                    conn.commit()

                    self.close_connection(conn)

                if is_fetchall:
                    f(self, *args, **kwargs, db=cursor)

                    rows = cursor.fetchall()

                    self.close_connection(conn)

                    return rows

            return wrapper

        return decorator

    # def add_virtual_numbers(self, mobile_number, table_name):
    #
    #     self.conn = self.get_connection()
    #
    #     self.db = self.get_cursor(self.conn)
    #
    #     self.db.execute("INSERT INTO {} (mobile_number) VALUES ({});".format(table_name, mobile_number))
    #
    #
    #     # self.db.execute("INSERT INTO {} (mobile_number) VALUES ({});".format(table_name, mobile_number))
    #
    #     self.conn.commit()
    #
    #     self.close_connection(self.conn)
    #
    #
    # def update_is_used(self, mobile_number, is_used, table_name):
    #     # number must exist in virtual numbers table
    #     self.db.execute("UPDATE {} SET is_used = {} WHERE mobile_number = {};".format(table_name, is_used, mobile_number))
    #
    #     self.conn.commit()
    #
    # def add_pkey_confirmation_table(self, table_name, primary_key_table_name):
    #
    #     self.db.execute("INSERT INTO {} (number_id) VALUES ((SELECT id FROM {} ORDER BY id DESC LIMIT 1));".format(table_name, primary_key_table_name))
    #
    #     self.conn.commit()
    #
    # def insert_confirmation_update_is_used(self, confirmation_code, primary_key_table_name, foreign_key_table_name, mobile_no):
    #
    #     self.db.execute(f"UPDATE {foreign_key_table_name} SET confirmation = {confirmation_code} WHERE number_id = "
    #                     f"(SELECT number_id FROM {foreign_key_table_name} INNER JOIN {primary_key_table_name} "
    #                     f"ON {foreign_key_table_name}.number_id = {primary_key_table_name}.id WHERE {primary_key_table_name}.mobile_number = {mobile_no});")
    #
    #     self.conn.commit()
    #
    #     self.update_is_used(mobile_no, "true", primary_key_table_name)
    #
    #
    # def get_confirmation_from_table(self, primary_key_table_name, foreign_key_table_name, mobile_no):
    #
    #     self.db.execute(f"SELECT confirmation FROM {foreign_key_table_name} "
    #                     f"INNER JOIN {primary_key_table_name} ON {primary_key_table_name}.id = "
    #                     f"{foreign_key_table_name}.number_id WHERE {primary_key_table_name}.mobile_number = {mobile_no};")
    #
    #     response = self.db.fetchall()
    #
    #     if response:
    #         return response[0][0]

    # else returns None

    # -----------------------   ---------------------------   ---------------------------   ---------------------------   ---------------------------   ---------------------------
    # ----------------------- AFTER NEW UPDATE ---------------------------
    # ----------------------- AFTER NEW UPDATE ---------------------------
    # ----------------------- AFTER NEW UPDATE ---------------------------
    # ----------------------- AFTER NEW UPDATE ---------------------------
    # ----------------------- AFTER NEW UPDATE ---------------------------
    # -----------------------   ---------------------------   ---------------------------   ---------------------------   ---------------------------   ---------------------------

    # -----------------------   ---------------------------   ---------------------------   ---------------------------   ---------------------------   ---------------------------
    # -----------------------   ---------------------------   ---------------------------   ---------------------------   ---------------------------   ---------------------------
    # -----------------------   ---------------------------   ---------------------------   ---------------------------   ---------------------------   ---------------------------

    # -----------------------   ---------------------------   ---------------------------   ---------------------------   ---------------------------   ---------------------------

    @complete_query(is_commit=True)
    def insert_new_issued_number(
        self, id_of_number, number_itself, db, is_uber=None, is_yango=None
    ):
        if is_uber:
            db.execute(
                f"INSERT INTO uber_number (portal_id, mobile_no) VALUES ({id_of_number}, "
                f"{number_itself});"
            )

        if is_yango:
            db.execute(
                f"INSERT INTO yango_number (portal_id, mobile_no) VALUES ({id_of_number}, "
                f"{number_itself});"
            )

    @complete_query(is_fetchall=True)
    def get_response_id(self, id_of_number, db, is_uber=None, is_yango=None):
        if is_uber:
            db.execute(f"SELECT id FROM uber_number WHERE portal_id = {id_of_number};")

        if is_yango:
            db.execute(f"SELECT id FROM yango_number WHERE portal_id = {id_of_number};")

    @complete_query(is_commit=True)
    def update_trip_info(
        self, portal_id, db, is_uber=None, is_yango=None
    ):  # increments by 1
        """

        :param: id_of_number, id of a reserved number
        :param is_uber: True if for uber column
        :param is_yango: True if for yango column
        :return: True if completed successfully, False if failed
        """

        # response_id = self.get_response_id(id_of_number)

        if is_uber:
            db.execute(
                f"UPDATE uber_number SET trips_completed = trips_completed + 1 WHERE portal_id = {portal_id};"
            )

        if is_yango:
            db.execute(
                f"UPDATE yango_number SET trips_completed = trips_completed + 1 WHERE portal_id = {portal_id};"
            )

    @complete_query(is_commit=True)
    def insert_confirmation_code(
        self, portal_id, confirmation_code, db, is_uber=None, is_yango=None
    ):
        # response_id = self.get_response_id(id_of_number)

        if is_uber:
            db.execute(
                f"UPDATE uber_number SET confirmation = {confirmation_code} WHERE portal_id = {portal_id};"
            )

        if is_yango:
            db.execute(
                f"UPDATE yango_number SET confirmation = {confirmation_code} WHERE portal_id = {portal_id};"
            )

    @complete_query(is_fetchall=True)
    def get_confirmation_code(self, portal_id, db, is_uber=None, is_yango=None):
        # response_id = self.get_response_id(id_of_number)

        # if response_id:

        if is_uber:
            db.execute(
                f"SELECT confirmation FROM uber_number WHERE portal_id = {portal_id};"
            )

        if is_yango:
            db.execute(
                f"SELECT confirmation FROM yango_number WHERE portal_id = {portal_id};"
            )

    @complete_query(is_fetchall=True)
    def get_last_added_number(self, db, is_uber=None, is_yango=None):
        if is_uber:
            db.execute("SELECT * FROM uber_number ORDER BY id DESC LIMIT 1;")

        if is_yango:
            db.execute("SELECT * FROM yango_number ORDER BY id DESC LIMIT 1;")

    @complete_query(is_fetchall=True)
    def get_mobile_no(self, id_of_number, db, is_uber=None, is_yango=None):
        if is_uber:
            db.execute(
                f"SELECT mobile_no FROM uber_number WHERE portal_id = {id_of_number};"
            )

        if is_yango:
            db.execute(
                f"SELECT mobile_no FROM yango_number WHERE portal_id = {id_of_number};"
            )

    @complete_query(is_commit=True)
    def insert_driver_data(self, name, phone, details, db, is_uber=None, is_yango=None):
        if is_uber:
            db.execute(
                f"INSERT INTO uber_driver_data (name, number, details, date) VALUES (%s, %s, %s, %s::timestamp);",
                (
                    name,
                    phone,
                    details,
                    datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                ),
            )
        if is_yango:
            db.execute(
                f"INSERT INTO yango_driver_data (name, number, details, date) VALUES (%s, %s, %s, %s::timestamp);",
                (
                    name,
                    phone,
                    details,
                    datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                ),
            )


if __name__ == "__main__":
    query = Query(
        Utils.get_json_to_dict(
            os.path.dirname(os.getcwd()) + "/config/database_config.json"
        )["DB_conn_str"]
    )

    query.insert_driver_data(
        "arif", "519234212", "Gray Honda Insight 77XZ712", is_yango=True
    )

    # query.pprint()
