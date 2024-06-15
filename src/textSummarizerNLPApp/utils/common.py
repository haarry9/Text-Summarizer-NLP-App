import os
from box.exceptions import BoxValueError
import yaml
from textSummarizerNLPApp.logging import logger
from ensure import ensure_annotations
from box import ConfigBox 
from pathlib import Path
from typing import Any


@ensure_annotations # used to avoid function input datatype mismatch
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    '''
    Reads yaml file and returns

    Args:
        path_to_yaml (Path): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty yaml file

    Returns:
        ConfigBox: ConfigBox type
    '''
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            if content is None:
                raise BoxValueError("yaml file is empty")
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError as e:
        logger.error(f"Error loading yaml file: {path_to_yaml} - {e}")
        raise ValueError("yaml file is empty") from e
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise e
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    '''
    Create list of directories

    Args:
    path_to_directories (list): list of path of directories 
    verbose (bool, optional): print log if directory is created. Default is True.
    '''
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory: {path}")


@ensure_annotations
def get_size(path: Path) -> str:
    '''
    get size in KB

    Args:
        path (Path): Path of the file

    Returns:
        str: size in KB
    '''
    if path.exists() and path.is_file():
        size_in_kb = round(os.path.getsize(path) / 1024)
        return f"~ {size_in_kb} KB"
    else:
        logger.error(f"File does not exist: {path}")
        return "File does not exist"
