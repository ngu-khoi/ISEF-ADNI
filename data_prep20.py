import os, itertools, shutil, csv


def prep(root, neural_network):
	with open('./patient_diagnosis_original.csv') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		line_count = 0
		for row in csv_reader:
				if line_count == 0:
					line_count += 1
				else:
					try:
						if row[1] == "AD":
							shutil.copy(root + row[0] + ".nii", neural_network + "1")
						elif row[1] == "CN":
							shutil.copy(root + row[0] + ".nii", neural_network + "0")
					except:
						print(row[0])
					line_count += 1


def missing(root):
	names=[]
	names1=[]
	with open('./patient_diagnosis_original.csv') as csv_file:
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
prep(r"D:/ADNI_Project/images_preprocessed_2/", r"D:/ADNI_Project/neural_network_processed2/")
#print(missing(r"D:/ADNI_Project/images_proprocessed_1/"))