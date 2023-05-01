from .Utils import get_random_string, validate_url
from ..models import UrlEntity


def add_long_url(long_url: str) -> UrlEntity:
    validate_url(url=long_url)
    short_url = get_random_string(8)
    entity = UrlEntity.objects.create(long_url=long_url, short_url=short_url)
    return entity


def get_short_url(url: str) -> str:
    return UrlEntity.objects.get(short_url=url).long_url
