import os

path = r"C:\Users\Nithya\Downloads\Data Science\Project\Final stuff\movies-data\movies-data-v1.0\reviews\text_reviews\www.nytimes.com - Copy"
in_files = os.listdir(path)

# file wrier to write to a single file
combined_writer = open("combined_nytimes_reviews.txt", "w", encoding = "utf8")

for each_file in in_files:
    # extract file name and write it to file
    combined_writer.write("File_name: " + str(each_file[0:each_file.find(".")]) + "\n")

    #file reader
    file = os.path.join(path, each_file)
    # file reader to open file for reading
    text_reader = open(file, "r", encoding="utf8")

    #read contents to variable text as a string
    text = text_reader.read()
    for item in text.split("</text>"):
        if "<text>" in item:
            combined_writer.write("Review: "+str(item[item.find("<text>")+len("<text>"): item.find("</text>")])+"\n")
        elif "<date>" in item:
            combined_writer.write("Release date: "+str(item [ item.find("<date>")+len("<date>") : item.find("</date>") ]+ "\n\n"))
    text_reader.close()

combined_writer.close()
print ("Text extraction done !!!")
