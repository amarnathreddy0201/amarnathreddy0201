import cv2
import numpy as np
import glob
import requests
import base64


def bilateral_filter():
    # Load the noisy image
    noisy_image = cv2.imread(r"C:\Development\img\7.jpg")

    # Apply denoising
    denoised_image = cv2.fastNlMeansDenoisingColored(noisy_image, None, 1, 1, 7, 21)

    cv2.imshow("denoised_image", denoised_image)
    cv2.waitKey(0)

    # Load an image
    image = cv2.imread(r"C:\Development\AIVision-Pi\img\7.jpg")

    # Apply bilateral filter for noise reduction
    filtered_image = cv2.bilateralFilter(
        denoised_image, d=9, sigmaColor=15, sigmaSpace=25
    )

    # Save or display the filtered image
    cv2.imshow("filtered_image.jpg", filtered_image)
    cv2.waitKey(0)


def channels_checking():
    # C:\Development\new\AIVision-Pi\logo.png
    # Load a color image
    image = cv2.imread(r"C:\Development\img\7.jpg", 1)

    # Split the color channels (BGR format in OpenCV)
    blue_channel, green_channel, red_channel = cv2.split(image)

    # Display the individual color channels using cv2.imshow
    cv2.imshow("Red Channel", red_channel)
    cv2.imshow("Green Channel", green_channel)
    cv2.imshow("Blue Channel", blue_channel)
    cv2.imshow("image", image)

    # Wait for a key press and then close the image windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def guided_filter():
    # Load the input image
    input_image = cv2.imread(r"C:\Development\img\7.jpg", 1)

    # Convert the input image to grayscale (if it's not already grayscale)
    if input_image.shape[2] == 3:
        input_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

    # Create a placeholder for the output image
    output_image = np.zeros_like(input_image)

    # Create a window size for the guided filter
    window_size = 5

    # Apply the guided filter
    output_image = cv2.ximgproc.guidedFilter(
        guide=input_image, src=input_image, radius=window_size, eps=0.05
    )

    # Display or save the output image
    cv2.imshow("Guided Filter Result", output_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def adaptive_threshold():
    # Load the input image
    image = cv2.imread(r"C:\Development\img\7.jpg", 1)

    # Convert the input image to grayscale
    input_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    _, binary_image = cv2.threshold(input_image, 120, 255, cv2.THRESH_BINARY)

    # Apply adaptive thresholding
    adaptive_threshold = cv2.adaptiveThreshold(
        input_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
    )
    # Display the original and binary images
    cv2.imshow("Original Image", image)
    cv2.imshow("Adaptive Thresholded Image", adaptive_threshold)
    cv2.imshow("binary_image", binary_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


data = [2, 32, 1, 2321, 2, 3, 2, 1, 235, 10]


def selection_sort():
    for i in range(0, len(data) - 1):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                temp = data[i]
                data[i] = data[j]
                data[j] = temp


def insertion_sort():
    for i in range(1, len(data)):
        j = i - 1
        key = data[i]

        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key

    print(data)


# def image_segmentation():
#     images = glob.glob(
#         "C:\\Users\\Downloads\\archive (1)\\people_segmentation\\masks\\*.png"
#     )

#     for img in images:
#         image = cv2.imread(img)
#         w, h, c = image.shape
#         for i in range(0, w):
#             for j in range(0, h):
#                 image[i][j][0] += 255
#                 image[i][j][1] += 255
#                 image[i][j][2] += 250

#         cv2.imshow("image", image)
#         cv2.waitKey(0)


def guided_filter(I, p, radius=5, eps=1e-8):
    """
    Guided Filter implementation
    :param I: guidance image
    :param p: filtering input image
    :param radius: window size
    :param eps: regularization parameter
    :return: filtered image
    """
    # Convert the images to float32
    I, p = I.astype(np.float32), p.astype(np.float32)

    # Precompute mean of I, p and cross-correlation terms
    mean_i = cv2.boxFilter(I, -1, (radius, radius))
    mean_p = cv2.boxFilter(p, -1, (radius, radius))
    mean_ip = cv2.boxFilter(I * p, -1, (radius, radius))
    cov_ip = mean_ip - mean_i * mean_p

    # Precompute mean of I * I and variance of I
    mean_ii = cv2.boxFilter(I * I, -1, (radius, radius))
    var_i = mean_ii - mean_i * mean_i

    # Compute 'a' and 'b'
    a = cov_ip / (var_i + eps)
    b = mean_p - a * mean_i

    # Compute mean of 'a' and 'b' using a window filter
    mean_a = cv2.boxFilter(a, -1, (radius, radius))
    mean_b = cv2.boxFilter(b, -1, (radius, radius))

    # Compute the output image q
    q = mean_a * I + mean_b

    return q


def checking_guided_filter():
    # Read the input image
    input_image = cv2.imread(
        r"C:\Development\img\7.jpg"
    )  # Replace 'input_image.jpg' with your image file

    # Convert the image to float32 and scale it to [0, 1]
    input_image1 = input_image.astype(np.float32) / 255.0

    # Apply the guided filter using the input image itself as the guidance image
    filtered_image = guided_filter(input_image1, input_image1, radius=5, eps=1e-8)

    # Display the original and filtered images
    cv2.imshow("Original Image", input_image)
    cv2.imshow("Filtered Image", filtered_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def anisotropic_diffusion(image, iterations=100, delta=0.0001, kappa=30):
    """
    Anisotropic diffusion for image edge detection.

    Parameters:
    - image: Input image (grayscale).
    - iterations: Number of iterations.
    - delta_t: Time step.
    - kappa: Perona-Malik diffusion coefficient.

    Returns:
    - Diffused image.
    """
    img = np.float32(image)
    try:
        for _ in range(iterations):
            # Calculate image gradients
            gradient_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
            gradient_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

            # Convert gradients back to 8-bit unsigned integers
            gradient_x = cv2.convertScaleAbs(gradient_x)
            gradient_y = cv2.convertScaleAbs(gradient_y)

            # Calculate diffusion coefficients
            diff_coeff_x = 1 / (1 + (gradient_x / kappa) ** 2)
            diff_coeff_y = 1 / (1 + (gradient_y / kappa) ** 2)

            # Update image using the diffusion equation
            image += delta * (diff_coeff_x * gradient_x + diff_coeff_y * gradient_y)

        return image
    except Exception as error:
        print("error is :", error)


def checking_anisotropic_diffusion():
    # Read the input image
    input_image = cv2.imread(
        r"C:\Development\img\7.jpg"
    )  # Replace 'input_image.jpg' with your image file
    print(input_image.shape)

    # Convert the image to float32 and normalize it
    input_image1 = input_image.astype(np.uint8) / 255.0

    # Apply anisotropic diffusion
    result_image = anisotropic_diffusion(
        input_image1, iterations=100, delta=0.01, kappa=30
    )
    cv2.imshow("Anisotropic Diffusion Result", result_image)
    cv2.waitKey(0)

    gray = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
    print(gray.shape)

    cv2.imshow("Correct Image", input_image)
    # Display the original and result images
    cv2.imshow("Original Image", input_image1)
    cv2.imshow("Anisotropic Diffusion Result", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def guided_filering():
    # Read the guidance image (I) and the filtering image (P)
    guidance_image = cv2.imread(r"C:\Development\img\7.jpg", 1)

    # Convert the images to the required format (e.g., grayscale)
    guidance_image_gray = cv2.cvtColor(guidance_image, cv2.COLOR_BGR2GRAY)
    filtering_image_gray = cv2.cvtColor(guidance_image, cv2.COLOR_BGR2GRAY)

    # Apply the Guided Filter
    radius = 50
    eps = 0.0001
    filtered_image = cv2.ximgproc.guidedFilter(
        guidance_image_gray, filtering_image_gray, radius, eps
    )

    # Display or save the filtered image
    cv2.imshow("Filtered Image", filtered_image)
    cv2.imshow("guidance_image ", guidance_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def stretching_image():
    # Read the image
    image = cv2.imread(r"C:\Development\img\7.jpg", 1)

    # Convert to float32 for better precision
    image_float32 = image.astype(np.float32)

    # Perform linear contrast stretching
    min_val = np.min(image_float32)
    max_val = np.max(image_float32)
    stretched_image = 255 * ((image_float32 - min_val) / (max_val - min_val))

    # Convert back to uint8
    stretched_image = stretched_image.astype(np.uint8)

    # Display the results
    cv2.imshow("Original Image", image)
    cv2.imshow("Contrast Stretched Image", stretched_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
