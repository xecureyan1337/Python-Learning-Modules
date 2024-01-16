# install mysql driver called "mysql Connector" and install it using pip install mysql-connector-python
import mysql.connector

class PythonDB():
    def __init__(self, db, mydb, mycursor):
        self.database = db
        self.mydb     = mydb
        self.mycursor = mycursor

    def create_connection(self):
    # connect mysql, make sure define db when create the connection
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database= self.database
        )

    def is_connected(self):
        if self.mydb.is_connected():
            print(f"Succesfully connected to database {self.database}")

    def activate_query(self):# to execture sql query
        self.mycursor = self.mydb.cursor()

    def create_db(self, new_db):
        self.mycursor.execute(f"CREATE DATABASE {new_db}")
        print(f"Database successfully created.")

    def delete_db(self):
        self.mycursor.execute(f"DROP DATABASE {self.database}")
        print(f"Database successfully deleted.")

    def show_db(self):
        self.mycursor.execute("SHOW DATABASES")

        for database in self.mycursor:
            print(database)
        
    def create_table(self, table, *name):
        self.mycursor.execute (f"CREATE TABLE {table} ({name[0]} INT AUTO_INCREMENT PRIMARY KEY, {name[1]} VARCHAR(255), {name[2]} INT (2))")

        print("Table successfully created.")

    # create_table("users", "id", "name", "age")

    def create_table_column(self, table, column):
        self.mycursor.execute (f"ALTER TABLE {table} ADD COLUMN {column}")
        
        print("Table column successfully created.")

    def run(self):
        self.create_connection()
        self.is_connected()
        self.activate_query()
        self.show_db()
        # self.create_table("users", "id", "name", "age")
        self.create_table_column("users", "key")

if __name__ == "__main__":
    #create object of class and connect to exist database
    python_db = PythonDB("pythondb", "mydb", "mycursor")
    python_db.run()

    # create new db
    # python_db.create_db("test")
