"""Provides objects shared across backend handlers"""

import datetime
import json
import secrets
from collections import namedtuple
from typing import TYPE_CHECKING, Any, Optional

from multidict import MultiDict

if TYPE_CHECKING:
    from aiohttp.web import Request

RequestSessionUserResults = namedtuple("RequestSessionUserResults", ["session", "user"])


class AppJSONEncoder(json.JSONEncoder):
    """JSONEncoder implementation that converts 'datetime' objects to str"""

    def default(self, o):
        if isinstance(o, datetime.datetime):
            return o.isoformat()

        if isinstance(o, bytes):
            return True

        try:
            return json.JSONEncoder.default(self, o)
        except TypeError:
            return str(o)


_app_encoder = AppJSONEncoder()


def encode_response_body(body: dict[str, Any]) -> bytes:
    """
    Encodes 'dict' object for 'Response' as 'JSON' string
    """

    return _app_encoder.encode(body).encode("utf-8")


def generate_response_headers(content_type: Optional[str] = None) -> "MultiDict":
    """
    Generates 'MultiDict' object containing default headers to be used with 'Response' object in
    handler functions
    """

    return MultiDict(
        [
            ("Access-Control-Allow-Origin", "*"),
            ("Access-Control-Allow-Methods", "GET,POST,OPTIONS"),
            ("Access-Control-Allow-Headers", "Content-Type, Authorization"),
            ("Access-Control-Expose-Headers", "Content-Disposition"),
            ("Content-Type", content_type or "application/json; charset=utf-8"),
        ]
    )
