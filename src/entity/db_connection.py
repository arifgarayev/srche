import psycopg2

class DBConnection(object):
    """
    Creating connection with db
    """

    def __init__(self, connection_string):
        # self.conn = psycopg2.connect(connection_string, sslmode='require')
        # self.db = self.conn.cursor()

        self.connection_string = connection_string

        # self.conn = psycopg2.connect(self.connection_string, sslmode='require')



    def get_connection(self):
        return psycopg2.connect(self.connection_string)

    def get_cursor(self, connection_obj):

        return connection_obj.cursor()

    def close_connection(self, connection_obj):

        return connection_obj.close()


