import json
import os
from datetime import datetime
import pandas as pd

HISTORY_FILE = "history.json"

class HistoryManager:
    def __init__(self):
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        if not os.path.exists(HISTORY_FILE):
            with open(HISTORY_FILE, 'w') as f:
                json.dump({}, f)

    def _load_data(self):
        try:
            with open(HISTORY_FILE, 'r') as f:
                return json.load(f)
        except:
            return {}

    def _save_data(self, data):
        with open(HISTORY_FILE, 'w') as f:
            json.dump(data, f)

    def save_prediction(self, username, disease, confidence, image_name):
        data = self._load_data()
        
        if username not in data:
            data[username] = []
            
        record = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "disease": disease,
            "confidence": float(confidence),
            "image_name": image_name
        }
        
        data[username].append(record)
        self._save_data(data)

    def get_user_history(self, username):
        data = self._load_data()
        return data.get(username, [])

    def get_analytics(self, username):
        """Returns a pandas DataFrame suitable for charting"""
        history = self.get_user_history(username)
        if not history:
            return None
            
        df = pd.DataFrame(history)
        return df
