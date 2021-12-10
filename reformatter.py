"""
This reformatter consists of a reduction of data from being longitudinal to consisting of just baseline data for each patient, 
extraction of images from directory trees into images subfolder, and the renaming of image files.

VARIABLES: destination should be the ADNI data folder. imageFolder is desired location for images
"""
import os, itertools, shutil

def remove(destination):
	for filename in os.listdir(destination):
		for filename1 in os.listdir(destination + filename):
			#for filename2 in os.listdir(destination + filename + "/" + filename1):
			"""
			if len(os.listdir(destination + filename + "/" + filename1)) > 1:
				removeCount = len(os.listdir(destination + filename + "/" + filename1))
				listOfFiles = os.listdir(destination + filename + "/" + filename1)
				for i in range(1, removeCount):
					shutil.rmtree(destination + filename + "/" + filename1 + "/" + listOfFiles[i])
			"""
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

def rename(destination, imageFolder):
	filenames = []
	for filename in os.listdir(destination):
		filenames.append(filename + ".nii")
	imagefiles = []
	for filename in os.listdir(imageFolder):
		imagefiles.append(filename)
	for i in range(len(filenames)):
		os.rename(imageFolder + imagefiles[i], imageFolder + filenames[i])

#MAIN
remove(r"D:/ADNI_Project/ADNI/")
#move(r"D:/ADNI_Project/ADNI/",r"D:/ADNI_Project/images/")
#rename(r"D:/ADNI_Project/ADNI/", r"D:/ADNI_Project/images/")