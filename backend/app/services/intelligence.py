def compute_confidence(source: str) -> float:
    if source == "rule":
        return 0.95
    if source == "ai":
        return 0.75
    return 0.5


def explain_mapping(column, matched_field, source):
    if source == "rule":
        return f"Matched via deterministic keyword rules for financial schema alignment."
    if source == "ai":
        return f"AI semantic match based on financial context similarity."
    return f"Heuristic fallback match for ambiguous column."

def build_mapping(field, match, source):
    return {
        "column": match,
        "confidence": compute_confidence(source),
        "explanation": explain_mapping(field, match, source)
    }