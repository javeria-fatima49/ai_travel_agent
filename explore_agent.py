class ExploreAgent:
    def __init__(self, model):
        self.model = model

    def run(self, destination: str) -> str:
        prompt = f"""
        Suggest fun things to do, local food, and attractions in {destination}.
        Respond with emojis and excitement.
        """
        return self.model.generate_content(prompt).text
