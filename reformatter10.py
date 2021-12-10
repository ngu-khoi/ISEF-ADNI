"""
This reformatter consists of removing all files that are not preprocessed with the condition "MPR__GradWarp__B1_Correction__N3__Scaled."

VARIABLES: destination should be the ADNI data folder. imageFolder is desired location for images
"""
import os, itertools, shutil

def action(destination):
	for filename in os.listdir(destination):
		for filename1 in os.listdir(destination + filename):
			if "MPR__GradWarp__B1_Correction__N3__Scaled" not in filename1:
				shutil.rmtree(destination + filename + "/" + filename1)

def remove(destination):
	for filename in os.listdir(destination):
		for filename1 in os.listdir(destination + filename):
			if len(os.listdir(destination + filename)) > 1:
				removeCount = len(os.listdir(destination + filename))
				listOfFiles = os.listdir(destination + filename)
				for i in range(1, removeCount):
					shutil.rmtree(destination + filename + "/" + listOfFiles[i])

def move(destination, imageFolder):
    all_files = []
    for root, _dirs, files in itertools.islice(os.walk(destination), 1, None):
        for filename in files:
            all_files.append(os.path.join(root, filename))
    for filename in all_files:
        shutil.copy(filename, imageFolder)

def rename(imageFolder):
	filenames = []
	for filename in os.listdir(imageFolder):
		os.rename(imageFolder + filename, imageFolder + filename[5: 15] + ".nii")

#MAIN
#action(r"D:/ADNI_Project/ADNI/")
#remove(r"D:/ADNI_Project/ADNI/")
#move(r"D:/ADNI_Project/ADNI/",r"D:/ADNI_Project/images/")
rename(r"D:/ADNI_Project/images/")