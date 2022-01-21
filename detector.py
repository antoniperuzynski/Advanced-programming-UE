import time
import cv2
import numpy
import imutils
from imutils.object_detection import non_max_suppression


def apply_non_max_suppression(coordinates: list) -> list:
    coordinates = numpy.array([[x, y, x + w, y + h] for (x, y, w, h) in coordinates])
    return non_max_suppression(coordinates, probs=None, overlapThresh=0.65)


descriptor = cv2.HOGDescriptor()
descriptor.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())


def detectpeople(path: str) -> list:
    image = cv2.imread(path)
    image = imutils.resize(image, width=min(800, image.shape[1]))
    start = time.time()
    coordinates, weights = descriptor.detectMultiScale(image, winStride=(5, 5), padding=(16, 16), scale=1.2)
    coordinates = apply_non_max_suppression(coordinates)
    end = time.time()
    number = 0
    for i, (x, y, w, h) in enumerate(coordinates):
        if weights[i] > 0.2:
            cv2.rectangle(image, (x + 10, y - 10), (w - 10, h + 10), (127, 255, 0), 2)
            number += 1
    cv2.putText(image, f'Total persons detected : {number}', (40, 40), cv2.FONT_HERSHEY_TRIPLEX, 0.7, (127, 255, 0), 2)
    cv2.putText(image, f'Detected in time \'{(end - start):.3f}', (40, 70), cv2.FONT_HERSHEY_TRIPLEX, 0.7,
                (127, 255, 0), 2)
    return image


def print_result(image: list) -> None:
    cv2.imshow("image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
