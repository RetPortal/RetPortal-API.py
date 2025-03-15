from retportal.api_client import APIClient

class TextAIAPI:
    def __init__(self, api_key):
        self.client = APIClient(api_key, "https://api.retportal.com/textAI/")

    def get_text(self, prompt, model=None):
        if model and not self.client.is_valid_model("text", model):
            return {"error": f"Invalid model: {model}"}
        return self.client.get("", params={"prompt": prompt}, model=model)
