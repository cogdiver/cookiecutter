import click
from dotenv import load_dotenv

from {{ cookiecutter.project_name }}.utils.cli import CLI

load_dotenv()

CONTEXT_SETTINGS = dict(
    help_option_names=['-h', '--help'],
    token_normalize_func=lambda x: x.lower(),
)


@click.command(cls=CLI, context_settings=CONTEXT_SETTINGS)
def cli():
    pass


if __name__ == "__main__":
    cli()
