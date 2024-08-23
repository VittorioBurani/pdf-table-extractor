#!/usr/bin/env python3
import os
import argparse
from pathlib import Path
from datetime import datetime
import camelot


PATH2CSVS = Path(__file__).parent / 'csvs'


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--files', type=str, help='PDF file / list of PDF files to look into (as single string)')
    return parser.parse_args()


def initialize_empty_folder() -> Path:
    now = datetime.now()
    PATH2CSVS.mkdir(exist_ok=True)
    new_folder = PATH2CSVS / now.strftime('%Y-%m-%d_%H-%M-%S-%f')
    new_folder.mkdir(exist_ok=True)
    return new_folder


def main(files:list[Path]) -> None:
    # Create parent folder for single run:
    new_folder = initialize_empty_folder()
    # Loop files:
    for f in files:
        # Create folder for every file:
        skip_root_char = 1 if os.name == 'posix' else 3
        file_name_for_folder = f.resolve().as_posix()[skip_root_char:].replace('/', '___')
        file_folder = new_folder / (file_name_for_folder)
        file_folder.mkdir(exist_ok=True)
        # Loop on tables:
        table_dfs = camelot.read_pdf(str(f.resolve()), pages='all')
        for i,table in enumerate(table_dfs):
            # Create CSV file for every table:
            table_csv = file_folder / f'{i}.csv'
            table.to_csv(table_csv.resolve())


if __name__ == '__main__':
    args = parse_args()
    print(args.files)
    files = [Path(f) for f in args.files.split('\n')[:-1]]
    main(files=files)
