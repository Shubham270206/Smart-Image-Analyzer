import cv2


def convert_to_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def apply_gaussian_blur(gray_image, kernel_size=5):
    return cv2.GaussianBlur(
        gray_image,
        (kernel_size, kernel_size),
        0
    )


def apply_threshold(gray_image):
    _, thresholded = cv2.threshold(
        gray_image,
        127,
        255,
        cv2.THRESH_BINARY
    )

    return thresholded