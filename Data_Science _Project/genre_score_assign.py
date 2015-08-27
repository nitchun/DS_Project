# module to assign a movie a score if there are award winners
import os
import re

all_lines_list = []
artists_list = []

# file writer to write to a single file
combined_writer = open("genre_scores.txt", "w", encoding = "utf8")

# file reader to open file for reading
file = r"C:\Users\Nithya\Desktop\new  2.txt"
text_reader = open(file, "r", encoding="utf8")

#read contents to variable text as a string
for line in text_reader:
    line_elements = line.split('\t')
    line_elements[0] = line_elements[0].strip()
    line_elements[1] = line_elements[1].strip()
    all_lines_list.append(line_elements)

text_reader.close()
#print(all_lines_list)
first = "$6,260"
genre_scores = []
n = 0
avg = 0
nom =1
score_sum = 0
for each in all_lines_list:
    #print(each)
    if(all_lines_list.index(each) == len(all_lines_list) - 1):
        avg = round(score_sum / n, 9)
        genre_scores.append(avg)
    if each[0] != first:
        nom += 1
        if n !=0:
            avg = round(score_sum / n, 9)
        print('avg is : ', str(score_sum)+'/'+str(n)+'= '+str(avg))
        print()
        print('new: ',each[0], each[1])
        genre_scores.append(avg)
        first = each[0]
        n = 1
        score_sum = eval(each[1])
        
        
    else:
        print('same :',each[0], each[1])
        n += 1
        score_sum += int(each[1])
print(nom)        
print(len(genre_scores))
for each in genre_scores:
    combined_writer.write(str(each))
    combined_writer.write('\n')
combined_writer.close()

