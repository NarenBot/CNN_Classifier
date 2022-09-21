import os
from pathlib import Path
import logging


logging.basicConfig(filename="Logs.log", level=logging.INFO,
                    format='[%(asctime)s] : %(message)s')

package_name = "CNN_Classifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"scripts/{package_name}/__init__.py",
    f"scripts/{package_name}/components/__init__.py",
    f"scripts/{package_name}/config/__init__.py",
    f"scripts/{package_name}/entity/__init__.py",
    f"scripts/{package_name}/constants/__init__.py",
    f"scripts/{package_name}/pipeline/__init__.py",
    f"scripts/{package_name}/utils/__init__.py",
    "tests/__init__.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "configs/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "toxi.ini",
    "research/trails.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(
            f"Created directory: '{filedir}' for filename: '{filename}'")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as file:
            pass
            logging.info(f"Created empty file: '{filepath}'")
    else:
        logging.info(f"'{filename}' already exists!")
