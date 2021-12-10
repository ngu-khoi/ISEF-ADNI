#Produce a new dataset with randomized 50alcoholic/50control information
import csv
import re
import os
import random
fileName1 = "full_label_list.txt"
#Find and read file
if os.path.isfile(fileName1):
    print("Files exist")
    File1 = open(fileName1,"r")
    line1 = File1.readline()
    outfile1 = "test.txt"
    outfile2 = "train.txt"
    outfile3 = "validation.txt"
    x1 = open(outfile1, "a", newline='')
    x2 = open(outfile2, "a", newline='')
    x3 = open(outfile3, "a", newline='')
    csv_writer1 = csv.writer(x1)
    csv_writer2 = csv.writer(x2)
    csv_writer3 = csv.writer(x3)
    csv_writer.writerow(line1.replace("\n","").split(","))
    line1 = File1.readline()
    while line1:
        line_details1 = line1.replace("\n","").split(",")
        if random.random() < .8:
            csv_writer1.writerow(line_details1)
        elif random.random() < .9 or :
            csv_writer.writerow(line_details2)
        elif random.random() < .5:
        line1 = File1.readline()
        line2 = File2.readline()
    x.close()
    File1.close()
    File2.close()
else:
    print("File does not exist")