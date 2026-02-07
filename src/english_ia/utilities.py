import json
from importlib.resources import files
import os

# Rutas de archivos dentro del paquete nexus
data_file = files("english_ia").joinpath("data/data.json")
system_file = files("english_ia").joinpath("data/system.txt")

def load_system():
    file = system_file.read_text(encoding="utf-8")
    return file


def load_data():
    return json.loads(data_file.read_text(encoding="utf-8"))


def save_current_agent(current_agent):
    data = load_data()
    data["current_agent"] = current_agent
    data_file.write_text(json.dumps(data, ensure_ascii=False, indent=4), encoding="utf-8")

if __name__ == "__main__":
    print(load_system())