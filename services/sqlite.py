import datetime
import sqlite3 as sq


async def db_start():
    global db, cur

    db = sq.connect(r'database/anketa.db')
    cur = db.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS profile(user_id TEXT PRIMARY KEY, photo TEXT, name TEXT, email TEXT, "
                "education TEXT, age TEXT, gender TEXT, description TEXT, time_update TEXT)")

    db.commit()


async def create_profile(user_id):
    user = cur.execute("SELECT 1 FROM profile WHERE user_id == {key}".format(key=user_id)).fetchone()
    if not user:
        cur.execute("INSERT INTO profile "
                    "VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    (user_id, '', '', '', '', '', '', '', ''))
        db.commit()


async def edit_profile(user_dict, user_id):
    cur.execute("UPDATE profile "
                "SET photo = '{}', "
                "name = '{}', "
                "email = '{}', "
                "education = '{}', "
                "age = '{}', "
                "gender = '{}', "
                "description = '{}', "
                "time_update = '{}'"
                "WHERE user_id == '{}'".format(user_dict[user_id]['photo'],
                                               user_dict[user_id]['name'],
                                               user_dict[user_id]['user_email'],
                                               user_dict[user_id]['education'],
                                               user_dict[user_id]['age'],
                                               user_dict[user_id]['gender'],
                                               user_dict[user_id]['desc'],
                                               datetime.datetime.today().strftime('%d %B %Y %H:%M:%S'),
                                               user_id
                                               )
                )
    db.commit()
