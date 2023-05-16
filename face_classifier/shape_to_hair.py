import os
import random

project_dir = '/home/alonso/brproject/face_classifier/'
shape_file = open(project_dir+'faceshape', 'r')
shape = shape_file.read()
gender = 'male'
file_dir = project_dir+'styles/'+gender+'/'+shape+'/'
hair_file = random.choice(os.listdir(file_dir))
print(file_dir+hair_file)
