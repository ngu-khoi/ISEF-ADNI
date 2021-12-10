"""
This reformatter renames preprocessed "MPR__GradWarp__B1_Correction__N3__Scaled" to consist of just subject name.

VARIABLES: destination should be the ADNI data folder. imageFolder is desired location for images
"""
import os, itertools, shutil

def rename(imageFolder):
	filenames = []
	for filename in os.listdir(imageFolder):
		os.rename(imageFolder + filename, imageFolder + filename[4: 14] + ".nii")
#MAIN
rename(r"D:/ADNI_Project/images_preprocessed_2/")