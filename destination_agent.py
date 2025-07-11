class DestinationAgent:
    def __init__(self, model):
        self.model = model

    def run(self, user_input: str) -> str:
        prompt = f"""
You are a smart travel advisor.

User said: "{user_input}"

Step 1: Suggest ONE travel destination based on user's mood or interest.
Step 2: Explain in a short paragraph why it's a perfect fit.

Format the response exactly like this:
Destination: <destination name>
Reason: <brief explanation>
"""
        response = self.model.generate_content(prompt).text.strip()
        return response
