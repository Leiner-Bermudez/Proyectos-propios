import json
from pathlib import Path
carpeta = Path(__file__).parent

with open(carpeta / "usuario.json", "r") as f:
    datos = json.load(f)
    activos = [usuario for usuario in datos if usuario["activo"] == True]

with open(carpeta / "activos.json", "w") as f:
    json.dump(activos, f, indent=4)

print("Se guardaron", len(activos), "usuarios activos")