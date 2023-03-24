import psycopg2

conn = psycopg2.connect(
        host="localhost",
        database="flask_db",
        # user=os.environ['DB_USERNAME'],
        # password=os.environ['DB_PASSWORD']
        user = "postgres",
        password = "123")
cur = conn.cursor()

def searchTarget(search_string):
    cur.execute(f'''SELECT uniProt_accession, uniProt_id, primary_gene_name
                    FROM protein_information
                    WHERE to_tsvector(uniProt_accession || ' ' || uniProt_id || ' ' || primary_gene_name) @@ to_tsquery('{search_string}');''')
    result = cur.fetchall()
    print(result)




# def insertRow(publication_id, principal_findings, methodology, score):
#     cur.execute(f'''INSERT INTO publication_table (Publication_ID, Principal_findings, Methodology, Score)
#                     VALUES ('{publication_id}', '{principal_findings}', '{methodology}', '{score}')
#                     ON CONFLICT (Publication_ID) DO UPDATE 
#                     SET Principal_findings = excluded.Principal_findings, 
#                         Methodology = excluded.Methodology,
#                         Score = excluded.Score;
#     ''')
    
#     conn.commit()

def insertUserReview(User_ID, Publication_ID, Score, Principal_Findings, Methodology):
    cur.execute(f'''INSERT INTO user_reviews (User_ID, Publication_ID, Score,Principal_Findings, Methodology)
                    VALUES ('{User_ID}', '{Publication_ID}', '{Score}', '{Principal_Findings}', '{Methodology}')
                    ON CONFLICT (User_ID, Publication_ID) DO UPDATE 
                    SET Principal_Findings = excluded.Principal_Findings, 
                        Methodology = excluded.Methodology,
                        Score = excluded.Score;
    ''')

    # TODO: update publication table score
    # cur.execute(f'''UPDATE publication_table
    #                 SET Score = ''')

    conn.commit()

if __name__ == "__main__":
    print("searchTarget results are:")
    searchTarget("hello")

    insertUserReview("id1", "Publication_ID1", "2.0", "findings 1", "method1-1")
    insertUserReview("id2", "Publication_ID1", "4.0", "findings 2", "method1-2")
    insertUserReview("id3", "Publication_ID2", "5.8", "findings 3", "method1-3")
    cur.execute(f'''select AVG(score) from publication_table WHERE uniprotkb_ac = 'UniProtKB_AC1' GROUP BY uniprotkb_ac;''')
    print(cur.fetchall())

