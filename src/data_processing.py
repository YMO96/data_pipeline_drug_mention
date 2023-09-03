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

        if 'csv' in files[0]:
            df1 = pd.read_csv(path + '/' + files[0],encoding='utf8') #Lire le premier fichier si csv
            print(df1)
        elif 'json' in files[0]:
            df1 = pd.read_json(path + '/' + files[0],convert_dates=False,encoding='utf8') #Lire le premier fichier json

        for file in files[1:]: #lire les fichiers suivants
            if 'csv' in file :
                df2 = pd.read_csv(path +'/' +  file,encoding='utf8')
            elif 'json' in file :
                df2 = pd.read_json(path +'/' +  file,convert_dates=False,encoding='utf8')
            df1 = pd.concat([df1,df2],axis=0,ignore_index=True)  #merge les données

        df_total = df1.drop_duplicates()   #déduplication
        df_total = df_total.reset_index(drop=True) #redéfinir index

        return df_total
