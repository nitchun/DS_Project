# module used for creating wordVaks and doneSyns tables
# doneSyns table is sed to store all the words generated to compare and avoid crawling web again anf again
import sqlite3

conn = sqlite3.connect('knowledgeBase.db')# db name
c = conn.cursor()

def createDB():
    #c.execute("CREATE TABLE wordVals (word TEXT, value TEXT)")
    #c.execute("CREATE TABLE doneSyns (word TEXT)")
    c.execute("INSERT INTO wordVals (word, value) VALUES (?,?)",
                                      ('good', 1))
    c.execute("INSERT INTO wordVals (word, value) VALUES (?,?)",
                                      ('bad', -1))
    c.execute("INSERT INTO wordVals (word, value) VALUES (?,?)",
                                      ('neutral', 0))
    conn.commit()
                            

createDB()
