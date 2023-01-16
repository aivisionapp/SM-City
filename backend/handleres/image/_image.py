"""Provides handlers for '/image' endpoints"""

from typing import TYPE_CHECKING

from aiohttp.web import Response

from models.event import Event

from .._shared import generate_response_headers

if TYPE_CHECKING:
    from aiohttp.web import Request


async def _image_get_handler(request: "Request"):
    event = await Event.get_by_uid(uid=request.match_info["uid"])

    return Response(
        status=200,
        headers=generate_response_headers(content_type=event.image["type"]),
        body=event.image["content"],
    )
