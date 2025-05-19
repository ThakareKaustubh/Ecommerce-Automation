import yaml
import os
from dotenv import load_dotenv

load_dotenv()  # Load .env variables


def load_config(file_path="config\config.yaml"):
    with open(file_path, "r") as f:
        config = yaml.safe_load(f)
    # Add environment-based credentials
    config["credentials"] = {
        "username": os.getenv("USERNAME"),
        "password": os.getenv("PASSWORD")
    }
    return config
