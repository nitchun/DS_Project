import time
import urllib2
from urllib2 import urlopen
import re
from cookielib import CookieJar
import os
import sqlite3

cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

conn = sqlite3.connect('knowledgeBase.db')
c = conn.cursor()
query = "SELECT * FROM wordVals WHERE value =?"
c.execute(query, [(-1)])
data = c.fetchall()
#data = [('neutral',0)]#,('bad',-1),('neutral',0))
start_words = []
for each in data:
        start_words.append(str(each[0]))
        startingWordVal = -1
print start_words       
synArray = []

def main():
    for startingWord in start_words:
        print startingWord
        try:
            page = 'http://thesaurus.com/browse/'+startingWord+'?s=t'
            sourceCode = opener.open(page).read()

            try:
                synoNym = sourceCode.split('<div class="synonym-description">')
                x = 1
                while x < len(synoNym):
                    try:
                        synoNymSplit = synoNym[x].split('<div class="synonyms-horizontal-divider"></div>')[0]
                        synoNyms = re.findall(r'text\">(\w*?)</span>', synoNymSplit)
                        print synoNyms
                        for eachSyn in synoNyms:
                            query = "SELECT * FROM wordVals WHERE word =?"
                            c.execute(query, [(eachSyn)])
                            data = c.fetchone()#if there are multiple get only one

                            if data is None:
                                print 'not there in db yet, lets add it'
                                c.execute("INSERT INTO wordVals (word, value) VALUES (?,?)",
                                         (eachSyn, startingWordVal))
                                conn.commit()
                            else:
                                """if str(data[1]) != startingWordVal:
                                    print 'already there but different value'
                                    c.execute("INSERT INTO wordVals (word, value) VALUES (?,?)",
                                         (eachSyn, startingWordVal))
                                    conn.commit()"""
                                print 'word already here!'
                    except Exception, e:
                        print str(e)
                        print 'failed in 3rd try'
                    x += 1
            except Exception, e:
                print str(e)
                print 'failed in 2nd try'
        except Exception, e:
            print str(e)
            print 'failed in 1st try'
                                
main()
#c.execute("INSERT INTO doneSyns (word) VALUES (?)",
          #(startingWord,))
#conn.commit()
