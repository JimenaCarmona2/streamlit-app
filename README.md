# ¡Bienvenidos al Dashboard App!
Dashboard app with Streamlit and Plotly that helps to reduce Churn clients with KPI and Machine Learning results.

# Ejecución

Pasos  (Windows):

1. Crear y activar un entorno virtual:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Instalar dependencias:

```powershell
pip install -r requirements.txt
```

3. Ejecutar la app:

```powershell
streamlit run app/main.py
```

4. Flujo de trabajo:
- Sube tu modelo (.pkl o .joblib) en la barra lateral.
- (Opcional) sube un CSV con las muestras a predecir.
- Pulsa "Realizar predicción" para obtener resultados y descargarlos.

Notas:
- El directorio `models/` está en `.gitignore` — guarda tus modelos ahí.
- `app/model_loader.py` tiene una función `load_model` que soporta `joblib` y `pickle`.
- Actualiza `app/utils.py` para que coincida con el preprocesado de tu pipeline.
