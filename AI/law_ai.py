import openai
import os

class LawAI:
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")
        self.messages = []
        self.messages=[{"role": "system", "content": "Jesteś polskim prawnikiem. Twoim zadaniem jest odpowiedzieć na pytania klientów."}]


    def generate(self, query):
        new_query = {"role": "user", "content": query}
        self.messages.append(new_query)
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.messages,
        )
        response = completion.choices[0].message
        self.messages.append(response)
        return response

    def clear(self):
        self.messages = []

    def get_messages(self):
        return self.messages
    

    def generate_document(self, query):
        return