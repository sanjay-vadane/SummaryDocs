class Summarizer:
    def __init__(self):
        pass

    def summarize_text(self, text):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": f"Please summarize the following text:\n\n{text}"}
            ]
        )
        summary = response['choices'][0]['message']['content']
        return summary.strip()