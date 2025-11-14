import pandas as pd


def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    """Placeholder de preprocesado. Modifica según tu pipeline.
    Aquí dejamos la columna tal cual."""
    return df


def predict(model, df: pd.DataFrame):
    X = preprocess(df)
    preds = model.predict(X)
    return preds
