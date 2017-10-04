import pandas as pd
from bs4 import BeautifulSoup
import requests
import os

cols = [0,1,3,4,13,14,15,17,18,19,20,21,22,23,24,25,50,51,52]

def crime_from_web():
    """Returns DataFrame of bexar county criminal records"""
    r = requests.get('http://gov.bexar.org/dc/dcrecords.html')
    soup = BeautifulSoup(r.text, 'html.parser')

    df = pd.DataFrame()
    
    links = soup.find_all('a')
    for link in links:
        if link['href'].endswith('.xls'):
            df = df.append(pd.read_excel(link['href'], parse_cols=cols))
    return df
    
def crime_from_disk():
    files = [f for f in os.listdir() if f.endswith('.xls')]
    df = pd.DataFrame()
    for file in files:
        df = df.append(pd.read_excel(file, parse_cols=cols))
    return df