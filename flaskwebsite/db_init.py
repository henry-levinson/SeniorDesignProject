import os
import psycopg2
import requests, sys, json
from get_protein_info import get_protein_info
from sqlalchemy import create_engine

def init_connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(
            host=os.getenv('DATABASE_HOST'),
            database=os.getenv('DATABASE_NAME'),
            user=os.getenv('DATABASE_USER'),
            password=os.getenv('DATABASE_PASSWORD'),
            port=os.getenv('DATABASE_PORT')
        )
		
        # create a cursor
        cur = conn.cursor()

        cur.execute('''
            CREATE TABLE IF NOT EXISTS PROTEIN_INFO (
                UNIPROTKB_AC VARCHAR(20) PRIMARY KEY,
                UNIPROTKB_ID VARCHAR(20),
                DESCRIPTION VARCHAR(1000),
                ENSEMBL VARCHAR(20),
                HGNC VARCHAR(20),
                PDB VARCHAR(20),
                PDB_ID VARCHAR(20),
                GTEX VARCHAR(100),
                EXPRESSION_ATLAS VARCHAR(100)
            );
        ''')

        cur.execute('''
            CREATE TABLE IF NOT EXISTS PUBLICATION_INFO (
                UNIPROTKB_AC VARCHAR(20),
                PUBLICATION_ID VARCHAR(20) PRIMARY KEY,
                PUBLICATION_NAME VARCHAR(100),
                AUTHORS VARCHAR(100),
                PRINCIPAL_FINDINGS VARCHAR(1000),
                METHODOLOGY VARCHAR(1000),
                SCORE REAL
            );
        ''')

        cur.close()
        return conn

    except (Exception, psycopg2.DatabaseError) as error:
        print("The following error occured:",error)


def populate_db():
    """Populate database with protein information and publication information"""
    host=os.getenv('DATABASE_HOST'),
    database_name=os.getenv('DATABASE_NAME'),
    username=os.getenv('DATABASE_USER'),
    password=os.getenv('DATABASE_PASSWORD'),
    port=os.getenv('DATABASE_PORT')

    engine = create_engine(f'postgresql://{username}:{password}@{host}:{port}/{database_name}')

    offset = 0
    size = 100      #size 500 reccommended by website, smaller value for testing
    while True:
        requestURL = f"https://www.ebi.ac.uk/proteins/api/proteins?offset={offset}&size={size}&isoform=1"

        r = requests.get(requestURL, headers={"Accept" : "application/json"})

        if not r.ok:
            r.raise_for_status()
            sys.exit()

        objList = json.loads(r.text)

        for o in objList:
            protein_id = o.get("accession")
            protein_info, pubs_info_list = get_protein_info(protein_id)

            protein_info.to_sql("PROTEIN_INFO", engine, if_exists='append')
            for pub in pubs_info_list:
                pub.to_sql("PUBLICATION_INFO", engine, if_exists='append')
        
        offset += size
        if offset > r.headers["x-total-results"]:
            break

        break #used for testing


def del_tables(conn):
    cur = conn.cursor()

    cur.execute('''
        DROP TABLE IF EXISTS PROTEIN_INFO;
    ''')

    cur.execute('''
        DROP TABLE IF EXISTS PUBLICATION_INFO;
    ''')

    cur.close()


if __name__ == "__main__":
    conn = init_connect()
    populate_db()

    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM PROTEIN_INFO;""")
    for table in cursor.fetchall():
        print(table)

    del_tables(conn)

