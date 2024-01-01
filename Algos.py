import numpy as np
import pandas as pd

  #### Linear Regression ####
class Linear:
    def __init__(self):
        self.m = None
        self.b = None

    
    def fit(self,x_train,y_train):
        x_bar = x_train.mean()
        y_bar = y_train.mean()
        numerator = 0
        denomumerator = 0

        for i in range(len(x_train)):
            numerator += (x_train[i]-x_bar) * (y_train[i]-y_bar)
            denomumerator += (x_train[i]-x_bar)**2
        self.intercept_ = numerator/denomumerator
        self.coeff_ = y_bar - self.m*x_bar
        return self.intercept_,self.coeff_  

      
    def predict(self,x_test):
            return self.intercept_*x_test+self.coeff_
    

  #### Multiple Linear Regression ####
class MultiLinearRegression:
        def __init__(self):
            self.x_train = np.insert(self.x_train,0,1,axis=1)
        
        def fit(self,x_train,y_train):
            # calcuate the coeffs and intercept
            betas = np.linalg.inv(np.dot(self.x_train.T,self.x_train)).dot(self.x_train.T).dot(self.y_train)
            self.intercept_ = betas[0]
            self.coeff_ = betas[1:]
            return self.intercept_,self.coeff_
        
        def predict(self,x_test):
            return np.dot(self.x_test,self.coeff_) + self.intercept_

