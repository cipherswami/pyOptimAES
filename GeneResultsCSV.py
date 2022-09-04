import pandas as pd

dfIEEE = pd.read_csv('Results_IEEE.csv')
dfOptimized = pd.read_csv('Results_Optimized.csv')

dfIEEE = dfIEEE.rename(columns={
    'CCMP Encryption Time': 'CCMP Encryption Time IEEE', 
    'CCMP Decryption Time': 'CCMP Decryption Time IEEE',
    'GCMP Encryption Time': 'GCMP Encryption Time IEEE',
    'GCMP Decryption Time': 'GCMP Decryption Time IEEE'
    })

dfOptimized = dfOptimized.rename(columns={
    'CCMP Encryption Time': 'CCMP Encryption Time Optimized',
    'CCMP Decryption Time': 'CCMP Decryption Time Optimized',
    'GCMP Encryption Time': 'GCMP Encryption Time Optimized',
    'GCMP Decryption Time': 'GCMP Decryption Time Optimized'
    })

df = pd.DataFrame()

df['Block Length'] = dfIEEE['Block Length']
df['CCMP Encryption Time IEEE'] = dfIEEE['CCMP Encryption Time IEEE']
df['CCMP Decryption Time IEEE'] = dfIEEE['CCMP Decryption Time IEEE']
df['GCMP Encryption Time IEEE'] = dfIEEE['GCMP Encryption Time IEEE']
df['GCMP Decryption Time IEEE'] = dfIEEE['GCMP Decryption Time IEEE']
df['CCMP Encryption Time Optimized'] = dfOptimized['CCMP Encryption Time Optimized']
df['CCMP Decryption Time Optimized'] = dfOptimized['CCMP Decryption Time Optimized']
df['GCMP Encryption Time Optimized'] = dfOptimized['GCMP Encryption Time Optimized']
df['GCMP Decryption Time Optimized'] = dfOptimized['GCMP Decryption Time Optimized']

print(df)
df.to_csv('Results_analysis.csv', index=False)