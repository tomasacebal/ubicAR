import json
import os

# Leer el archivo de entrada
with open("data_cruda.json", "r", encoding="utf-8") as f:
    input_json = json.load(f)

# Crear estructura transformada
output_json = {}

for entry in input_json.get("worksheet", []):
    provincia = entry.get("Provincia")
    localidad = {
        "nombre": entry.get("Nombre"),
        "latitud": entry.get("Latitud"),
        "longitud": entry.get("Longitud")
    }

    if provincia:
        if provincia not in output_json:
            output_json[provincia] = []
        output_json[provincia].append(localidad)

# Guardar el archivo general
with open("argentina.json", "w", encoding="utf-8") as f:
    json.dump(output_json, f, ensure_ascii=False, indent=2)

# Crear la carpeta para provincias si no existe
os.makedirs("provincias", exist_ok=True)

# Guardar un archivo por provincia
for provincia, localidades in output_json.items():
    # Nombre de archivo seguro (sin espacios, mayúsculas o caracteres raros)
    filename = provincia.lower().replace(" ", "_").replace("á", "a").replace("é", "e") \
        .replace("í", "i").replace("ó", "o").replace("ú", "u").replace("ñ", "n")
    filepath = os.path.join("provincias", f"{filename}.json")
    
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(localidades, f, ensure_ascii=False, indent=2)

print("Transformación completa. Archivos generados en 'data_transformada.json' y en la carpeta 'provincias/'.")
