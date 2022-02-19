import logging
from time import time
import click

from {{ cookiecutter.project_name }}.main import run
from {{ cookiecutter.project_name }}.utils.logging import get_logger

logger = get_logger("CLI-Logger", logging.DEBUG, colored=True)



@click.command()
@click.option("-p", "--path", default="./data_upload/config/files/config.yaml")
@click.pass_context
def cli(path):
    """Execute main process"""
    t0 = time()

    print('\n')
    logger.info("Starting process...")
    
    run(path)

    logger.debug(f"Total process execution time: {round((time() - t0)/60, 2)}M.")
