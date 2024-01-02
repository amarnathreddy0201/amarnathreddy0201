import logging
from datetime import datetime
import os

import boto3

logging.basicConfig(level=logging.INFO, filename='sample.log', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(filename)s - %(lineno)d')
logger = logging.getLogger(__name__)


class BucketS3:

    def __init__(self,bucket_name):
        
        self.s3_resource  = boto3.resource('s3')
        self.bucket_name = bucket_name
        self.folders_name_list=[]

        self.bucket = None
        

    def check_bucket_and_create(self)->boto3:
        """
        Chek the bucket exist or not.
        If bucket not exist create.
        """
        try:
            self.bucket = self.s3_resource.Bucket(self.bucket_name)

            if not self.bucket.creation_date:
                logger.info(f"bucket not exist and bucket created : {self.bucket_name}")
                self.bucket =  self.s3_resource.create_bucket(Bucket=self.bucket_name,
                CreateBucketConfiguration={'LocationConstraint':'ap-south-1'})

            logger.info(self.bucket.name)

            return self.bucket
        except Exception as error:
            logger.error(error)
    
    def chek_folder_path_in_bucket(self,folder_path:str)->str:
        """ Check folder path 
        If folder path not exist create and return path
        :
        """
        try:
            objects = self.bucket.objects.filter(Prefix=folder_path+"/")

            s3_object = [data.key for data in objects]

            if folder_path not in s3_object:
                self.bucket.put_object(Bucket=self.bucket_name, Key=folder_path+"/")
                logger.info("folder path created")
            else:
                logger.info("Data already exists")
            return folder_path
        except Exception as error:
            logger.error(error)

    
    def insert_data(self,folder_path:str , file_name:str , data)->None:
        """
        Creating file and inserting data.
        Input : 
            1) folder_path : str
            2) file_name : str
        Return :
            None
        """
        try:
            file_key_to_check = folder_path+"/"+file_name

            file_exist = False
           
            for obj in self.bucket.objects.filter(Prefix= file_key_to_check):
                logger.info(obj)
                find_file_name = obj.key.split('/')[-1]
                if(find_file_name == file_name):
                    
                    file_exist = True
                    break

            if file_exist:
                logger.info("exist")

            else:
                response = self.bucket.put_object(Bucket= self.bucket_name,Key =file_key_to_check,Body=data)
                logger.info(response)
                logger.info("not exist")
        except Exception as error:
            logger.error(error)

    def retriving_data_from_bucket(self,folder_path)->None:
        """
        Get the total data from bucket based on path
        Input:
            1) folder_path : str
        Return:
            None
        """
        folder = folder_path+"/"
        objects = self.bucket.objects.filter(Prefix= folder)
       
        folder_files = [data.key for data in objects] # getting folder and files in a folder.
        
        os.makedirs(folder_files[0], exist_ok=True) # Create folder

        # filter based on folder names 
        for i in range(0,len(folder_files)-1):
            objects = self.bucket.objects.filter(Prefix= folder_files[i+1])
            
            for data in objects:
                saving_files = os.getcwd()+"\\"+data.key.replace("/","\\")
                with open(saving_files,"w") as file:
                    pass
                self.bucket.download_file(data.key,saving_files)


if __name__ =="__main__":

    year_folder = str(datetime.today().year)

    # Buckets created : 1) images-uploading 2)alluviumdata 3) alluviumdata
    creating_bucket = BucketS3("amardata")#"images-uploading") # Unique name

    bucket = creating_bucket.check_bucket_and_create()

    # Creating folder in aws with year and type of work
    folder = str(year_folder) + "/reddy"

    folder_path = creating_bucket.chek_folder_path_in_bucket(folder)

    data = b"jjirkngkjrn"
    file_name = "text2.txt"

    creating_bucket.insert_data(folder_path,file_name,data)
    creating_bucket.retriving_data_from_bucket(folder_path)


    # Creating folder in aws with year and type of work(ex : text or pi)
    folder = str(year_folder) + "/pi"

    folder_path = creating_bucket.chek_folder_path_in_bucket(folder)

    data = b"jjirkngkhghjhwhjebgujghlhbjerlgjkb;jrn"
    file_name = "text2.txt"

    creating_bucket.insert_data(folder_path,file_name,data)

    creating_bucket.retriving_data_from_bucket(folder_path)
