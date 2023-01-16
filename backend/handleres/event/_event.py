"""Provides handlers for '/event' endpoints"""
import datetime
from dataclasses import asdict
from typing import TYPE_CHECKING, Any, cast, Optional

from aiohttp.web import Response
import aiohttp.hdrs

from models.event import Event

from .._shared import (
    encode_response_body,
    generate_response_headers,
)

if TYPE_CHECKING:
    from aiohttp.web import Request


def _format_event_view(event: "Event", /) -> dict[str, Any]:
    event_dict = asdict(event)
    del event_dict["image"]["content"]
    return event_dict


async def _event_post_handler(request: "Request"):
    request_multipart = await request.multipart()

    meta: dict[str, Any] = {}

    while True:
        part = await request_multipart.next()

        if part is None:
            break

        part = cast(aiohttp.multipart.BodyPartReader, part)

        if part.headers[aiohttp.hdrs.CONTENT_TYPE] == "application/json":
            _meta = await part.json()
            if _meta:
                meta = _meta
            continue

        content = await part.read(decode=False)

        name = cast(str, part.filename)
        _type = part.headers[aiohttp.hdrs.CONTENT_TYPE]
        size = len(content)

    event = Event(
        image={
            "name": name,
            "type": _type,
            "size": size,
            "dims": (0, 0),
            "content": content,
        },
        meta=meta,
    )

    await event.save()

    return Response(
        status=200, headers=generate_response_headers(), body={"event_uid": event.uid}
    )


async def _event_get_handler(
    request: "Request",
):
    page = 1
    create_time: Optional[str] = None

    if "page" in request.query:
        page = int(request.query["page"])

    if "create_time" in request.query:
        create_time = request.query["create_time"]

    events = await Event.find_paginated_by_create_time_optional(
        page=page,
        create_time=create_time,
    )

    events_view = [_format_event_view(event) for event in events]

    return Response(
        status=200,
        headers=generate_response_headers(),
        body=encode_response_body({"events": events_view}),
    )


async def _event_count_handler(
    request: "Request",
):
    create_time: Optional[str] = None

    if "create_time" in request.query:
        create_time = request.query["create_time"]

    events_count = await Event.count(create_time=create_time)

    return Response(
        status=200,
        headers=generate_response_headers(),
        body=encode_response_body({"events_count": events_count}),
    )
