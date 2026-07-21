"""Module that contains functions for handling dff files."""


import json
from pathlib import Path

from cyclopts.types import ExistingFile

from parsers.dff import Dff
from utils import obj_to_dict


def dff_dump(dff: ExistingFile, output: Path) -> None:
    """Dump DFF file to JSON."""
    # Reading a DFF file
    with Dff.from_file(dff) as parser:
        parser._read()
        with open(output, 'w', encoding='utf-8') as f:
            json.dump(obj_to_dict(parser.rw_stream), f, ensure_ascii=False, indent=4)

def dff_extract(dff: Path, resblock: Path, output_dir: Path) -> None:
    """Extract DFF file using a resblock."""
    # TODO
    pass
