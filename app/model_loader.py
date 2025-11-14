import os
import pickle
import joblib


def save_uploaded_model(uploaded_file, dest_dir="../models"):
    """Guarda el archivo subido en `dest_dir` y devuelve la ruta guardada.
    `uploaded_file` puede ser un objeto con `.read()` y `.name` (como Streamlit UploadedFile).
    """
    os.makedirs(dest_dir, exist_ok=True)
    name = getattr(uploaded_file, "name", "uploaded_model")
    path = os.path.join(dest_dir, name)
    # uploaded_file puede ser bytes o file-like
    content = None
    try:
        content = uploaded_file.read()
    except Exception:
        # si es bytes
        content = uploaded_file
    with open(path, "wb") as f:
        f.write(content)
    return path


def load_model(path):
    """Carga un modelo desde `path`. Soporta joblib y pickle (.pkl, .joblib, .sav).
    ADVERTENCIA: Unpickling ejecuta código arbitrario — no cargar modelos no confiables.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"Modelo no encontrado: {path}")

    lower = path.lower()
    try:
        if lower.endswith(".joblib") or lower.endswith(".jl"):
            return joblib.load(path)
        # intenta joblib de todos modos (es robusto)
        try:
            return joblib.load(path)
        except Exception:
            pass
        # fallback a pickle
        with open(path, "rb") as f:
            return pickle.load(f)
    except Exception as e:
        raise RuntimeError(f"Error cargando el modelo: {e}")
