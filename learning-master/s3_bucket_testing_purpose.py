import cv2
from s3_bucket import BucketS3
from datetime import datetime
import json
import time

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(funcName)s:  %(lineno)d - %(message)s  : %(name)s",
)

logger = logging.getLogger(__name__)


if __name__ == "__main__":
    #############################################
    #        Image converting into base64       #
    #############################################
    def image_converting_to_base64(image):
        """
        Converting image to base 64 string.
        Input: image
        Return:
            1) image in bytes
        """
        _, original_images = cv2.imencode(".jpg", image)
        return original_images.tobytes()

    ###########################################
    #       Access S3 bucket resources        #
    ###########################################
    # For creating and Access of boto3.resource.
    bucket_name = "mybucket-for-images-public-amar"
    s3_resources = BucketS3(bucket_name)

    # For checking the bucket existing or not(if it's not exist create).
    s3_bucket = s3_resources.check_bucket_and_create()

    cors_configuration = {
        "AllowedHeaders": ["*"],
        "AllowedMethods": ["GET", "PUT", "POST", "DELETE", "HEAD"],
        "AllowedOrigins": ["*"],
        "ExposeHeaders": ["ETag"],
        "MaxAgeSeconds": 3000,
    }

    s3_resources.set_cors_policy(
        cors_configuration
    )  # This one is not implemented properly

    bucket_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "PublicReadGetObject",
                "Effect": "Allow",
                "Principal": "*",
                "Action": "s3:PutBucketPolicy",
                "Resource": f"arn:aws:s3:::{bucket_name}/*",
            }
        ],
    }

    # Convert the policy to a JSON string
    public_read_policy_json = json.dumps(bucket_policy)
    s3_resources.set_bucket_policy(public_read_policy_json)

    # Creating folder in aws with year and type of work
    year_folder = str(datetime.today().year)
    # print(datetime.today().month)
    folder = (
        f"Pi/{str(year_folder)}/{datetime.today().month}/{str(datetime.today().day)}"
    )
    # Check folder path if it's not exist create path.
    folder_path_of_s3_bucket = s3_resources.chek_folder_path_in_bucket(folder)

    original = f"original_{time.time()}.jpg"

    # For saving data into s3 bucket.
    object_key = folder_path_of_s3_bucket + "/" + original
    image = cv2.imread(
        r"C:\Users\alluv\OneDrive\Pictures\fsr_2_1.jpg",
        1,
    )  # Put you image here.

    s3_resources.saving_data_into_aws_s3(object_key, image_converting_to_base64(image))
    data = {}
    data["Original_Image"] = (
        f"https://{bucket_name}.s3.ap-south-1.amazonaws.com/{object_key}"
    )
    print(data)

    s3_resources.retriving_data_from_bucket(
        "Pi/2024"
    )  # For downloading all data interms of folder.
