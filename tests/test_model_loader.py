import pytest
import os
from app import model_loader


def test_load_nonexistent_raises():
    with pytest.raises(FileNotFoundError):
        model_loader.load_model("models/no_existe.pkl")
