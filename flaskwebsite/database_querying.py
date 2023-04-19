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
                        WHERE to_tsvector(\"UNIPROTKB_AC\" || ' ' || \"UNIPROTKB_ID\" || ' ' || \"GENE NAME\") @@ to_tsquery('{search_string}');''')
        # result = self.cur.fetchall()
        df = self.cur.fetchall()
        #print(df)
        return df

    def insertUserReview(self, User_ID, Publication_ID, Score, Principal_Findings, Methodology):
        self.cur.execute(f'''INSERT INTO \"USER_REVIEWS\" (User_ID, Publication_ID, Score,Principal_Findings, Methodology)
                        VALUES ('{User_ID}', '{Publication_ID}', '{Score}', '{Principal_Findings}', '{Methodology}')
                        ON CONFLICT (User_ID, Publication_ID) DO UPDATE 
                        SET Principal_Findings = excluded.Principal_Findings, 
                            Methodology = excluded.Methodology,
                            Score = excluded.Score;
        ''')
        # update score of publication that user reviewed
        self.updatePublicationTable(Publication_ID)

    def updatePublicationTable(self,Publication_ID):
        self.cur.execute(f'''UPDATE publication_table
                        SET Score = ROUND(
                                    (SELECT avg(score)
                                    FROM user_reviews
                                    WHERE publication_id = '{Publication_ID}'
                                    GROUP BY publication_id), 1)
                        WHERE publication_id = '{Publication_ID}';''')

        conn.commit()

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
    testHandler.searchTarget("hello")
    testHandler.insertUserReview("id1", "Publication_ID1", "2.0", "findings 1", "method1-1")
    testHandler.insertUserReview("id2", "Publication_ID1", "4.0", "findings 2", "method1-2")
    testHandler.insertUserReview("id3", "Publication_ID2", "5.8", "findings 3", "method1-3")