# module to assign a movie a score if there are award winners
import os
import re

award_winners = []
artists_list = []

# file writer to write to a single file
combined_writer = open("combined_award_scores.txt", "w", encoding = "utf8")

# file reader to open file for reading
file = r"C:\Users\Nithya\Downloads\Data Science\Project\Final stuff\award_list.txt"
text_reader = open(file, "r", encoding="utf8")

#read contents to variable text as a string
for line in text_reader:
    line_elements = line.split('\t')
    award_winners.append(line_elements[0])

text_reader.close()

file = r"C:\Users\Nithya\Downloads\Data Science\Project\Final stuff\award.txt"
text_reader = open(file, "r", encoding="utf8")

for line in text_reader:
    #line = text_reader.readline()
    line_elements = line.split('\t')
    line_elements[0] = 'movie: ' + str(line_elements[0])
    line_elements[-1] = line_elements[-1].strip()
    artists_list.append(line_elements)
    
checklist = []
movie = ""
for each in artists_list:
    x = 0
    if each[0] != movie:
        checklist[:] = []
        movie = each[0]
        score = 0
        #print('movie: ', movie , 'score :', str(score))
    for single in each:
        if single in award_winners:
            if single not in checklist:
                #print('scored entry: ',movie, single)
                score += 1
                #print(score)
                checklist.append(single)
            
    each.append('score:' + str(score))
    combined_writer.write(str(each))
    combined_writer.write('\n')
#print(len(artists_list))
print ("Text extraction done !!!")
combined_writer.close()
text_reader.close()
