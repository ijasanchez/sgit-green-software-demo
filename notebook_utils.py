import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def plot_metric_vs_input_size(dataframe, metric):
    """
    Plots the specified metric against input size, differentiated by execution type.

    Parameters:
        dataframe (pd.DataFrame): DataFrame containing 'input_size', 'execution_type', and the specified metric columns.
        metric (str): The name of the metric to plot ('emissions' or 'execution_time').

    Returns:
        None
    """
    if metric not in dataframe.columns:
        raise ValueError(f"Metric '{metric}' not found in DataFrame columns.")

    # Set the aesthetic style of the plots
    sns.set_theme(style="whitegrid")

    # Initialize the matplotlib figure
    plt.figure(figsize=(12, 6))

    # Create the line plot
    sns.lineplot(
        data=dataframe,
        x='input_size',
        y=metric,
        hue='execution_type',
        marker='o'
    )

    # Set plot title and labels
    plt.title(f'{metric.replace("_", " ").capitalize()} vs. Input Size by Execution Type')
    plt.xlabel('Input Size')
    plt.ylabel(metric.replace("_", " ").capitalize())

    # Display the legend
    plt.legend(title='Execution Type')

    # Show the plot
    plt.show()
    
def plot_execution_time_vs_emissions(dataframe):
    """
    Plots a scatter plot to visualize the correlation between execution time and emissions.

    Parameters:
        dataframe (pd.DataFrame): DataFrame containing 'execution_time' and 'emissions' columns.

    Returns:
        None
    """
    # Validate input
    if not {'execution_time', 'emissions'}.issubset(dataframe.columns):
        raise ValueError("DataFrame must contain 'execution_time' and 'emissions' columns.")

    # Set the aesthetic style of the plots
    sns.set_theme(style="whitegrid")

    # Initialize the matplotlib figure
    plt.figure(figsize=(10, 6))

    # Create the scatter plot
    sns.scatterplot(
        data=dataframe,
        x='execution_time',
        y='emissions',
        alpha=0.7
    )

    # Set plot title and labels
    plt.title('Correlation between Execution Time and Emissions')
    plt.xlabel('Execution Time (seconds)')
    plt.ylabel('Emissions (kg CO₂eq)')

    # Show the plot
    plt.show()

