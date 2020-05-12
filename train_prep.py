import csv
import os,shutil


path ='./C1-P1_Train Dev_fixed/C1-P1_Train/'
moveto = './train_data/'

with open('./C1-P1_Train Dev_fixed/train.csv',newline='') as csvfile:

	rows = csv.reader(csvfile)
	for row in rows :
		if row[0] == 'image_id':
			continue
		str1 = row[0]
		str2 = row[1]
		src = path+str1
		dst = moveto+str2
		shutil.move(src,dst)

