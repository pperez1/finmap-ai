import os
import json
import re
import anthropic

client = anthropic.Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

STANDARD_SCHEMA = ["Revenue", "OperatingCost", "DSCR"]


# -----------------------------
# RULE-BASED
# -----------------------------
def rule_map(columns):
    mapping = {}

    for col in columns:
        c = col.lower()

        if "rev" in c:
            mapping["Revenue"] = col
        elif "cost" in c or "opex" in c:
            mapping["OperatingCost"] = col
        elif "dscr" in c:
            mapping["DSCR"] = col

    return mapping


# -----------------------------
# SAFE JSON PARSER
# -----------------------------
def parse_ai_output(text):
    try:
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if not match:
            return None
        return json.loads(match.group())
    except:
        return None


# -----------------------------
# AI MAPPING
# -----------------------------
def ai_map(columns):
    prompt = f"""
Map columns to schema: {STANDARD_SCHEMA}

Return ONLY JSON:
{{
  "mapping": {{
    "Revenue": "column"
  }},
  "confidence": 0.0
}}

Columns:
{columns}
"""

    try:
        response = client.messages.create(
            model="claude-haiku-4-5",
            max_tokens=300,
            messages=[{"role": "user", "content": prompt}]
        )

        raw = response.content[0].text
        parsed = parse_ai_output(raw)

        if not parsed:
            return {"mapping": {}, "confidence": 0}

        return parsed

    except Exception as e:
        print("AI ERROR:", e)
        return {"mapping": {}, "confidence": 0}


# -----------------------------
# HYBRID ENGINE
# -----------------------------
def hybrid_map(columns):
    rules = rule_map(columns)
    ai = ai_map(columns)

    mapping = {**rules, **ai.get("mapping", {})}

    missing = [
        f for f in STANDARD_SCHEMA
        if f not in mapping
    ]

    unmapped = [
        c for c in columns
        if c not in mapping.values()
    ]

    return {
        "mapping": mapping,
        "confidence": ai.get("confidence", 0),
        "missing_fields": missing,
        "unmapped_columns": unmapped
    }