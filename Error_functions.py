import math
class Error:
    def __init__(self,y_test,y_pred):
        self.y_test=y_test
        self.y_pred=y_pred
    
    def mse(self):
        self.mse=0
        for i in len(self.y_test):
           self.mse += (self.y_test[i]-self.y_pred[i])**2/len(self.y_test)
        return self.mse
    

    def rmse(self):
        self.mse=0
        for i in len(self.y_test):
           self.mse += (self.y_test[i]-self.y_pred[i])**2/len(self.y_test)
        self.rmse=math.sqrt(self.mse)
        return self.rmse


    def r2_score(self):
        pass
