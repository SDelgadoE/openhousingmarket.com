from Post_Calculator_v1 import closest
import pandas as pd
import dask.dataframe as dd
 
#Find closest postcodes
postcode = 'W9 2AN'
kilometers = 0.2
close_postcodes = closest(postcode, kilometers) 
list_postcodes = list(close_postcodes['postcode'])

#Pre load transaction data
dask_df = dd.read_csv('pp-complete.csv', names=['Transaction unique identifier'
                                                                      , 'Price'
                                                                      , 'Date of Transfer'
                                                                      , 'Postcode'
                                                                      , 'Property Type'
                                                                      , 'Old/New'
                                                                      , 'Duration'
                                                                      , 'PAON'
                                                                      , 'SAON'
                                                                      , 'Street'
                                                                      , 'Locality'
                                                                      , 'Town/City' 
                                                                      , 'District'
                                                                      , 'County'
                                                                      , 'PPD Category Type'
                                                                      , 'Record Status'
                                                                      ])


#dask_df.npartitions

#Filter transaction data for the postcodes that are close
result = dask_df[(dask_df['Postcode'].isin(list_postcodes))]

dfout = result.compute()

transaction_data = pd.DataFrame(dfout)
dfout = []
transaction_data = transaction_data.reset_index(drop=True)
transaction_data.head(4)

transaction_data.info()
transaction_data.describe()
