import pathlib

import yaml


def write_config(filename, content):
    path = pathlib.Path('/'.join(filename.split("/")[:-1]))
    if not path.exists():
        path.mkdir(parents=True)

    with pathlib.Path(filename).open("w") as f:
        yaml.dump(content, f)


def load_config(filename):
    file = pathlib.Path(filename)
    if not file.is_file():
        return False

    with file.open("r") as f:
        return yaml.full_load(f)
