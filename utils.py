"""Misc util functions"""

from enum import IntEnum

def obj_to_dict(obj):
    """Convert an object to a JSON-serializable dictionary."""
    if isinstance(obj, IntEnum):
        return obj.value

    if hasattr(obj, '__dict__'):
        result = {}
        for key, value in obj.__dict__.items():
            if key.startswith('_'):
                continue
            result[key] = obj_to_dict(value)
        return result

    if isinstance(obj, list):
        return [obj_to_dict(item) for item in obj]

    if isinstance(obj, bytes):
        return obj.hex()

    if isinstance(obj, str):
        return obj.rstrip('\x00')  # Strip null bytes from strings

    return obj