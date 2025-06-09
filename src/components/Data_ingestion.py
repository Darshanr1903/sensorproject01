from pymongo.mongo_client import MongoClient
import numpy as np
import pandas as pd
import sys
import os
from zipfile import Path
from src.constant import *
from src.exception import CustomException
from src.logger import logging
from src.utils.main_utils import MainUtils
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    artifact_folder:str=os.path.join(artifact_folder)

class DataIngestion:
    def __init__(self):
        self.data_ingestion_config=DataIngestionConfig()
        self.utils=MainUtils()
    

    def export_collection_as_dataframe(self,db_name,collection_name):
        try:
            mongo_client=MongoClient(MONGO_DB_URL)
            collection=mongo_client[db_name][collection_name]
            df=pd.DataFrame(list(collection.find()))
            if("_id" in df.columns.to_list()):
                df.drop(columns=["_id"],axis=1)
                df.replace({"na":np.nan},inplace=True)
            return df
        except Exception as e:
            raise CustomException(e,sys)
    

    def export_data_info_feature_store_file_path(self):
        try:
            logging.info(f"exporting data from mongo db")
            raw_file_path=self.data_ingestion_config.artifact_folder
            os.makedirs(raw_file_path,exist_ok=True)
            sensor_data=self.export_collection_as_dataframe(db_name=MONGO_DATABASE_NAME ,collection_name=MONGO_COLLECTION_NAME)
            logging.info(f"saving exported data info features store file path:{raw_file_path}")
            feature_file_store_path=os.path.join(range,'wafer_fault.csv')
            sensor_data.to_csv(feature_file_store_path,index=False)
            return feature_file_store_path
        except Exception as e:
            raise CustomException(e,sys)
    
    def intiate_data_ingestion(self)->Path:
        logging.info("Entered intiate_data_ingestion method")
        try:
            feature_store_file_path=self.export_data_info_feature_store_file_path()
            logging.info("got the data from mongo db")
            logging.info("exited from initiate_dat_ingestion method from data ingestion class")
            return feature_store_file_path
        except Exception as e:
            raise CustomException(e,sys)