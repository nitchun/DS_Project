import sqlite3


conn = sqlite3.connect('knowledgeBase.db')
c = conn.cursor()

def createDB():
    c.execute("CREATE TABLE knowledgeBase(descriptive TEXT)")
