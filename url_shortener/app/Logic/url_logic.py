
from .Utils import get_random_string
from .dto import LongUrlDto, UrlDto
from ..models import UrlEntity


def add_long_url(long_url_dto: LongUrlDto) -> UrlDto:
    short_url = get_random_string(8)
    url_dto = UrlDto(short_url=short_url, long_url=long_url_dto.long_url)
    return UrlDto(**UrlEntity.objects.create(**url_dto.dict()).__dict__)


def get_short_url(url: str) -> str:
    return UrlEntity.objects.get(short_url=url).long_url
