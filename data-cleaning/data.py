import pandas as pd

# create dataset
mydata = {
    'mobil' : ['BMW', 'Lambo', 'Bugga'],
    'slot'  : ['3', '2', '1']
}

# import modules + read file csv
# df = pd.read_csv('contoh.csv')
# df2 = pd.read_csv('games.csv')

myvar = pd.DataFrame(mydata)

print(myvar)