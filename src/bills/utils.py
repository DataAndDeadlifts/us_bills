from pathlib import Path
from yaml import load, SafeLoader
from resources import resources_path


def load_context(resource_dir=resources_path):
    context_path = resource_dir / "context.yaml"
    if context_path.exists():
        return load(context_path.read_bytes(), Loader=SafeLoader)
    return {}
