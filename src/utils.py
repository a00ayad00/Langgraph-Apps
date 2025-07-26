import yaml
from box.exceptions import BoxValueError
from box import ConfigBox

def read_yaml(yaml_path: str) -> ConfigBox:
    try:
        with open(yaml_path) as yaml_file:
            content = yaml.safe_load(yaml_file)
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e