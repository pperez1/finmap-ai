def hybrid_map(columns):
    mapping = {}

    for col in columns:
        c = col.lower()

        if "revenue" in c:
            mapping["Revenue"] = col
        elif "cost" in c:
            mapping["OperatingCost"] = col
        elif "dscr" in c:
            mapping["DSCR"] = col

    return mapping