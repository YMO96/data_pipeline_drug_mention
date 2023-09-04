import pandas as pd
import os

"""import data files"""
class DataProcessor:
    def __init__(self, data_dir):
        self.data_dir = data_dir

    def load_data(self,data_type):
        if not data_type :
            print("veuillez renseigner le type de donnéees svp")
            return None
        path = f"{self.data_dir}/{data_type}"
        files = os.listdir(path) #Obtenir les noms de tous les fichiers d'un dossier

        #lire les fichiers de données un par un
        mainDf = pd.DataFrame()
        for file in files:
            if 'csv' in file :
                currentDf = pd.read_csv(path +'/' +file,encoding='utf8')
            elif 'json' in file :
                currentDf = pd.read_json(path +'/' + file,convert_dates=False,encoding='utf8')
            mainDf = pd.concat([mainDf,currentDf],axis=0,ignore_index=True) # merge les données

        mainDf = mainDf.drop_duplicates()   #déduplication
        mainDf = mainDf.reset_index(drop=True) #redéfinir index

        return mainDf
