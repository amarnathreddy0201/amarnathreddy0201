import os
import pandas as pd
from tqdm import tqdm

def function():
    excel_file_path = r"train.csv"
    
    # Specify the columns you want to read
    columns_to_read = ['file_name', 'label']
    
    # Read the Excel file, selecting only the specified columns
    train_df = pd.read_csv(excel_file_path, usecols=columns_to_read)
    
    
    
    # loading training images
    train_img = []
    for img_name,label in zip(train_df['file_name'],train_df['label']):
        dir ="test1"+"/"+str(label)
        os.makedirs(dir, exist_ok=True)
    
        source_path = "train/"+img_name
        if os.path.exists(source_path):
            destination_path = os.path.join(dir, img_name)
            # # Rename the file
            os.rename(source_path, destination_path)

def function1():
    import os
    import pandas as pd
    # from tqdm import tqdm
    
    excel_file_path = r"train.csv"
    
    # Specify the columns you want to read
    columns_to_read = ['file_name', 'label']
    
    # Read the Excel file, selecting only the specified columns
    train_df = pd.read_csv(excel_file_path, usecols=columns_to_read)
    
    
    
    # loading training images
    train_img = []
    i=0
    for img_name,label in zip(train_df['file_name'],train_df['label']):
        if i%100==0:
            dir ="test1"+"/"+str(label)
        else:
            dir ="train1"+"/"+str(label)
        os.makedirs(dir, exist_ok=True)
    
        source_path = "train/"+img_name
        if os.path.exists(source_path):
            destination_path = os.path.join(dir, img_name)
            # # Rename the file
            os.rename(source_path, destination_path)
            i+=1
        


        

