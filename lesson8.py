import random
import pandas as pd


lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
print(lst)
data = pd.DataFrame({'whoAmI': lst})
print(data)


human_column = [1 if x == 'human' else 0 for x in lst]
robot_column = [1 if x == 'robot' else 0 for x in lst]
one_hot_representation = pd.DataFrame({'human': human_column, 'robot': robot_column})
print(one_hot_representation)
