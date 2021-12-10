import os, itertools, shutil, csv


def prep(root, neural_network):
	with open('./patient_diagnosis.csv') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		line_count = 0
		for row in csv_reader:
				if line_count == 0:
					line_count += 1
				else:
					try:
						if int(row[1]) == 1:
							shutil.copy(root + row[0] + ".nii", neural_network + "1")
						elif int(row[1]) == 0:
							shutil.copy(root + row[0] + ".nii", neural_network + "0")
					except:
						print(row[0])
					line_count += 1


def missing(root):
	names=[]
	names1=[]
	with open('./patient_diagnosis.csv') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		line_count = 0
		for row in csv_reader:
				if line_count == 0:
					line_count += 1
				else:
					names1.append(row[0])
	for name in os.listdir(root):
		names.append(name[0:10])
	
	names=set(names)
	names1=set(names1)

	return [list(names-names1)]
#main
prep(r"D:/ADNI_Project/images_unprocessed/", r"D:/ADNI_Project/neural_network_unprocessed/")
#print(missing(r"D:/ADNI_Project/images_proprocessed_1/"))