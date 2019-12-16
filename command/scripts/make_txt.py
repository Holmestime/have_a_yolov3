from os import listdir, getcwd
from os.path import join
import os


TRAIN_PATH = "./ImageSets/Main/train.txt"
VAL_PATH = "./ImageSets/Main/val.txt"
TRAIN_FOLDER = "./train/"
VAL_FOLDER = "./val/"

if __name__ == '__main__':

    
    train_path=TRAIN_PATH
    val_path=VAL_PATH

    file_list=os.listdir(TRAIN_FOLDER)
    train_file=open(train_path,'w')
    val_file=open(val_path,'w')
    
    for file_obj in file_list:

        file_path=os.path.join(TRAIN_FOLDER,file_obj)

    
        file_name,file_extend=os.path.splitext(file_obj)
		
        train_file.write(file_name+'\n')

    file_list = os.listdir(VAL_FOLDER)
    for file_obj in file_list:

        file_path=os.path.join(VAL_FOLDER,file_obj)

    
        file_name,file_extend=os.path.splitext(file_obj)
        
        val_file.write(file_name+'\n')


    train_file.close()

    val_file.close()
