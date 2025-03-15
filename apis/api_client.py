import requests
from urllib.parse import quote
import json
import os

class APIClient:
    def __init__(self, api_key, base_url):
        self.api_key = api_key
        self.base_url = base_url
        self.models = self._fetch_models()

    def _fetch_models(self):
        models_url = "https://api.retportal.com/v1/models"
        try:
            response = requests.get(models_url)
            response.raise_for_status()
            models_data = response.json()
            models = {}
            for model in models_data:
                api_type = model.get("api_type")
                model_name = model.get("model")
                if api_type and model_name:
                    if api_type not in models:
                        models[api_type] = []
                    models[api_type].append(model_name)
            return models
        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch models: {e}")
            return {}

    def _build_url(self, endpoint, params=None, model=None):
        url = self.base_url + endpoint + f"api_key={self.api_key}"
        if params:
            for key, value in params.items():
                url += f"&{key}={quote(value)}"
        if model:
            url += f"&model={quote(model)}"
        return url

    def get(self, endpoint, params=None, model=None):
        url = self._build_url(endpoint, params, model)
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

    def is_valid_model(self, api_type, model_name):
        return model_name in self.models.get(api_type, [])

