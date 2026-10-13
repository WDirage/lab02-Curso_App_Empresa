# Proyecto Django: formularios y cálculos

Incluye tres secciones:
- Formulario original de encuesta.
- Calculadora de dos números: suma, resta y multiplicación.
- Cálculo del volumen de un cilindro: `V = π × (diámetro / 2)² × altura`.

## Requisitos
- Python 3.10 o superior.
- pip.

## Ejecutar en Windows
1. Extrae el ZIP en una carpeta.
2. Abre una terminal (CMD o PowerShell) dentro de la carpeta `lab02` (donde está `manage.py`).
3. Crea un entorno virtual y actívalo:

   ```bat
   py -m venv .venv
   .venv\Scripts\activate
   ```

4. Instala las dependencias:

   ```bat
   python -m pip install -r requirements.txt
   ```

5. Inicia el servidor:

   ```bat
   python manage.py runserver
   ```

6. Abre en tu navegador `http://127.0.0.1:8000/`.

## Ejecutar en macOS o Linux
Desde la carpeta `lab02`:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python manage.py runserver
```

La calculadora está en `/encuesta/operaciones/` y el cilindro en `/encuesta/cilindro/`.
