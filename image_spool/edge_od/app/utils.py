import json
import os
import time
from concurrent import futures
from typing import Optional

import requests
from dotenv import load_dotenv

executor = futures.ThreadPoolExecutor(max_workers=1)


load_dotenv()

time_delay = float(os.environ["TIME_DELAY"])

CONFIG: dict[str, Optional[float]] = {
    "last_time": None,
}


def send_data(image: bytes, detections: dict) -> None:
    """
    POST image and detections to API to record detection event.

    :param image: (bytes) image.
    :param detections: (dict) detections reported by AI model.
    """

    current_time = time.perf_counter()

    if CONFIG["last_time"] is None:
        CONFIG["last_time"] = current_time
        return

    if current_time - CONFIG["last_time"] < 5:  # seconds
        CONFIG["last_time"] = current_time
        return

    class_name = detections[0].categories[0].category_name
    os.write(1, f"Sending data for {class_name} \n".encode())

    multipart = [
        ("meta", (None, json.dumps(detections).encode("UTF-8"), "application/json")),
        ("image", ("event.jpeg", image, "image/jpeg")),
    ]

    requests.post(
        url="http://localhost:8081",
        data={},
        files=multipart,
        timeout=30,
    )
