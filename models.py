from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, HttpUrl

class ProductItem(BaseModel):
    title: str = Field(..., description="Full name or title of the product")
    price: float = Field(..., description="Price in base currency")
    currency: str = Field(default="GBP", description="Currency symbol or ISO code")
    rating: int = Field(default=0, ge=0, le=5, description="Star rating from 1 to 5")
    availability: str = Field(default="In stock", description="Stock status text")
    product_url: str = Field(..., description="Canonical product URL")
    image_url: Optional[str] = Field(None, description="Product thumbnail URL")
    scraped_at: datetime = Field(default_factory=datetime.utcnow, description="UTC timestamp of extraction")
