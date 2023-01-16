"""Provides default action for executing python package"""
import os

from aiohttp import web

from app import app

if __name__ == "__main__":
    port = int(os.environ['PORT']) if 'PORT' in os.environ else 80
    web.run_app(app, port=port)
