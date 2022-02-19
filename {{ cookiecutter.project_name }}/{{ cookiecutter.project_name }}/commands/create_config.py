import pprint

import click

from {{ cookiecutter.project_name }}.utils.config import write_config
from {{ cookiecutter.project_name }}.utils.constants import REPOSITORY_NAME

def get_multi_value(message, is_excluded=False):
    insert = True
    values = []
    while insert:
        _file = click.prompt(message, default="")
        if _file:
            obj = {"name": _file}
            if not is_excluded:
                _headers = click.confirm("With headers?")
                obj["headers"] = _headers
            values.append(obj)
        insert = bool(_file)
    return values


@click.command("create_config", short_help="Create a new configuration file")
@click.option('-p', '--path', prompt=True, default=f'./{REPOSITORY_NAME}/config/files/config.yaml')
@click.option("-d", "--default", is_flag=True, show_default=True)
def cli(path, default):
    """This script create a new YAML configuration file."""
    config = None
    if default:
        config = {
            "process": [],
            "folder_reports": f"./{REPOSITORY_NAME}/data/reports",
            {% if cookiecutter.s3.lower()=='y' -%}
            "upload_s3": False,
            {% endif -%}{% if cookiecutter.data_base.lower()=='y' -%}
            "upload_db": False
            {% endif -%}
        }
    else:
        config = {
            "process": [],
            "folder_reports": click.prompt("Folder output", default=f"./{REPOSITORY_NAME}/data/reports"),
            {% if cookiecutter.s3.lower()=='y' -%}
            "upload_s3": click.confirm("Upload to S3?", default=False),
            {% endif -%}{% if cookiecutter.data_base.lower()=='y' -%}
            "upload_db": click.confirm("Upload to DB?", default=False),
            {% endif -%}
        }

        # Folders
        config["process"] = get_multi_value("Insert path (Leave blank to continue)")


    if default or click.confirm(pprint.pformat(config) + "\n\nCreate file?", abort=True):
        write_config(path, config)
    
    click.echo("✅ Configuration file was successfully created ✅")
