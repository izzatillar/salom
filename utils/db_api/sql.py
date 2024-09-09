import sqlite3


class Database:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_users(self):
        sql = """
        CREATE TABLE Users (
           chat_id integer not null,
           lang varchar(20) not null,
           city varchar(20),
           name varchar(25),
           contact varchar(20)
            );
"""
        self.execute(sql, commit=True)

    def get_branches(self, chat_id, lang):
        if lang == 'uz':
            sql = '''
    SELECT city.id FROM users 
    JOIN city on city.name_uz = users.city
    WHERE chat_id = ?
                '''
            city_id = self.execute(sql=sql, parameters=(chat_id,), fetchone=True)[0]
            sql = '''
    SELECT filials.name FROM city
    JOIN filials on city.id = filials.city_id
    WHERE city.id = ?
                '''
            branches = [i[0] for i in self.execute(sql=sql, parameters=(city_id,), fetchall=True)]
            return branches
        elif lang == 'ru':
            sql = '''
    SELECT city.id FROM users 
    JOIN city on city.name_ru = users.city
    WHERE chat_id = ?
                            '''
            city_id = self.execute(sql=sql, parameters=(chat_id,), fetchone=True)[0]
            sql = '''
    SELECT filials.name FROM city
    JOIN filials on city.id = filials.city_id
    WHERE city.id = ?
                            '''
            branches = [i[0] for i in self.execute(sql=sql, parameters=(city_id,), fetchall=True)]
            return branches
        else:
            sql = '''
    SELECT city.id FROM users 
    JOIN city on city.name_eng = users.city
    WHERE chat_id = ?
                            '''
            city_id = self.execute(sql=sql, parameters=(chat_id,), fetchone=True)[0]
            sql = '''
    SELECT filials.name FROM city
    JOIN filials on city.id = filials.city_id
    WHERE city.id = ?
                            '''
            branches = [i[0] for i in self.execute(sql=sql, parameters=(city_id,), fetchall=True)]
            return branches

    def get_category(self):
        sql = 'select name from category'
        return [i[0] for i in self.execute(sql=sql, fetchall=True)]


def logger(statement):
    print(f"""
_____________________________________________________
Executing:
{statement}
_____________________________________________________
""")
