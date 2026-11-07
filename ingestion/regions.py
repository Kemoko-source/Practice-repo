def normalize_region(region_name: str) -> str:
    """Return a cleaned-up region name in a predictable format."""
    if not region_name:
        return "unknown"

    cleaned = region_name.strip().replace("_", " ").title()
    return cleaned
