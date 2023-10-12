from langchain.document_loaders import DirectoryLoader
from langchain.indexes import VectorstoreIndexCreator
from deep_translator import (GoogleTranslator)

class ConstitutionAI:
    def __init__(self, query):
        self.query = query
    
    def getResponse(self):
        translated = GoogleTranslator(source='auto', target='en').translate(text=self.query)
        loader = DirectoryLoader('_data', '*.txt')
        index = VectorstoreIndexCreator().from_loaders([loader])

        translated_response = GoogleTranslator(source='auto', target='pl').translate(text=index.query(translated))
        return translated_response
