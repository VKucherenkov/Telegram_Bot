import psycopg2

from config_data.config import load_config

config = load_config()


async def db_start():
    try:
        connection = psycopg2.connect(
            host=config.tg_bot.host,
            user=config.tg_bot.login_psql,
            password=config.tg_bot.password_psql,
            database=config.tg_bot.db_name
        )
        connection.autocommit = True

        with connection.cursor() as cur:
            cur.execute(
                'SELECT version();'
            )
            print(f"Server version: {cur.fetchone()}")

        with connection.cursor() as cur:
            cur.execute(
                'CREATE TABLE IF NOT EXISTS anketa('
                'user_id varchar(20) PRIMARY KEY, '
                'photo varchar(100),'
                'name varchar(200),'
                'email varchar(50),'
                'education varchar(20),'
                'age smallint,'
                'gender varchar(20),'
                'description text,'
                'time_update timestamptz);'
            )
            print(f'[INFO] Database was init successfully')

    except Exception as _ex:
        print('[INFO-start] Error while working with PostgreSQL', _ex)
    finally:
        if connection:
            connection.close()
            print('[INFO-start] PostgreSQL connection closed')


async def create_profile(user_id, full_name):
    try:
        connection = psycopg2.connect(
            host=config.tg_bot.host,
            user=config.tg_bot.login_psql,
            password=config.tg_bot.password_psql,
            database=config.tg_bot.db_name
        )
        connection.autocommit = True

        with connection.cursor() as cur:
            cur.execute(
                'SELECT version();'
            )
            print(f"Server version: {cur.fetchone()}")

            cur.execute("SELECT 1 FROM anketa WHERE user_id = '{key}'".format(key=user_id))
            user = cur.fetchone()
            if not user:
                cur.execute("INSERT INTO anketa "
                            "VALUES('{}', NULL, '{}', NULL, NULL, NULL, NULL, NULL, current_timestamp(0))".format(user_id, full_name))
                print(f'[INFO] Database was added user {full_name} with id: {user_id}')

    except Exception as _ex:
        print('[INFO-create_profile] Error while working with PostgreSQL', _ex)
    finally:
        if connection:
            connection.close()
            print('[INFO-create_profile] PostgreSQL connection closed')


async def edit_profile(user_dict, user_id):
    try:
        connection = psycopg2.connect(
            host=config.tg_bot.host,
            user=config.tg_bot.login_psql,
            password=config.tg_bot.password_psql,
            database=config.tg_bot.db_name
        )
        connection.autocommit = True

        with connection.cursor() as cur:
            cur.execute(
                'SELECT version();'
            )
            print(f"Server version: {cur.fetchone()}")

            cur.execute("UPDATE anketa "
                        "SET photo = '{}', "
                        "name = '{}', "
                        "email = '{}', "
                        "education = '{}', "
                        "age = '{}', "
                        "gender = '{}', "
                        "description = '{}', "
                        "time_update = current_timestamp(0) "
                        "WHERE user_id = '{}'".format(user_dict[user_id]['photo'],
                                                       user_dict[user_id]['name'],
                                                       user_dict[user_id]['user_email'],
                                                       user_dict[user_id]['education'],
                                                       user_dict[user_id]['age'],
                                                       user_dict[user_id]['gender'],
                                                       user_dict[user_id]['desc'],
                                                       user_id
                                                       )
                        )
            print(f'[INFO] Database was updated user with id: {user_id}')

    except Exception as _ex:
        print('[INFO-edit_profile] Error while working with PostgreSQL', _ex)
    finally:
        if connection:
            # cursor.close()
            connection.close()
            print('[INFO-edit_profile] PostgreSQL connection closed')