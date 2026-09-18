import cv2


def find_contours(binary_image):
    contours, _ = cv2.findContours(
        binary_image,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    return contours


def analyze_contours(contours):
    contour_data = []

    for index, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        perimeter = cv2.arcLength(contour, True)

        x, y, width, height = cv2.boundingRect(contour)

        contour_data.append({
            "id": index + 1,
            "area": round(area, 2),
            "perimeter": round(perimeter, 2),
            "width": width,
            "height": height
        })

    return contour_data


def draw_contours(image, contours):
    result = image.copy()

    cv2.drawContours(
        result,
        contours,
        -1,
        (0, 255, 0),
        2
    )

    return result