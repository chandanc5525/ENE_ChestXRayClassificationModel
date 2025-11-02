import os
from pathlib import Path

# ---------------------------------------------------------
# Minimal CNN Project Folder Structure Generator
# ---------------------------------------------------------

PROJECT_NAME = "Chest_Xray_Classification"

# Folder structure
folders = [
    f"{PROJECT_NAME}/config",
    f"{PROJECT_NAME}/data",
    f"{PROJECT_NAME}/logs",
    f"{PROJECT_NAME}/metrics",
    f"{PROJECT_NAME}/models",
    f"{PROJECT_NAME}/notebooks",
    f"{PROJECT_NAME}/src/data",
    f"{PROJECT_NAME}/src/models",
    f"{PROJECT_NAME}/src/training",
    f"{PROJECT_NAME}/src/evaluation",
    f"{PROJECT_NAME}/src/utils",
]

# Files to create (mostly placeholders)
files = [
    f"{PROJECT_NAME}/config/config.yaml",
    f"{PROJECT_NAME}/requirements.txt",
    f"{PROJECT_NAME}/README.md",
    f"{PROJECT_NAME}/.gitignore",
    f"{PROJECT_NAME}/main.py",
    f"{PROJECT_NAME}/src/pipeline.py",
    f"{PROJECT_NAME}/src/data/data_ingestion.py",
    f"{PROJECT_NAME}/src/data/data_preprocessing.py",
    f"{PROJECT_NAME}/src/models/cnn_model.py",
    f"{PROJECT_NAME}/src/training/trainer.py",
    f"{PROJECT_NAME}/src/evaluation/evaluator.py",
    f"{PROJECT_NAME}/src/utils/logger.py",
]

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create __init__.py in src submodules
src_dirs = [
    "src",
    "src/data",
    "src/models",
    "src/training",
    "src/evaluation",
    "src/utils",
]
for d in src_dirs:
    Path(f"{PROJECT_NAME}/{d}/__init__.py").touch()

# Create empty placeholder files
for file in files:
    Path(file).touch()

# Write simple contents for readme and gitignore
Path(f"{PROJECT_NAME}/README.md").write_text(f"# {PROJECT_NAME}\n\nModular CNN project structure.")
Path(f"{PROJECT_NAME}/.gitignore").write_text("""__pycache__/
*.pyc
models/
logs/
data/
metrics/
.vscode/
.DS_Store
""")

print(f"Project structure '{PROJECT_NAME}' created successfully.")
