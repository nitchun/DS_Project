import re
import nltk
import os
import sqlite3
#____________________ CONNECT TO THE DB ___________________________________
conn = sqlite3.connect('knowledgeBase.db')# db name
c = conn.cursor()
#_____________________EMPTY LISTS TO STORE WORDS AND THIER SCORES___________________________
word_list = []
val_list = []
#_________________LIST OF NOT SO IMPORTANTS PARTS OF SPEECH TAGS_____________________________
not_imp = ['IN', 'CC', ',', '.', ':', '(', ')', ':', 'TO', 'VBZ', 'DT', 'NNP']
#________________________RETRIEVE RECORDS FROM WORDvALS TABLE____________________________________
c.execute("SELECT * FROM wordVals")
data = c.fetchall()
#__________________________PUT THE RETRIEVED DATA (RETURNED AS A LIST OF TUPLES(WORD, VAL)INTO INDIVIDUAL LISTS_________________________
for each in data:
    word_list.append(str(each[0]))
    val_list.append(str(each[1]))

#_____________________MODULE TO READ INPUT REVIEWS AND SCORE THEM BASED ON POLARITY____________________________
def get_data():
    print 'creating writer............'
    #______________OPEN FILE WRITER_______________________________________
    combined_writer = open("villagevoice_review_scores.txt", "w")
    #_______________FILE TO READ______________________________________________
    file = r"C:\Users\Nithya\Downloads\Data Science\Project\Final stuff\combined review text\combined_villagevoice_reviews.txt"
    print 'creating reader............'
    #________________OPEN FILE READER____________________________________________
    text_reader = open(file, "r")
    print 'reading all reviews............'
    #___________READ THE ENTIRE FILE AS A STRING________________________________
    reviews = text_reader.read()
    #print reviews
    print 'reading all movie names............'
    #___________RETRIEVE MOVIE NAMES INTO A LIST_________________________________
    movie_list = re.findall('File_name: (.*)', reviews)
    movie_list.pop(-1)
    print 'Length of movies : ', len(movie_list)
    print movie_list
    print 'reading all release dates............'
    #_____________RETRIEVE MOVIE RELEASE DATES INTO A LIST_______________________________
    release_list = re.findall('Release date: (.*)', reviews)
    print 'Length of dates : ', len(release_list)
    print 'putting reviews into list............'
    #______________FIND REVIEW TEXT AND PUT INTO A LIST_____________________
    review_list = re.findall("Review:([\s\S]*?)File_name:", reviews)
    print 'Length of reviews : ', len(review_list)
    #________________LOOP THROUGH THE LIST AND PROCESS EACH REVIEW________________
    for each in review_list:
        #print "processing" + str(movie_list[review_list.index(each)])+ " review"
        #_______STORE REVIEW SCORE RETURNED BY THE PROCESSOR METHOD________________
        score  = processor(each)
        #print "score for "+ str(movie_list[review_list.index(each)]) + " is : "+ str(score)
        #____________WRITE TO OUTPUT FILE___________________
        combined_writer.write("Movie: " + movie_list[review_list.index(each)]+"       Score: "+str(score)+"       Release :" + release_list[review_list.index(each)]+"\n")
        #combined_writer.write("Score: "+str(score)+"\n")
        print '1 record added............contents written to file'
    #_________________CLOSE READER____________________
    text_reader.close()
    #_________________CLOSE WRITER______________________
    combined_writer.close()

def processor(data):
    try:
        #_____________LIST TO STORE ITEMS TO BE REMOVED___________________
        remove_from_tagged = []
        #______________VARIABLE TO STORE FINAL SCORE OF THE REVIEW_______________
        pol_score = 0
        #_____________SPLIT INPUT REVIEW INTO TOKENS(WORDS)________________
        tokenized = nltk.word_tokenize(data)
        print 'tokenized....'
        #_____________TAG TOKENS WITH PARTS OF SPEECH LABELS(NOUN, ADJECTIVE......ETC)__________________
        tagged = nltk.pos_tag(tokenized)
        print 'tokens tagged with parts of speech labels......'
        #______________LOOP THROUGH EACH TAGGED TOKEN AND COLLECT ALL THE UNIMPORTANT TOKENS INTO A LIST______________
        print 'removing not so important tokens.........'
        for each in tagged:
            if each[1] in not_imp:
                remove_from_tagged.append(each)
        #_________________REMOVE THE COLLECTED UMIMPORTANT TOKENS_______________________
        for each in remove_from_tagged:
            tagged.remove(each)
        print 'removed useless tokens'
        #_________________COLLECT WORDS IN REVIEW THAT DESCRIBE SOMETHING ABOUT DIFFERENT ENTITIES IN THE MOVIE INTO A LIST ____________________
        descriptives = re.findall(r'\(\'(\w*)\',\s\'JJ\w?\'', str(tagged))
        #____________________LOOP THROUGH EACH DESCRIPTIVE WORD AND INSERT INTO DATABASE INTO KNOWLEDGEbASE TABLE_______________________
        for each in descriptives:
            print each
            c.execute("INSERT INTO knowledgeBase (des_words) VALUES (?)", (each,)) # insert into table descriptives in knowledgeBase db
            conn.commit()
            #__________IF DESCRIPTIVE WORD IS IN wordVal TABLE, INCREMENT SCORE BY CORRESPONDING VALUE_________________________
            if each in word_list:
                #print each + " is in the db"
                idx = word_list.index(each)
                #print "word :"+each+"  val :"+val_list[idx]
                pol_score += int(val_list[idx])
        #_______RETURN FINAL POLARITY SCORE___________________
        return pol_score
       
    except Exception, e:
        print('failed in the first try of processor')
        print(str(e))
#__________call get_data() method to initilaize the program___________________________
get_data()
