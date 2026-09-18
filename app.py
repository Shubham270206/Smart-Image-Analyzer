import cv2
import numpy as np
import streamlit as st

from src.preprocessing import (
    convert_to_grayscale,
    apply_gaussian_blur,
    apply_threshold
)

from src.edge_detection import detect_edges

from src.contour_analysis import (
    find_contours,
    analyze_contours,
    draw_contours
)

from src.feature_extraction import (
    extract_edge_features,
    calculate_image_statistics
)

from src.visualization import convert_bgr_to_rgb


st.set_page_config(
    page_title="Smart Image Analyzer",
    page_icon="🔍",
    layout="wide"
)


st.title("🔍 Smart Image Analyzer")

st.write(
    "A Computer Vision application for image preprocessing, "
    "edge detection, contour analysis, and feature extraction."
)


uploaded_file = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png"]
)


if uploaded_file is not None:

    file_bytes = np.asarray(
        bytearray(uploaded_file.read()),
        dtype=np.uint8
    )

    image = cv2.imdecode(
        file_bytes,
        cv2.IMREAD_COLOR
    )

    if image is None:
        st.error("Unable to read the uploaded image.")
        st.stop()




    st.header("1. Image Preprocessing")

    gray = convert_to_grayscale(image)

    blurred = apply_gaussian_blur(gray)

    thresholded = apply_threshold(blurred)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image(
            convert_bgr_to_rgb(image),
            caption="Original Image",
            use_container_width=True
        )

    with col2:
        st.image(
            gray,
            caption="Grayscale Image",
            use_container_width=True
        )

    with col3:
        st.image(
            thresholded,
            caption="Thresholded Image",
            use_container_width=True
        )




    st.header("2. Edge Detection")

    edges = detect_edges(gray)

    st.image(
        edges,
        caption="Canny Edge Detection",
        use_container_width=True
    )



    st.header("3. Contour & Shape Analysis")

    contours = find_contours(thresholded)

    contour_image = draw_contours(
        image,
        contours
    )

    contour_data = analyze_contours(contours)

    st.image(
        convert_bgr_to_rgb(contour_image),
        caption=f"Detected Contours: {len(contours)}",
        use_container_width=True
    )

    if contour_data:

        st.subheader("Contour Information")

        st.dataframe(
            contour_data,
            use_container_width=True
        )

    else:

        st.info("No external contours detected.")


    st.header("4. Feature Extraction")

    edge_features = extract_edge_features(gray)

    statistics = calculate_image_statistics(image)

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Image Statistics")

        for key, value in statistics.items():

            st.write(
                f"**{key.replace('_', ' ').title()}:** {value}"
            )


    with col2:

        st.subheader("Edge Features")

        st.write(
            f"Edge pixels: "
            f"**{edge_features['edge_pixels']}**"
        )

        st.write(
            f"Edge density: "
            f"**{edge_features['edge_density']}**"
        )

        st.write(
            "Edge features describe the amount of "
            "structural information present in the image."
        )



    st.header("Analysis Summary")

    st.success(
        f"Image processed successfully. "
        f"{len(contours)} external contours detected "
        f"and {edge_features['edge_pixels']} edge pixels analyzed."
    )


else:

    st.info(
        "Upload a JPG, JPEG, or PNG image to begin analysis."
    )