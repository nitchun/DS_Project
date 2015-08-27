import os
import re
combined_writer = open("final_award_scores.txt", "w", encoding = "utf8")

# file reader to open file for reading
file = r"C:\Users\Nithya\Downloads\Data Science\Project\Final stuff\code\combined_award_scores.txt"
text_reader = open(file, "r", encoding="utf8")

#for each in text_reader:
line = text_reader.read()
m = re.findall(r"movie: ([^']+).*score:(.+)']", line)
#s = re.findall(r"score:(.+)']", line)
print(len(m))
#print(len(s))
for each in m:
    #print(each, str(s[m.index(each)]))
    combined_writer.write(str(each[0]))
    combined_writer.write('\t')
    combined_writer.write(str(each[1]))
    combined_writer.write('\n')

combined_writer.close()
text_reader.close()
