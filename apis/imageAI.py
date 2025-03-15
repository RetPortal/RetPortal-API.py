from retportal.api_client import APIClient

class ImageAIAPI:
    def __init__(self, api_key):
        self.client = APIClient(api_key, "https://api.retportal.com/imageAI/")

    def get_image(self, prompt, model=None):
        if model and not self.client.is_valid_model("image", model):
            return {"error": f"Invalid model: {model}"}
        return self.client.get("", params={"prompt": prompt}, model=model)

