from typing import Callable, TYPE_CHECKING

from aiohttp import web

from handleres._shared import generate_response_headers
from handleres.image import _image_get_handler
from handleres.event import (
    _event_count_handler,
    _event_get_handler,
    _event_post_handler,
)


if TYPE_CHECKING:
    from aiohttp.web import RouteDef

app = web.Application()


async def _root_hander(_):
    return web.Response(text="hello, world!")


async def _options_hander(_):
    return web.Response(status=200, headers=generate_response_headers())


def post_and_options(endpoint: str, handler: Callable) -> tuple["RouteDef", "RouteDef"]:
    return (web.options(endpoint, _options_hander), web.post(endpoint, handler))


def get_and_options(endpoint: str, handler: Callable) -> tuple["RouteDef", "RouteDef"]:
    return (web.options(endpoint, _options_hander), web.get(endpoint, handler))


app.add_routes(
    [
        web.get("/", _root_hander),
        web.get("/image/{uid}/{name}", _image_get_handler),
        *post_and_options("/event", _event_post_handler),
        web.get("/event", _event_get_handler),
        web.get("/event/count", _event_count_handler),
    ]
)
