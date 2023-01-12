import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import env
import os


def get_connection(db, user=env.username, host=env.host, password=env.password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

def wrangle_zillow():
    filename = 'zillow.csv'

    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        df = pd.read_sql('SELECT bedroomcnt, bathroomcnt, calculatedfinishedsquarefeet, \
        taxvaluedollarcnt, yearbuilt, taxamount, fips FROM properties_2017 \
            where propertylandusetypeid = 261', get_connection('zillow'))
        df.to_csv(filename)
        df = df.rename(columns = {'bedroomcnt':'bedrooms', 'bathroomcnt':'bathrooms', 'calculatedfinishedsquarefeet':'sqft',
                    'yearbuilt':'year_built'})
        df.drop_duplicates(inplace=True)
        df = df.dropna()
        return df

    