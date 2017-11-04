import pandas as pd

def fill_miss(dataframe,collist, repl):
    '''
    MUTATING. replaces NaNs in the columns with repl string.
    
    dataframe - Pandas dataframe to fill 
    collist - list of columns in the dataframe to fill the missing values
    repl - string that replaces missing values. Ex: repl = "NO VALUE"
    '''
    for col in [x for x in dataframe.columns if x in collist]:
        dataframe[col].fillna(repl, inplace=True)

def create_dummy(dataframe, collist, target):
    '''
    creates a 0/1 column for the selected columns in the dataframe
    
    dataframe - Pandas dataframe  
    collist - list of columns in the dataframe that will have dummy columns.
    
    target - value in the column that will have value 1. every other value will be replaced by 0
    '''
    neme = ''
    for col in [x for x in dataframe.columns if x in collist]:
        temp = pd.Series(dataframe[col].replace(target, 1).replace('[^target]', 0, regex=True))
        name = 'Missing' + str(col)
        dataframe[name] = temp
    return dataframe

def leveler(dataframe, column, asc_list):
    '''
    .MUTATING. converts values in the dataframe into numbers
    
    dataframe - Pandas dataframe
    column - column to transform
    asc_list - list of values in the cloumn in ascending order.
    values in the asc_list will be replaced by 0,1,2,3...
    '''
    for i in range(len(asc_list)):
        dataframe[column].replace(asc_list[i], i, inplace=True)