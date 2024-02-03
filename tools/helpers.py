import os
import pandas as pd
import numpy as np
import plotly.express as px
import logging as log


"""
This module contains functions for creating tables, columns, and writing DataFrames to files.
"""



def create_calendar_table(start_date, end_date):
    """
    The function creates and returns df calendar table
    """
    df = pd.DataFrame({'date': pd.date_range(start_date, end_date)})
    # week
    df['date_weekday'] = df['date'].dt.strftime("%A")
    df['day_of_week'] = df['date'].apply(lambda x: x.weekday())
    df['is_weekend'] = df['day_of_week'].apply(lambda x: (x>4) * 1)
    df['abbreviated_weekday'] = df['date'].dt.strftime("%a")
    # month
    df['month_start'] = df['date'].to_numpy().astype('datetime64[M]')
    df['month_num'] = df['date'].dt.month
    df['month_year'] = df['date'].dt.strftime("%B %Y")
    # quater # optional
    # df['quarter_number'] = df['date'].dt.quarter
    # df['quarter_text'] = df['date'].apply(lambda x: f'Q{x.quarter} {x.strftime("%Y")}')
    # # year
    # df['year_start'] = df['date'].to_numpy().astype('datetime64[Y]')
    # df['year'] = df['date'].dt.isocalendar().year
    
    return df


def add_date_based_columns(df, date):
    """
    Function to add date relative columns
    """    
    month = df[date].to_numpy().astype('datetime64[M]') 
    month_num = df[date].dt.month
    month_year = df[date].dt.strftime("%B %Y")
    weekday = df[date].dt.strftime("%A")
    day_of_week = df[date].apply(lambda x: x.weekday())
    is_weekend = day_of_week.apply(lambda x: (x>4) * 1)
    
    return month, month_num, month_year, day_of_week, is_weekend     
  

def write_df_to_csv(df, path_to_save, file_name):
    """
    Function writes DataFrame to csv file
    """
    
    df.to_csv(
        os.path.join(path_to_save, file_name)
        ,encoding='utf-8'
        ,header='column_names'
        ,index=False
        ,mode='w' # truncate the file first
        )
    log.info(f'The DataFrame {df} has been written to {path_to_save}')
    

if __name__=='__main__':
    print("helpers.py is being run directly")
else:
    print("helpers.py is being imported into module")