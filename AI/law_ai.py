from AI.law_ai_abstract import LawAIAbstract

class LawAI(LawAIAbstract):
    def __init__(self, messages = []):
        self.messages=[{"role": "system", "content": "Jesteś polskim prawnikiem. Twoim zadaniem jest odpowiedzieć na pytania klientów."}]
        if (messages != []):
            self.messages = messages
            

        super().__init__(self.messages)