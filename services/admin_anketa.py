import sqlite3 as sq



def get_ankets():
    query = '''SELECT user_id, photo, name, email, 
            education, age, gender, description, time_update
            FROM profile'''
    db = sq.connect('database/anketa.db')
    cur = db.cursor()
    ankets = list(cur.execute(query))
    db.close()
    return ankets


if __name__ == '__main__':
    print(*get_ankets(), sep='\n')
