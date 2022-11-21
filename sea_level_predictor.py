import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    fig, ax = plt.subplots(figsize=(20, 15))
    # Add labels and title
    #ax=fig.add_axes([0,0,1,1])
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    plt.scatter(x, y, color = "maroon", alpha = 0.5)
    # Create first line of best fit
    res = stats.linregress(x, y)
    plt.plot(x, res.intercept + res.slope*x, 'gray')
    #define new set of x values for predictions & set new x limits
    plt.xlim([1870, 2060])
    years_extended = np.arange(2013, 2050, 1)
    #extend prediction line
    line = [slope*year + intercept for year in years_extended]
    plt.plot(years_extended, line, 'gray')

    # Create second line of best fit
    #create new dataframe (years 2000 - 2013)
    df2 = df.loc[df['Year'] >= 2000] 
    xnew = df2['Year']
    ynew = df2['CSIRO Adjusted Sea Level']
    #calculate new values 
    res2 = stats.linregress(xnew, ynew)
    #plot best fit line for values from 2000-2013 
    plt.plot(xnew, res2.intercept + res2.slope*xnew, 'orange')
    #create prediction line based on new values 
    line2 = [res2.slope*year + res2.intercept for year in years_extended]
    #plot prediction line 
    plt.plot(years_extended, line2, 'orange')
    # Save plot and return data for testing (DO NOT MODIFY)
    fig.savefig('sea_level_plot.png')
    return plt.gca()