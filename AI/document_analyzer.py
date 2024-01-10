from AI.law_ai_abstract import LawAIAbstract

class DocumentAnalyzer(LawAIAbstract):
    def __init__(self):
        self.messages = []
        self.messages=[{"role": "system", "content": """
                Jesteś polskim prawnikiem. Twoim zadaniem jest przeanalizowanie treści dokumentu i wygenerowanie wyjaśnienia dla klienta oraz opracoawnie 
                        odpowiedzi na podany dokument (co można zrobić, aby temat rozwiązać z jak największą korzyścią dla klienta)."""}]

        super().__init__(self.messages)

    def analyze_document(self, query):
        return self.generate(query)