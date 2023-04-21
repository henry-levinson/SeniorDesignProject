import psycopg2
import os
from pandas import DataFrame

class DbHandler():
    def __init__(self, conn):
        self.conn = conn
        self.cur = conn.cursor()
    
    def searchTarget(self, search_string):
        self.cur.execute(f'''SELECT *
                        FROM \"PROTEIN_INFO\"
                        WHERE to_tsvector(\"UNIPROTKB_AC\" || ' ' || \"UNIPROTKB_ID\" || ' ' || \"GENE_NAME\") @@ to_tsquery('{search_string}');''')
        # result = self.cur.fetchall()
        df = self.cur.fetchall()
        #print(df)
        return df
    
    def scanPublications(self, uniprotkb_ac):
        self.cur.execute(f'''SELECT *
                        FROM \"PUBLICATION_INFO\"
                        WHERE to_tsvector(\"UNIPROTKB_AC\" || ' ') @@ to_tsquery('{uniprotkb_ac}');''')
        # result = self.cur.fetchall()
        df = self.cur.fetchall()
        #print(df)
        return df
    
    def scanUserReviews(self, publication_id):
        self.cur.execute(f'''SELECT *
                        FROM \"user_reviews\"
                        WHERE to_tsvector(\"publication_id\" || ' ') @@ to_tsquery('{publication_id}');''')
        # result = self.cur.fetchall()
        df = self.cur.fetchall()
        print(df)
        return df

    def insertUserReview(self, User_ID, Publication_ID, Score, Principal_Findings, Methodology):
        self.cur.execute(f'''INSERT INTO \"user_reviews\" (User_ID, Publication_ID, Score,Principal_Findings, Methodology)
                        VALUES ('{User_ID}', '{Publication_ID}', '{Score}', '{Principal_Findings}', '{Methodology}')
                        ON CONFLICT (User_ID, Publication_ID) DO UPDATE 
                        SET Principal_Findings = excluded.Principal_Findings, 
                            Methodology = excluded.Methodology,
                            Score = excluded.Score;
        ''')
        # update score of publication that user reviewed
        self.updatePublicationInfoTable(Publication_ID)

    def updatePublicationInfoTable(self,Publication_ID):
        self.cur.execute(f'''UPDATE "PUBLICATION_INFO"
                        SET "SCORE" = ROUND(
                                    CAST(
                                        (SELECT avg(score)
                                        FROM user_reviews
                                        WHERE publication_id = '{Publication_ID}'
                                        GROUP BY publication_id
                                        )
                                    
                                    AS numeric), 1)
                        WHERE 'PUBLICATION_ID' = '{Publication_ID}';''')

        self.conn.commit()

if __name__ == "__main__":
    conn = psycopg2.connect(
        host="localhost",
        database="flask_db",
        # user=os.environ['DB_USERNAME'],
        # password=os.environ['DB_PASSWORD']
        user = "postgres",
        password = "123"
    )

    testHandler = DbHandler(conn)
    print("searchTarget results are:")
    testHandler.scanUserReviews("16141072 ")
    #testHandler.insertUserReview("id1", "Publication_ID1", "2.0", "findings 1", "method1-1")
    #testHandler.insertUserReview("id2", "Publication_ID1", "4.0", "findings 2", "method1-2")
    #testHandler.insertUserReview("id3", "Publication_ID2", "5.8", "findings 3", "method1-3")