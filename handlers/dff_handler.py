"""Module that contains functions for handling dff files."""

import json
from pathlib import Path
import zlib

from cyclopts.types import ExistingFile

from parsers.dff import Dff
from utils import obj_to_dict


def dff_dump(dff: ExistingFile, output: Path) -> None:
    """Dump DFF file to JSON."""
    # Reading a DFF file
    with Dff.from_file(dff) as parser:
        parser._read()
        with open(output, "w", encoding="utf-16") as f:
            json.dump(obj_to_dict(parser.rw_stream), f, ensure_ascii=False, indent=4)


def dff_extract(dff: ExistingFile, resblock: ExistingFile, output_dir: Path) -> None:
    """Extract DFF file using a resblock."""
    total_extracted_assets = 0
    output_dir.mkdir()
    resblock_output_dir = output_dir.joinpath("resblock")
    resblock_output_dir.mkdir()

    with Dff.from_file(dff) as parser:
        
        parser._read()
        for chunk in parser.rw_stream.chunks:
            if chunk.header.type == Dff.ChunkType.embedded_asset:
                extract_embedded_file(chunk.body,output_dir)
                total_extracted_assets += 1
            elif chunk.header.type == Dff.ChunkType.resource_catalogue:
                extract_resblock_files(chunk.body, resblock, resblock_output_dir)

        print(f"Extracted {total_extracted_assets} embedded assets.")


def extract_embedded_file(asset_body,output_path: Path) -> None:
    """Extract an embedded file from a dff."""
    output_path = output_path.joinpath(asset_body.header.name.rstrip("\x00"))
    with open(output_path, "wb") as f:
        f.write(asset_body.data)

def extract_resblock_files(catalogue_body, resblock: ExistingFile, output_dir: Path) -> None:
    """Extract all files from the dff files accompanying resblock file."""
    total_extracted_assets = 0
    with open(resblock, "rb") as resblock_f:
        for entry in catalogue_body.entries:
            name = entry.name.rstrip("\x00")
            if not name:
                continue

            resblock_f.seek(entry.ofs_resource)

            if entry.compressed_size == 0xFFFFFFFF:
                # Sentinel: stored uncompressed, read len_resource bytes directly
                data = resblock_f.read(entry.len_resource)
                total_extracted_assets += 1
            else:
                # Read the full padded block, then take the zlib stream from the end
                block = resblock_f.read(entry.compressed_size)
                zlib_start = entry.compressed_size - entry.actual_compressed_size
                try:
                    data = zlib.decompress(block[zlib_start:])
                    total_extracted_assets += 1
                except zlib.error as e:
                    print(f"Failed to decompress {entry.name.rstrip('\x00')}: {e}")

            output_path = output_dir / name
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, "wb") as out_f:
                out_f.write(data)
    
    print(f"Extracted {total_extracted_assets} resblock assets.")