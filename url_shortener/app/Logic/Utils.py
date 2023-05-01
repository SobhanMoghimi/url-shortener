import random
import string

from urllib.parse import urlparse


def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def validate_url(url: str) -> None:
    parsed_url = urlparse(url)
    if not ((parsed_url.scheme == 'https' or parsed_url.scheme == 'http') and parsed_url.netloc):
        raise ValueError("Invalid URL")

