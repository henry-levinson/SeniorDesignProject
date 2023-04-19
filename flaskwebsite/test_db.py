import os
from db_init import init_connect, populate_db, create_tables, del_tables

os.environ['DATABASE_HOST'] = "127.0.0.1"
os.environ['DATABASE_NAME'] = "BI_Protein_Info"
os.environ['DATABASE_USER'] = "postgres"
os.environ['DATABASE_PASSWORD'] = "sdp2023"
os.environ['DATABASE_PORT'] = "5432"


if __name__ == "__main__":
    print('Connecting to the PostgreSQL database...')
    conn = init_connect()
    print("Connected.")
    if conn:
        del_tables(conn)
        create_tables(conn)
        print("Populating Database...")
        populate_db()
        print("Populated")
        cursor = conn.cursor()
        # cursor.execute("""SELECT * FROM PROTEIN_INFO;""")
        # for table in cursor.fetchall():
        #     print(table)
