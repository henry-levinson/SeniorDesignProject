# for testing, should merge with db_init.py once finished

import os
import psycopg2
import requests, sys, json
from get_protein_info import get_protein_info
from sqlalchemy import create_engine
import random

os.environ['DATABASE_HOST'] = "localhost"
os.environ['DATABASE_NAME'] = "flask_db"
os.environ['DATABASE_USER'] = "postgres"
os.environ['DATABASE_PASSWORD'] = "123"
os.environ['DATABASE_PORT'] = "5432"

def init_connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # connect to the PostgreSQL server
        conn = psycopg2.connect(
            f'''host={os.environ['DATABASE_HOST']}
            dbname={os.environ['DATABASE_NAME']}
            user={os.environ['DATABASE_USER']}
            password={os.environ['DATABASE_PASSWORD']}
            port={os.environ['DATABASE_PORT']}'''
        )

        create_tables(conn)
		
        return conn

    except (Exception, psycopg2.DatabaseError) as error:
        print("The following error occured:",error)

def create_tables(conn):
    cur = conn.cursor()

    cur.execute('DROP TABLE IF EXISTS USER_REVIEWS;')
    cur.execute('''
        CREATE TABLE IF NOT EXISTS USER_REVIEWS (
            USER_ID VARCHAR(100),
            PUBLICATION_ID VARCHAR(100),
            SCORE REAL,
            PRINCIPAL_FINDINGS TEXT,
            METHODOLOGY TEXT,
            PRIMARY KEY (USER_ID, PUBLICATION_ID)
        );
    ''')
    
    cur.execute('DROP TABLE IF EXISTS USERS;')
    cur.execute('''
        CREATE TABLE IF NOT EXISTS USERS (
            USER_ID VARCHAR(100),
            USERNAME VARCHAR(100),
            DEPARTMENT VARCHAR(200),
            TA VARCHAR(200),
            PRIMARY KEY (USER_ID)
        );
    ''')

    cur.close()

# def populate_user_reviews(conn):
#     cur = conn.cursor()
#     cur.execute(('''INSERT INTO USER_REVIEWS (  USER_ID,
#                                                 PUBLICATION_ID,
#                                                 SCORE,
#                                                 PRINCIPAL_FINDINGS,
#                                                 METHODOLOGY)
#                 VALUES(
#                 'User1',
#                 16141072,
#                 4,
#                 'great publication good detail',
#                 'method 1'
#                 );'''
#             ))
    
#     cur.execute(('''INSERT INTO USER_REVIEWS (  USER_ID,
#                                                 PUBLICATION_ID,
#                                                 SCORE,
#                                                 PRINCIPAL_FINDINGS,
#                                                 METHODOLOGY)
#                 VALUES(
#                 'User2',
#                 16141072,
#                 8,
#                 'excellent publication great detail',
#                 'method 2'
#                 );'''
#             ))
    
#     cur.execute(('''INSERT INTO USER_REVIEWS (  USER_ID,
#                                                 PUBLICATION_ID,
#                                                 SCORE,
#                                                 PRINCIPAL_FINDINGS,
#                                                 METHODOLOGY)
#                 VALUES(
#                 'User3',
#                 16141072,
#                 0,
#                 'worst publication',
#                 'method 3'
#                 );'''
#             ))
 

# def del_tables(conn):
#     cur = conn.cursor()

#     cur.execute('''
#         DROP TABLE IF EXISTS PROTEIN_INFO;
#     ''')

#     cur.execute('''
#         DROP TABLE IF EXISTS PUBLICATION_INFO;
#     ''')

#     cur.close()


if __name__ == "__main__":
    conn = init_connect()
    #populate_user_reviews(conn)
    conn.commit()
    #populate_db()

    #cursor = conn.cursor()
    #cursor.execute("""SELECT * FROM PROTEIN_INFO;""")
    # for table in cursor.fetchall():
    #     print(table)

    #del_tables(conn)

