import tqdm
from time import sleep


def run(path):
    total = 10
    with tqdm.tqdm(desc="Procesing...", total=total, ncols=90) as pbar:
        for _ in range(total):
            sleep(1)
            pbar.update(1)
