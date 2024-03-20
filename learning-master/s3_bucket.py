"""Saving the data into S3 bucket using Python code. """

# 1st standard packages
import os
import json
import logging

# 2nd standard packages
# if you import your local package.
# 3rd standard packages
import boto3


logger = logging.getLogger(__name__)


class BucketS3:
    def __init__(self, bucket_name):
        self.s3_resource = boto3.resource(
            "s3",
        )

        self.bucket_name = bucket_name
        self.folders_name_list = []

        self.bucket = None

    def check_bucket_and_create(self) -> boto3:
        """
        Chek the bucket exist or not.
        If bucket not exist create.
        Input : None
        Return : bucket(If you want change data we will do that with bucker resource.)
        """
        try:
            self.bucket = self.s3_resource.Bucket(self.bucket_name)

            if not self.bucket.creation_date:
                logger.info(f"bucket not exist and bucket created : {self.bucket_name}")

                self.bucket = self.s3_resource.create_bucket(
                    Bucket=self.bucket_name,
                    CreateBucketConfiguration={
                        "LocationConstraint": "ap-south-1",
                    },
                    # ACL="private",
                )

            logger.info(self.bucket.name)

            return self.bucket
        except Exception as error:
            logger.error(error)

    def chek_folder_path_in_bucket(self, folder_path: str) -> str:
        """Check folder path
        If folder path not exist create and return path
        Input : folder_path:str
        Return : folder_path:str
        """
        try:
            objects = self.bucket.objects.filter(Prefix=folder_path + "/")

            s3_object = [data.key for data in objects]

            if folder_path not in s3_object:
                self.bucket.put_object(Bucket=self.bucket_name, Key=folder_path + "/")
                logger.info("folder path created")
            else:
                logger.info("Data already exists")
            return folder_path
        except Exception as error:
            logger.info(error)

    def insert_data(self, folder_path: str, file_name: str, data) -> None:
        """
        Creating file and inserting data.
        Input :
            1) folder_path : str
            2) file_name : str
            3) data : base64
        Return :
            None
        """
        try:
            file_key_to_check = folder_path + "/" + file_name

            file_exist = False

            for obj in self.bucket.objects.filter(Prefix=file_key_to_check):
                logger.info(obj)
                find_file_name = obj.key.split("/")[-1]
                if find_file_name == file_name:
                    file_exist = True
                    break

            if file_exist:
                logger.info("exist")

            else:
                response = self.bucket.put_object(
                    Bucket=self.bucket_name, Key=file_key_to_check, Body=data
                )
                logger.info(response)
                logger.info("not exist")
        except Exception as error:
            logger.error(error)

    def retriving_data_from_bucket(self, folder_path) -> None:
        """
        Get the total data from bucket based on path and
        it will download the data in current working directory
        Input:
            1) folder_path : str
        Return:
            None
        """
        try:
            folder = folder_path + "/"
            objects = self.bucket.objects.filter(Prefix=folder)

            folder_files = [
                data.key for data in objects
            ]  # getting folder and files in a folder.

            output_directory = [
                data for data in folder_files if not data.endswith(("png", "jpg"))
            ]

            for i in range(0, len(output_directory)):
                os.makedirs(output_directory[i], exist_ok=True)
                objects = self.bucket.objects.filter(Prefix=output_directory[i])

                for data in objects:

                    saving_files = os.getcwd() + "\\" + data.key.replace("/", "\\")

                    if not os.path.exists(saving_files):

                        if data.key.endswith(".png") or data.key.endswith(".jpg"):
                            with open(saving_files, "w") as file:
                                pass

                            if os.path.exists(saving_files):
                                self.bucket.download_file(data.key, saving_files)
                        else:
                            print("File not exist")

        except Exception as error:

            logger.error(error)

    def retriving_data_as_a_link_from_bucket(self, folder_path) -> None:
        """
        Get the total data from bucket based on path as a link
        Input:
            1) folder_path : str
        Return:
            1) None
        """
        try:
            folder = folder_path + "/"
            objects = self.bucket.objects.filter(Prefix=folder)

            logger.info(objects)

            folder_files = [
                data.key for data in objects
            ]  # getting folder and files in a folder.

            logger.info(len(folder_files))
            # filter based on folder names
            for i in range(0, len(folder_files) - 1):
                objects = self.bucket.objects.filter(Prefix=folder_files[i + 1])

                # Based on data key name it will give link
                for data in objects:
                    presigned_url = self.s3_resource.meta.client.generate_presigned_url(
                        "get_object",
                        Params={"Bucket": self.bucket_name, "Key": data.key},
                    )

                    logger.info("Pre-signed URL:", presigned_url)
        except Exception as error:
            logger.error(error)

    def set_bucket_policy(self, policy_document) -> None:
        """
        Set bucket policy for the S3 bucket.
        Input:
            1) policy_document: dict - The bucket policy document.
        Return:
            None
        """
        try:
            self.bucket.Policy().put(Policy=policy_document)
            print("Bucket policy set successfully.")
        except Exception as error:
            logger.error(error)

    def set_cors_policy(self, cors_configuration: dict) -> None:
        """
        Set CORS configuration for the S3 bucket.
        Input:
            1) cors_configuration: dict - The CORS configuration.
        Return:
            None
        """
        try:
            self.bucket.Cors().put(
                CORSConfiguration={"CORSRules": [cors_configuration]}
            )
            print("CORS configuration set successfully.")
        except Exception as error:
            logger.error(error)

    def saving_data_into_aws_s3(self, key: str, byte_array: bytes) -> None:
        """For saving the img URL in s3 bucket
        Input:
            key {str} -- Key of the image
            s3Bucket {s3Bucket} -- s3_resources(s3bucket)
            byte_array {bytes} -- bytes
        """
        try:
            data_1 = self.bucket.put_object(
                Key=key,
                Body=byte_array,
            )
        except Exception as error:
            logger.error(error)
