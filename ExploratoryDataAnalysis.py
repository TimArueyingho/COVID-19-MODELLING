#Basic Data Exploration without comparisons
# !pip install pandas-profiling if not on system
import matplotlib.pyplot as plt
import seaborn as sea
import pandas as pd

def eda_selection(file_location):
    # !pip install pandas-profiling if not on system
    import matplotlib
    matplotlib.use('TkAgg')
    import matplotlib.pyplot as plt
    import seaborn as sea
    sea.set(font_scale=0.5)
    import pandas as pd
    master_data = pd.read_csv(f'{file_location}/Master Data.csv')
    # % matplotlib inline  (uncomment if using Jupyter NB)
    #plt.figure(figsize=(25, 15))
    master_data_copy = master_data.copy()
    master_data_copy = master_data_copy.drop(columns=['Region name', 'Local Authority'])
    View_charts2 = ExploreMasterData(master_data_copy)
    View_charts2.histplot_master_data()
    View_charts2.barchart_master_data()
    
    View_charts = ExploreMasterData(master_data)
    View_charts.heatmap_master_data()

class ExploreMasterData:
    def __init__(self, x):
        self.x = x

    def histplot_master_data(self):
        #for all, column in enumerate(master_data.columns):
        for all, column in enumerate(self.x.columns):
            plt.subplot(4, 6, all + 1)
            #sea.histplot(data=master_data[column])
            #plt.tight_layout()
            sea.histplot(data=self.x[column])
            plt.xticks(rotation=30, fontsize=6)
            plt.title(column)
        plt.savefig('Histograms of all variables.png')
        plt.savefig('Histograms of all variables.pdf')
        plt.tight_layout()
        plt.show()

    def lineplot_master_data(self):
        #for all, column in enumerate(master_data.columns):
        for all, column in enumerate(self.x.columns):
            plt.subplot(4, 6, all + 1)
            #sea.lineplot(data=master_data[column])
            # plt.tight_layout()
            plt.xticks(rotation=30, fontsize=6)
            sea.lineplot(data=self.x[column])
            plt.title(column)

        plt.savefig('Lineplots of all variables.png')
        plt.savefig('Lineplots of all variables.pdf')
        plt.tight_layout()
        plt.show()

    def scatterplot_master_data(self):
        #for all, column in enumerate(master_data.columns):
        for all, column in enumerate(self.x.columns):
            plt.subplot(4, 6, all + 1)
            #sea.scatterplot(data=master_data[column])
            # plt.tight_layout()
            plt.xticks(rotation=30, fontsize=6)
            sea.scatterplot(data=self.x[column])
            plt.title(column)

        plt.savefig('Scatterplots of all variables.png')
        plt.savefig('Scatterplots of all variables.pdf')
        plt.tight_layout()
        plt.show()

    def heatmap_master_data(self):
        #correlation = master_data.corr()
        correlation = self.x.corr()
        fig, ax = plt.subplots(figsize=(10, 10))
        sea.heatmap(data=correlation, annot=False, cmap="seismic", center=0, linewidths=0.9)
        plt.savefig('Correlations.png')
        plt.savefig('Correlations.pdf')
        plt.show()

    def barchart_master_data(self):
        #for all, column in enumerate(master_data.columns):
        for all, column in enumerate(self.x.columns):
            plt.subplot(4, 6, all + 1)
            #sea.barplot(data=master_data[column])
            # plt.tight_layout()
            plt.xticks(rotation=30, fontsize=6)
            sea.barplot(data=self.x[column])
            plt.title(column)

        plt.savefig('Barplots of all variables.png')
        plt.savefig('Barplots of all variables.pdf')
        plt.tight_layout()
        plt.show()

    




