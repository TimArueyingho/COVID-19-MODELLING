# Basic Data Exploration without comparisons
# !pip install pandas-profiling if not on system
from pandas_profiling import ProfileReport
import pandas_profiling as pdp
import matplotlib.pyplot as plt
import seaborn as sea
import pandas as pd

#% matplotlib inline  (uncomment if using Jupyter NB)
plt.figure(figsize=(25, 15))

master_data_input = input("Please enter dataset path in csv: ")
master_data = pd.read_csv(master_data_input)


class ExploreMasterData:
    def __init__(self, x):
        self.x = x

    def master_data_profile(self):
        PROFILE = ProfileReport(self.x, title='Profiling Report of COVID-19 data', minimal=True, progress_bar=False,
                                missing_diagrams={
                                    'heatmap': True,
                                    'dendrogram': False,
                                })
        PROFILE.to_file(output_file="Master Data.html")

    def histplot_master_data(self):
        for all, column in enumerate(master_data.columns):
            plt.subplot(4, 6, all + 1)
            sea.histplot(data=master_data[column])
            plt.title(column)
        plt.savefig('Histograms of all variables.png')
        plt.tight_layout()
        plt.show()

    def lineplot_master_data(self):
        for all, column in enumerate(master_data.columns):
            plt.subplot(4, 6, all + 1)
            sea.lineplot(data=master_data[column])
            plt.title(column)

        plt.savefig('Lineplots of all variables.png')
        plt.tight_layout()
        plt.show()

    def scatterplot_master_data(Self):
        for all, column in enumerate(master_data.columns):
            plt.subplot(4, 6, all + 1)
            sea.scatterplot(data=master_data[column])
            plt.title(column)

        plt.savefig('Scatterplots of all variables.png')
        plt.tight_layout()
        plt.show()

    def heatmap_master_data(self):
        correlation = master_data.corr()
        fig, ax = plt.subplots(figsize=(10, 10))
        sea.heatmap(data=correlation, annot=False, cmap="seismic", center=0, linewidths=0.9)
        plt.savefig('Master Data.png')
        plt.show()

    def barchart_master_data(self):
        for all, column in enumerate(master_data.columns):
            plt.subplot(4, 6, all + 1)
            sea.barplot(data=master_data[column])
            plt.title(column)
            
        plt.savefig('Barplots of all variables.png')
        plt.tight_layout()
        plt.show()  
        
View_charts = ExploreMasterData(master_data)
View_charts.master_data_profile()
View_charts.histplot_master_data()
View_charts.lineplot_master_data()
View_charts.scatterplot_master_data()
View_charts.heatmap_master_data()
View_charts.barchart_master_data()






