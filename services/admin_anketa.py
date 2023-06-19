import psycopg2

from config_data.config import load_config

config = load_config()



def get_ankets():
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
            cur.execute('''SELECT user_id, photo, name, email, 
                    education, age, gender, description, time_update
                    FROM anketa''')
            ankets = cur.fetchall()
            print(f'Печатаем анкеты: {ankets}')
            return ankets
    except Exception as _ex:
        print('[INFO-get_users] Error while working with PostgreSQL', _ex)
    finally:
        if connection:
            connection.close()
            print('[INFO-get_users] PostgreSQL connection closed')

if __name__ == '__main__':
    print(*get_ankets(), sep='\n')
