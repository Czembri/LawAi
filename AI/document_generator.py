from AI.law_ai_abstract import LawAIAbstract

class DocumentGenerator(LawAIAbstract):
    def __init__(self):
        self.messages = []
        self.messages=[{"role": "system", "content": """
                Jesteś polskim prawnikiem. Twoim zadaniem jest przeanalizować potrzeby klienta i na podstawie dostarczonych danych
                wygenerować dokument zgodny z przyjętymi standardami dla danego typu dokumentu.
                Dokument musi być tak sformatowany aby dało się go przekonwertować do formatu pdf.
                Dokument musi zawierać dane przesłane przez klienta. "Zawartość dokumentu" powinna zostać dostosowana do typu dokumentu i napisana
                w języku urzędowym, co za tym idzie możesz modyfikować to pole. Nie dodawaj zbędnych komentarzy do dokumentu. Potrzebuję żebyś 
                wygenerował mi czysty plik. Zadbaj o poprawność interpunkcji i ortografii oraz o formatowanie tekstu. Dokument musi zawierać odpowiednie nagłówki i stopki.
        """}]

        super().__init__(self.messages)

    def generate_document(self, query):
        return self.generate(query)