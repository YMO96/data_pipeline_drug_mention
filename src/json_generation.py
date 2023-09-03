from src.mention_analysis import MentionAnalyzer
import pandas as pd
"""génération et export du résultat"""
class JSONGenerator:
    def __init__(self, drugs_df):
        self.drugs_df = drugs_df

    def generate_json(self, pubmed_df,clinical_trials_df):
        result = {}
        mention_analyzer = MentionAnalyzer()  # constuire un objet MentionAnalyzer

        # parser tous les nom drug
        for _, row in self.drugs_df.iterrows():
            drug_name = row['drug']
            mentions = []

            # parser dans les articles et essai pour voir si le nom existe
            for _, pubmed_row in pubmed_df.iterrows():
                title = pubmed_row['title']
                mention = mention_analyzer.analyze_mentions(drug_name,title)
                if mention:
                    mentions.append({
                        'title': title,
                        'type_article': 'pubmed',
                        'date': pubmed_row['date'],
                        'journal': pubmed_row['journal']
                    })

            for _, trials_row in clinical_trials_df.iterrows():
                title = trials_row['scientific_title']
                mention = mention_analyzer.analyze_mentions(drug_name,title)
                if mention:
                    mentions.append({
                        'title': title,
                        'type_article': 'clinical_trials',
                        'date': trials_row['date'],
                        'journal': trials_row['journal']
                    })

            result[drug_name] = {
                'mentions': mentions              
            }
         # export dans pd
        result_df = pd.DataFrame(result)

        # re-formatter en json
        result_df.to_json('results/drugs_references.json', orient='records', indent=4,force_ascii=False)
        
       
