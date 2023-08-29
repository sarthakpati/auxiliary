from .percentile_normalizer import PercentileNormalizer
from .windowing_normalizer import WindowingNormalizer


def normalize_with_percentiles(
    image, lower_percentile, upper_percentile, lower_limit, upper_limit
):
    """
    Normalize an input image using percentile-based normalization.

    Parameters:
        image (numpy.ndarray): The input image.
        lower_percentile (float): The lower percentile for mapping.
        upper_percentile (float): The upper percentile for mapping.
        lower_limit (float): The lower limit for normalized values.
        upper_limit (float): The upper limit for normalized values.

    Returns:
        numpy.ndarray: The normalized image.
    """
    # Create an instance of the PercentileNormalizer class
    normalizer = PercentileNormalizer(
        lower_percentile, upper_percentile, lower_limit, upper_limit
    )

    # Call the normalize method of the normalizer instance
    normalized_image = normalizer.normalize(image)

    return normalized_image


def normalize_with_windowing(image, center, width):
    """
    Normalize an input image using windowing-based normalization.

    Parameters:
        image (numpy.ndarray): The input image.
        center (float): The window center.
        width (float): The window width.

    Returns:
        numpy.ndarray: The normalized image.
    """
    # Create an instance of the WindowingNormalizer class
    normalizer = WindowingNormalizer(center, width)

    # Call the normalize method of the normalizer instance
    normalized_image = normalizer.normalize(image)

    return normalized_image
