# Localidades de Argentina por Provincia con Coordenadas

Este repositorio contiene un dataset estructurado de **todas las localidades de Argentina**, agrupadas por provincia, incluyendo su **nombre, latitud y longitud**.

## 📌 ¿Qué contiene este dataset?

- Localidades de todas las provincias argentinas.
- Coordenadas geográficas (`latitud`, `longitud`) para cada localidad.
- Organización clara por provincia en archivos individuales `.json`.

## 📦 Estructura de Archivos

- `argentina.json`: archivo maestro con todas las provincias y sus respectivas localidades.
- Carpeta `provincias/`: un archivo `.json` por provincia, ideal para consultas puntuales o integraciones específicas.

### 📁 Ejemplo de estructura

```json
{
  "SANTA FE": [
    {
      "nombre": "SAN JERONIMO",
      "latitud": "-32.2399352",
      "longitud": "-61.231266"
    },
    ...
  ],
  ...
}
```

### Ejemplo de archivo provincial (`provincias/santa_fe.json`):

```json
[
  {
    "nombre": "SAN JERONIMO",
    "latitud": "-32.2399352",
    "longitud": "-61.231266"
  },
  ...
]
```

## 🎯 Usos posibles

- Integración en sistemas de georreferenciación o GIS.
- Cruces con datos censales, sanitarios o sociales.
- Visualización de mapas interactivos.
- Aplicaciones gubernamentales, académicas o civiles.

## 📥 Fuente original

Los datos fueron derivados de un dataset estructurado oficial del Ministerio de Obras Públicas de Argentina, conteniendo variables censales y geográficas por localidad.

## 📝 Licencia

Este dataset se publica bajo la licencia **MIT**. Libre para usar, modificar y distribuir con atribución.

---

Desarrollado para la reutilización de datos territoriales de forma abierta, limpia y accesible.
