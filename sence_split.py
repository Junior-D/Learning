# -*- coding: utf-8 -*-

import os
import csv
import json
import shutil

image_path = './ai_challenger_scene_train_20170904/scene_train_images_20170904/'
label_path = './ai_challenger_scene_train_20170904/scene_train_annotations_20170904.json'
csv_path = './ai_challenger_scene_train_20170904/scene_classes.csv'
folder_path = './sence_split'  # set the new folder address
os.mkdir(folder_path)	# generate the new folder

def sence_split(image_path = image_path, label_path = label_path, folder_path = folder_path):
	csv_dict = {}
	csv_file = file(csv_path, 'rb')
	data_csv = csv.reader(csv_file)
	for line in data_csv:
		csv_dict[int(line[0])] = line[1].decode('utf-8').encode('gb2312') 
	csv_file.close()
	
	data_dict = {}
	with open(label_path, 'r') as f:
		label_list = json.load(f)

	for item in label_list:
		data_dict[item['image_id']] = int(item['label_id'])

	index = 0 # number of completed
	for i in range(0, 80):
		folder_new = folder_path + '/' + str(i) + str(csv_dict[i])	# Set the subfolder path
		image_copy = []	# Crate a list to save the image_name that to be copied
		for item in label_list:
			if int(item['label_id']) == i:
				image_copy.append(item['image_id'])

		os.mkdir(folder_new)	# Generate the subfolder 
		for item in image_copy:
			shutil.copy(image_path + str(item), folder_new )	# Copy image to new folder

		index += len(image_copy)
		print i, len(image_copy), index, len(data_dict)

if __name__ == '__main__':
	sence_split()