from check_para import Check_para
from default_data import dataset

class Default(Check_para):
     def __init__(self):
        super().__init__()

    
     def apply_default(self):
            default=Check_para(data='placement_2.csv',target='package',test_size=0.2)
            if default.check_path_file():
                default.read_csv()
     
                if self.data == 'default':
                     default_dataset=dataset()
                     print(default_dataset.Linear_dataset())
#                default.check_test_size()
#     default.check_target()
#     default.check_score()
#     default.check_OF()
#     default.xy_change_type()
#     default.train_test_split()

new= Default()
new.apply_default()



