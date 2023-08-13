#requirements
import pandas as pd
import numpy as np
import csv
import os
import sys
import random
from Custom_handling import Custom_exception


class Check_para():

    def __init__(self,data='default',target='',test_size=0.2,score='r2_score',opt_fun=False) -> None:
        self.m=None
        self.b=None
        self.data=data
        self.target=target
        self.test_size=test_size
        self.score=score  
        self.opt_fun=opt_fun
         
    
    def check_path_file(self):
        try:
            if self.data == 'default':
                 return True
            elif not os.path.isfile(self.data):
                raise FileNotFoundError("File is not in the directory.")   
            elif not self.data.endswith('.csv'):
                 raise Custom_exception('Not a CSV file')
            else:
                 return True
          
        except FileNotFoundError as e:
                sys.exit(f"Error: {e}")
        except Custom_exception as e:
                sys.exit(f"Error: {e}") 
    
    
    
    
    def read_csv(self):
        try:  
            with open(self.data,'r') as csv_file:
                content=csv.DictReader(csv_file)
                self.df_=pd.DataFrame(content)
            return self.df_
                
        except FileNotFoundError as e:
            raise Custom_exception("File not found.")
             

#         ##### Check test_size #####
    def check_test_size(self):
          try:
               if isinstance(self.test_size, float):
                    pass
                    
               else:
                    raise Custom_exception('Expected Float type value in test_size.')
          except Custom_exception as e:
              sys.exit(f"Error: {e}")
    

        ##### Check target #####
    def check_target(self):
            try:
               #  sys.exit('1212')
                if self.target in self.df_.columns:
                     pass
                else:
                     raise Custom_exception('Check column name entered as target column.')
            except Custom_exception as e:
             sys.exit(f"Error: {e}")

        ##### Score ####
    def check_score(self):
            try:

                 if self.score in ['mse','r2_score','rmse']:
                      pass
                 else:
                      raise Custom_exception('Wrong Error_Function!!!')
            except Custom_exception as e:
                sys.exit(f"Error: {e}")

                 ###### Optimization Function ######
    def check_OF(self):
            try:
                 if self.opt_fun in ['GD','SGD','gd','sgd','',False]:
                      pass
                 else:  
                      raise Custom_exception('Check entered optimization Function')
            except Custom_exception as e:
                sys.exit(f"Error: {e}")

    def xy_change_type(self):
         for column in self.df_.columns:
              if isinstance(column,object):
                   self.df_.drop(column,axis=1,inplace=True)
         x=self.df_.drop(self.target,axis=1)
         y=self.df_[self.target]

         self.x_=x.astype(float)
         self.y_=y.astype(float)
         

    
    def train_test_split(self):
         print('hello')
         split_index=round(self.test_size*len(self.x_))
     #     random_split=[random.randint(0,split_index) for _ in range(split_index)]
         self.x_train=self.x_.iloc[0:split_index,:]
         self.x_test=self.x_.iloc[split_index+1:,:]

         self.y_train=self.y_.iloc[split_index]
         self.y_test=self.y_.iloc[split_index+1:]
         return self.x_train,self.y_train,self.y_train,self.y_test 


    def return_para(self):
         return [self.df_,self.test_size,self.target,self.opt_fun,self.score]