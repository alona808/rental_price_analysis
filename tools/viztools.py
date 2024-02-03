"""
This module contains functions for plotting visualization
"""

import os
import pandas as pd
import numpy as np
import plotly.express as px
import logging as log


def highlight_max(s, props=''):
    """
    Function to highlight the max value in columns
    """
    return np.where(s == np.nanmax(s.values), props, '')


def plot_histogram(series, bins=None):
    """
    Function plots histogram of given series
    """
    series_name = series.name.replace('_', ' ').title()
    fig = px.histogram(
        x=series
        ,nbins=bins                   
        ,title = f'Histogram of {series_name}'
        ,template='plotly_dark'
        )
    fig.show()


def plot_boxplot(series):
    """
    Function plots boxplot of given series
    """
    series_name = series.name.replace('_', ' ').title()
    fig = px.box(
        x=series
        ,title = f'Box Plot of {series_name}'
        ,template='plotly_dark'
        )
    fig.show()


def plot_correlation_heatmap(df, df_name='DataFrame'):
    """
    Function plots correlation heatmap of given DataFrame
    """
    # Correlation 
    df_corr = df.corr().round(1)
    # display(df_corr) # optional
    # Mask to matrix
    mask = np.zeros_like(df_corr, dtype=bool)
    mask[np.triu_indices_from(mask)] = True
    # Viz
    df_corr_viz = df_corr.mask(mask).dropna(how='all')
    
    fig = px.imshow(df_corr_viz
        ,text_auto=True
        ,title = f'Correlation Matrix of {df_name}'
        ,template='plotly_dark'
        )
    fig.show()

def plot_heat_map(df, color_val, title=''):
    """
    """
    fig = px.imshow(
        df.values
        ,x = df.columns # labels for x-axis
        ,y = df.index # labels for y-axis 
        ,text_auto=',.6r', aspect="auto"
        ,labels=dict(x='', y='', color=color_val) 
        ,color_continuous_scale='rdpu'  #'pubugn'
        ,title = f'<b>{title}</b>'
        ,template='plotly_dark'
    )
    fig.show()


def plot_dualaxis_line_graph(df, axis_x, axis_y:list, title=''):
    """
    """
    fig = px.line(
        df
        ,x=axis_x
        ,y=axis_y
        ,title=title
        ,template='plotly_dark'
    )
    fig.update_yaxes(showgrid=False).update_xaxes(showgrid=False)\
        .update_traces(textangle=1, selector=dict(type='bar'), textfont_color='white')
    fig.show()      

def plot_line_discrete_map(df, axis_y:list, title:''):
    """
    """
    color_discrete_map={
      axis_y[0]: px.colors.qualitative.Vivid[1],
      axis_y[1]: px.colors.qualitative.Vivid[2],
      axis_y[2]: px.colors.qualitative.Vivid[4]
    }
           

def plot_bar_graph(df, axis_x, axis_y, label, title, color=None):
    """
    Function plots the bar graph
    """
    fig = px.bar(
    df
    ,x=axis_x
    ,y=axis_y
    ,text=label
    ,barmode='group'
    ,template='plotly_dark'
    ,title=title
    ,color=color
    )
    fig.update_yaxes(visible=False, showgrid=False)\
        .update_xaxes(showgrid=False)\
            .update_traces(textangle=1, selector=dict(type='bar'), textfont_color='white')
    fig.show()
    

if __name__=='__main__':
    print("viztools.py is being run directly")
else:
    print("viztools.py is being imported into module")