import re
"""déterminer si un drug est considéré comme mentionné dans un article PubMed ou un essai clinique ou par un journal"""
class MentionAnalyzer:

    def analyze_mentions(self, drug,text):

        pattern = re.compile(rf'\b{re.escape(drug)}\b', re.IGNORECASE)
        mention = re.findall(pattern, text)
        
        return mention
