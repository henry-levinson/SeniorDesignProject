import os
import psycopg2

conn = psycopg2.connect(
        host="localhost",
        database="flask_db",
        # user=os.environ['DB_USERNAME'],
        # password=os.environ['DB_PASSWORD']
        user = "postgres",
        password = "123")

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute('DROP TABLE IF EXISTS books;')
cur.execute('CREATE TABLE books (id serial PRIMARY KEY,'
                                 'title varchar (150) NOT NULL,'
                                 'author varchar (50) NOT NULL,'
                                 'pages_num integer NOT NULL,'
                                 'review text,'
                                 'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                 )

cur.execute('DROP TABLE IF EXISTS protein_information;')
cur.execute('CREATE TABLE protein_information (id serial PRIMARY KEY,'
                                                'uniProt_accession varchar (150) NOT NULL,'
                                                'uniProt_id varchar (150) NOT NULL,'
                                                'primary_gene_name varchar (150) NOT NULL);'
                                                )

cur.execute('DROP TABLE IF EXISTS publication_table;')
cur.execute('''CREATE TABLE publication_table (id serial PRIMARY KEY,
                                                UniProtKB_AC text ,
                                                Publication_ID text UNIQUE,
                                                Publication_Name text,
                                                Authors text,
                                                Score decimal);''')

cur.execute('DROP TABLE IF EXISTS user_reviews;')
cur.execute('''CREATE TABLE user_reviews (id serial PRIMARY KEY,
                                            User_ID text,
                                            Publication_ID text,
                                            Score decimal,
                                            Principal_Findings text,
                                            Methodology text,
                                            UNIQUE(User_ID, Publication_ID));''')

cur.execute('''INSERT INTO publication_table (UniProtKB_AC,
                                                Publication_ID,
                                                Publication_Name ,
                                                Authors ,
                                                Score)
                VALUES(
                'UniProtKB_AC1',
                'id_test1',
                'name1',
                'author1',
                3.7);'''
            )

cur.execute('''INSERT INTO publication_table (UniProtKB_AC,
                                                Publication_ID,
                                                Publication_Name ,
                                                Authors ,
                                                Score)
                VALUES(
                'UniProtKB_AC1',
                'id_test2',
                'name2',
                'author2',
                3.9);'''
            )

cur.execute('''INSERT INTO publication_table (UniProtKB_AC,
                                                Publication_ID,
                                                Publication_Name ,
                                                Authors ,
                                                Score)
                VALUES(
                'UniProtKB_AC2',
                'id_test3',
                'name33',
                'author32',
                4.8);'''
            )

# Insert data into the table

cur.execute('INSERT INTO protein_information (uniProt_accession, uniProt_id, primary_gene_name)'
            'VALUES (%s, %s, %s)',
            ('1hello1',
             'id1',
             'gene1')
            )

cur.execute('INSERT INTO protein_information (uniProt_accession, uniProt_id, primary_gene_name)'
            'VALUES (%s, %s, %s)',
            ('hello',
             'id1',
             'gene1')
            )

cur.execute('INSERT INTO protein_information (uniProt_accession, uniProt_id, primary_gene_name)'
            'VALUES (%s, %s, %s)',
            ('hello2',
             'hello',
             'gene1')
            )

cur.execute('INSERT INTO protein_information (uniProt_accession, uniProt_id, primary_gene_name)'
            'VALUES (%s, %s, %s)',
            ('hiii',
             'test',
             'hello')
            )


cur.execute('INSERT INTO books (title, author, pages_num, review)'
            'VALUES (%s, %s, %s, %s)',
            ('A Tale of Two Cities',
             'Charles Dickens',
             489,
             'A great classic!')
            )


cur.execute('INSERT INTO books (title, author, pages_num, review)'
            'VALUES (%s, %s, %s, %s)',
            ('Anna Karenina',
             'Leo Tolstoy',
             864,
             'Another great classic!')
            )

conn.commit()

cur.close()
conn.close()