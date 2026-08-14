import os
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

tavily = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)


def build_search_query(brand, mpn, description):
    return f"{brand} {mpn} {description}"


def search_sources(brand, mpn, description):

    query = build_search_query(
        brand,
        mpn,
        description
    )

    response = tavily.search(
        query=query,
        search_depth="basic",
        max_results=5
    )

    results = []

    for item in response["results"]:

        results.append({
            "title": item["title"],
            "url": item["url"],
            "source_type": "web",
            "content": item["content"]
        })

    return query, results


def rank_sources(results, brand, mpn):

    ranked = []

    for source in results:

        score = 0

        content = (
            source["content"] + " " +
            source["title"]
        ).lower()

        if brand.lower() in content:
            score += 30

        if mpn.lower() in content:
            score += 40

        source["relevance"] = score

        ranked.append(source)

    ranked.sort(
        key=lambda x: x["relevance"],
        reverse=True
    )

    return ranked

def extract_facts(results):

    specifications = {}

    for source in results:

        text = source["content"].lower()

        if "voltage" in text:
            specifications["voltage"] = "Found in source"

        if "weight" in text:
            specifications["weight"] = "Found in source"

        if "battery" in text:
            specifications["battery"] = "Found in source"

        if "speed" in text:
            specifications["speed"] = "Found in source"

        if "dimensions" in text:
            specifications["dimensions"] = "Found in source"

    return specifications


def research_product(brand, mpn, description):

    query, results = search_sources(
        brand,
        mpn,
        description
    )

    ranked_sources = rank_sources(
        results,
        brand,
        mpn
    )

    specifications = extract_facts(
        ranked_sources
    )

    return {
        "product": {
            "brand": brand,
            "mpn": mpn,
            "description": description
        },
        "search_query": query,
        "specifications": specifications,
        "sources": ranked_sources,
        "research_status": "completed"
    }
    return {
        "product": {
            "brand": brand,
            "mpn": mpn,
            "description": description
        },
        "search_query": query,
        "sources": ranked_sources,
        "research_status": "completed"
    }
    ranked_sources = rank_sources(
        results,
        brand,
        mpn
    )

    return {
        "product": {
            "brand": brand,
            "mpn": mpn,
            "description": description
        },
        "search_query": query,
        "sources": ranked_sources,
        "research_status": "completed"
    }