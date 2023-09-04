from src.data_processing import DataProcessor
from src.json_generation import JSONGenerator
import json

# Extraire depuis le json produit par la data pipeline le nom du journal qui mentionne le plus de médicaments différents
def maxJournal(file):
    # Lire des données JSON et les convertir en dictionnaire
    with open(file, 'r') as json_file:
        data = json.load(json_file)
    journals={}
    # Traverser des données JSON
    for dictionary in data:
        for drug, articles in dictionary.items():
            for article in articles:
                if article['journal'] not in journals.keys():
                    journals[article['journal']]=[drug]
                elif drug not in journals[article['journal']]:
                    journals[article['journal']].append(drug)

    # Trouver le nombre max de médicaments différents
    mx = max(len(journals[x]) for x in journals.keys())

    most_common_journal=[k for k, v in journals.items() if len(v)==mx]
    print("le nom du journal qui mentionne le plus de médicaments différents :")
    for journal in most_common_journal:
        print(f"- {journal}，en total {len(journals[journal])} médicaments différents : {journals[journal]}")

    # json de médicaments par journal (bonus)
    with open("results/drugs_by_journal.json","w", encoding='utf-8') as f:
        f.write( json.dumps( journals,ensure_ascii=False,indent=4) )       


if __name__ == "__main__":
    data_dir = "data"  
    #data_processing
    data_processor = DataProcessor(data_dir)
    drugs_df = data_processor.load_data('drugs')
    pubmed_df = data_processor.load_data('pubmed')
    clinical_trials_df = data_processor.load_data('clinical_trials')
   
    #json_generation
    json_generator = JSONGenerator(drugs_df)
    json_generator.generate_json(pubmed_df,clinical_trials_df)

    #maxjournal
    maxJournal('results/drugs_references.json')