"""Tool for processing DFF and TXP files."""
from pathlib import Path
from typing import Annotated
from cyclopts import App, Group, Parameter, validators
from cyclopts import types as ct

from handlers.dff_handler import dff_dump, dff_extract

app = App()

input_group = Group(
    "Input (choose one)",
    validator=validators.LimitedChoice(1),
    default_parameter=Parameter(negative=""),
)
action_group = Group(
    "Action (choose one)",
    validator=validators.LimitedChoice(1),
    default_parameter=Parameter(negative=""),
)

def txp_dump(txp: Path, output: Path) -> None:
    """Dump TXP file to JSON."""
    # TODO
    pass


def txp_extract(txp: Path, output_dir: Path) -> None:
    """Extract TXP file."""
    # TODO
    pass


@app.default
def main(
    *,
    dff: Annotated[ct.ExistingFile | None, Parameter(group=input_group)] = None,
    txp: Annotated[ct.ExistingFile | None, Parameter(group=input_group)] = None,
    dump: Annotated[Path | None, Parameter(group=action_group)] = None,
    extract: Annotated[list[Path] | None, Parameter(group=action_group)] = None,
) -> None:
    """Process DFF or TXP files."""
    if dump is not None:
        if dff is not None:
            dff_dump(dff, dump)
        else:
            assert txp is not None
            txp_dump(txp, dump)
    else:
        assert extract is not None
        if dff is not None:
            if len(extract) != 2:
                raise ValueError("--dff --extract requires: <resblock_file> <output_dir>")
            resblock_file: Path = extract[0]
            output_dir: Path = extract[1]
            if not resblock_file.exists():
                raise FileNotFoundError(f"Resblock file not found: {resblock_file}")
            dff_extract(dff, resblock_file, output_dir)
        else:
            assert txp is not None
            if len(extract) != 1:
                raise ValueError("--txp --extract requires: <output_dir>")
            txp_extract(txp, extract[0])


app()
