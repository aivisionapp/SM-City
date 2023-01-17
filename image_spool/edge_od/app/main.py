import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor

import cv2
from dotenv import load_dotenv
from tflite_support.task import core, processor, vision

import utils

executor = ThreadPoolExecutor()

load_dotenv()

selected_model = os.environ["MODEL_NAME"]


ip_camera_url = os.environ["CAMERA_URL"]

trushold = float(os.environ["TRUSHOLD"])

DEFAULT_WIDTH = 640
DEFAULT_HEIGHT = 480


def run(
    model: str = selected_model,
    camera_id: str = ip_camera_url,
    width: int = DEFAULT_WIDTH,
    height: int = DEFAULT_HEIGHT,
    num_threads: int = 4,
) -> None:

    cap = cv2.VideoCapture(camera_id)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    base_options = core.BaseOptions(
        file_name=model, use_coral=False, num_threads=num_threads
    )
    detection_options = processor.DetectionOptions(
        max_results=3, score_threshold=trushold
    )
    options = vision.ObjectDetectorOptions(
        base_options=base_options, detection_options=detection_options
    )
    detector = vision.ObjectDetector.create_from_options(options)

    while cap.isOpened():
        success, image = cap.read()
        if not success:
            sys.exit("ERROR: Unable to read from camera feed")
        # reduce the loop speed
        time.sleep(0.01)

        image = cv2.flip(image, 1)

        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        input_tensor = vision.TensorImage.create_from_array(rgb_image)

        detection_result = detector.detect(input_tensor)

        if len(detection_result.detections) > 0:
            executor.submit(utils.send_data, image, detection_result.detections)

    cap.release()
    cv2.destroyAllWindows()


def main():
    run()


if __name__ == "__main__":
    main()
