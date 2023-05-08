from pydantic import BaseModel, validator
from urllib.parse import urlparse


class LongUrlDto(BaseModel):
    long_url: str

    @validator('long_url')
    def validate_url(cls, value) -> None:
        parsed_url = urlparse(value)
        if not (parsed_url.scheme in ['https', 'http'] and parsed_url.netloc):
            raise ValueError("Invalid URL")
        return value


class UrlDto(BaseModel):
    long_url: str
    short_url: str
