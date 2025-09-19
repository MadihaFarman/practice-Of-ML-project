# code related to data transfromation

import sys
import os
from dataclasses import dataclass
from src.logger import logging
from src.exception import CustomException
import pandas as pd
import numpy as np

from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from src.utils import save_object
@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts','preprocessor.pkl')


class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()

    def get_data_transformer_object(self):
       """
       This function is responsible for data Transformation
       """

       try:
          numerical_cols = ['writing_score','reading_score']
          categorical_coloumns = [
                'gender',
                'race_ethnicity',
                'parental_level_of_education',
                'lunch',
                'test_preparation_course',
            ]
        

          num_pipeline = Pipeline(
            steps=[
                ('imputer',SimpleImputer(strategy='most_frequent')),
                ('scaler',StandardScaler(with_mean=False))
            ]
        )

          categorical_pipeline = Pipeline(
                steps = [
                    ('imputer',SimpleImputer(strategy='most_frequent')),
                    ('one_hot_encoder',OneHotEncoder()),
                    ('scaler',StandardScaler(with_mean=False))

                ]
            )
        
          logging.info(f'Numerical coloumns : {numerical_cols}')
          logging.info(f'Categorical coloumns : {categorical_coloumns}')

          preprocessor = ColumnTransformer(
            [
                ('num_pipeline',num_pipeline,numerical_cols),
                ('categorical_pipeline',categorical_pipeline,categorical_coloumns)
            ]
        )

          return preprocessor
       
       except Exception as e:
          raise CustomException(e,sys)

    
    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info('Read train and test data completed!')

            logging.info('Obtaining preprocessing object')

            preprocessing_obj = self.get_data_transformer_object()

            target_col_name = 'math_score'
            
            input_feature_train_df = train_df.drop(columns=[target_col_name],axis=1)
            target_feature_train_df = train_df[target_col_name]

            input_feature_test_df = test_df.drop(columns=[target_col_name],axis=1)
            target_feature_test_df = test_df[target_col_name]

            logging.info(
                f"Applying preprocessing object on training dataframe and test dataframe"
            )

            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)

            train_arr = np.c_[
                input_feature_train_arr,np.array(target_feature_train_df)
            ]

            test_arr = np.c_[
                input_feature_test_arr,np.array(target_feature_test_df)
            ]

            logging.info("saving preprocessing object.")

            save_object(          # function is defined in utils.py

                file_path= self.data_transformation_config.preprocessor_obj_file_path,
                obj = preprocessing_obj
            )

            return(
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )
        except Exception as e:
            raise CustomException(e,sys)
        

## extra code for checking if data_transformation.py is working well        

# if __name__ == "__main__":
#     obj = DataTransformation()

#     train_path = "artifacts/train.csv"   
#     test_path = "artifacts/test.csv"     

#     train_arr, test_arr, _ = obj.initiate_data_transformation(train_path, test_path)
#     print("Data transformation completed successfully!")

        


