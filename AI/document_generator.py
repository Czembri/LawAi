from AI.law_ai_abstract import LawAIAbstract

class DocumentGenerator(LawAIAbstract):
    def __init__(self):
        self.messages = []
        self.messages=[{"role": "system", "content": "Jesteś polskim prawnikiem. Twoim zadaniem przeanalizować potrzeby klienta i wygenerować odpowiedni dokument w formacie HTML z odpowiednimi stylami tak żeby był on konwertowalny na format PDF."}]

        super().__init__(self.messages)

    def generate_document(self, query):
        return self.generate(query)