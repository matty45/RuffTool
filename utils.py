"""Misc util functions"""

def obj_to_dict(obj):
    """Convert a object to a JSON-serializable dictionary."""
    if hasattr(obj, '__dict__'):
        result = {}
        for key, value in obj.__dict__.items():
            # Skip internal attributes
            if key.startswith('_'):
                continue
            # Handle nested objects
            if hasattr(value, '__dict__'):
                result[key] = obj_to_dict(value)
            # Handle lists
            elif isinstance(value, list):
                result[key] = [obj_to_dict(item) if hasattr(item, '__dict__') else item for item in value]
            # Handle enums
            elif hasattr(value, 'value'):
                result[key] = value.value
            # Handle bytes
            elif isinstance(value, bytes):
                result[key] = value.hex()
            else:
                result[key] = value
        return result
    return obj
