import os
import psycopg2
import requests, sys, json
from get_protein_info import get_protein_info
from sqlalchemy import create_engine
import random

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

    cur.execute('''
        CREATE TABLE IF NOT EXISTS "PROTEIN_INFO" (
            "index" REAL,
            "UNIPROTKB_AC" VARCHAR(20),
            "UNIPROTKB_ID" VARCHAR(20),
            "GENE_NAME" VARCHAR(20),
            "DESCRIPTION" VARCHAR(1000),
            "ENSEMBL" VARCHAR(20),
            "HGNC" VARCHAR(20),
            "PDB" VARCHAR(20),
            "PDB_ID" VARCHAR(20),
            "GTEX" VARCHAR(100),
            "EXPRESSION_ATLAS" VARCHAR(100),
            PRIMARY KEY ("UNIPROTKB_AC")
        );
    ''')

    cur.execute('''
        CREATE TABLE IF NOT EXISTS "PUBLICATION_INFO" (
            "index" REAL,
            "UNIPROTKB_AC" VARCHAR(20),
            "PUBLICATION_ID" VARCHAR(20),
            "PUBLICATION_NAME" VARCHAR(200),
            "AUTHORS" VARCHAR(200),
            "SCORE" REAL,
            PRIMARY KEY ("PUBLICATION_ID", "UNIPROTKB_AC")
        );
    ''')

    cur.close()
    conn.commit()


def populate_db():
    """Populate database with protein information and publication information"""
    host=os.environ['DATABASE_HOST']
    database_name=os.environ['DATABASE_NAME']
    username=os.environ['DATABASE_USER']
    password=os.environ['DATABASE_PASSWORD']
    port=os.environ['DATABASE_PORT']

    engine = create_engine(f'postgresql://{username}:{password}@{host}:{port}/{database_name}')

    offset = 0
    # offset = random.randint(0, 30000)  #used for testing
    size = 500      # size 500 reccommended by website, smaller value for testing
    while True:
        requestURL = f"https://www.ebi.ac.uk/proteins/api/proteins?offset={offset}&size={size}&seqLength=0-100000"
        print("Get successful with offset", offset)
        

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
        if offset > int(r.headers["X-Pagination-TotalRecords"]):
            break

        if offset >= 1000:
            break #used for testing


def del_tables(conn):
    cur = conn.cursor()

    cur.execute('''
        DROP TABLE IF EXISTS "PROTEIN_INFO";
    ''')

    cur.execute('''
        DROP TABLE IF EXISTS "PUBLICATION_INFO";
    ''')

    cur.close()
    conn.commit()


if __name__ == "__main__":
    conn = init_connect()
    populate_db()

    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM PROTEIN_INFO;""")
    for table in cursor.fetchall():
        print(table)

    del_tables(conn)

