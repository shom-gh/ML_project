import pandas

def fill_miss(dataframe,collist, repl):
    '''
    replaces NaNs in the columns with repl string.
    
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
    for col in [x for x in dataframe.columns if x in collist]:
        temp = pd.Series(dummy.FireplaceQu).replace(target, 1).replace('[^target]', 0, regex=True)
        name = 'Missing' + str(col)
        dataframe[name] = temp
    return dataframe