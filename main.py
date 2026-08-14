from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict
from ai_service import enrich_product
from research_service import research_product

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# What the user provides
class ProductInput(BaseModel):
    brand: str
    mpn: str
    description: str


# What our system produces
class ProductIntelligence(BaseModel):
    product_name: str
    brand: str
    mpn: str
    category: str
    description: str
    features: List[str]
    applications: List[str]
    specifications: Dict[str, str]
    keywords: List[str]
    confidence: float
    completeness: float


@app.get("/")
def home():
    return {
        "message": "Product Intelligence API is running!"
    }


@app.post("/product")
def create_product(product: ProductInput):

    research = research_product(
        product.brand,
        product.mpn,
        product.description
    )

    result = enrich_product(
        product.brand,
        product.mpn,
        product.description,
        research["sources"]
    )

    return result

@app.post("/research")
def research(product: ProductInput):

    result = research_product(
        product.brand,
        product.mpn,
        product.description
    )

    return result