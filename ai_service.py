import re

def extract_specifications(text):

    specifications = {}

    patterns = {
        "Voltage": r"(\d+(?:\.\d+)?)\s*(?:V|volt|volts)\b",
        "Weight": r"(\d+(?:\.\d+)?)\s*(?:kg|kilograms?|g)\b",
        "Speed": r"(\d+(?:,\d+)*)\s*(?:rpm|r/min)\b",
        "Power": r"(\d+(?:\.\d+)?)\s*(?:W|watts?|kW)\b",
        "Capacity": r"(\d+(?:\.\d+)?)\s*(?:Ah|mAh|L|litres?|liters?)\b"
    }

    for name, pattern in patterns.items():

        match = re.search(
            pattern,
            text,
            re.IGNORECASE
        )

        if match:
            specifications[name] = match.group(0)

    return specifications

def enrich_product(brand, mpn, description, sources):

    text = ""

    for source in sources:
        text += " " + source["content"]

    text = text.lower()

    # Category
    category = "Industrial Product"

    if "drill" in text or "drilling" in text:
        category = "Power Tools"
    elif "pump" in text:
        category = "Industrial Pumps"
    elif "motor" in text:
        category = "Electric Motors"
    elif "sensor" in text:
        category = "Industrial Sensors"

    # Features
    features = []

    if "battery" in text:
        features.append("Battery powered")

    if "cordless" in text:
        features.append("Cordless operation")

    if "compact" in text:
        features.append("Compact design")

    if "lightweight" in text:
        features.append("Lightweight design")

    if not features:
        features.append("Product features identified from research")

    # Applications
    applications = []

    if category == "Power Tools":
        applications = [
            "Drilling",
            "Installation",
            "Maintenance"
        ]

    elif category == "Industrial Pumps":
        applications = [
            "Fluid transfer",
            "Industrial systems"
        ]

    elif category == "Electric Motors":
        applications = [
            "Industrial machinery",
            "Equipment drives"
        ]

    elif category == "Industrial Sensors":
        applications = [
            "Monitoring",
            "Automation"
        ]

    else:
        applications = [
            "Industrial applications"
        ]

    # Keywords
    keywords = [
        brand,
        mpn,
        category
    ]

    # Source information
    source_list = []

    for source in sources:
        source_list.append({
            "title": source["title"],
            "url": source["url"],
            "relevance": source["relevance"]
        })

    return {
        "product": {
            "name": f"{brand} {mpn}",
            "brand": brand,
            "mpn": mpn,
            "description": description
        },

        "classification": {
            "category": category
        },

        "features": features,

        "applications": applications,

        "specifications": extract_specifications(text),

        "keywords": keywords,

        "quality": {
            "confidence": 0.75,
            "completeness": 0.60,
            "source_count": len(sources)
        },

        "sources": source_list
    }