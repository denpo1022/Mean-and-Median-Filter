import numpy as np
import matplotlib.pyplot as plt
import random
import cv2
import math


def SaltAndPaper(image, density):
    # create an empty array with same size as input image
    output = np.zeros(image.shape, np.uint8)

    # parameter for controlling how much salt and paper are added
    threshhold = 1 - density

    # loop every each pixel and decide add the noise or not base on threshhold (density)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            possibility = random.random()
            if possibility < density:
                output[i][j] = 0
            elif possibility > threshhold:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output


def MeanFilter(image, filter_size):
    # create an empty array with same size as input image
    output = np.zeros(image.shape, np.uint8)

    # creat an empty variable
    result = 0

    # deal with filter size = 3x3
    if filter_size == 9:
        for j in range(1, image.shape[0]-1):
            for i in range(1, image.shape[1]-1):
                for y in range(-1, 2):
                    for x in range(-1, 2):
                        result = result + image[j+y, i+x]
                output[j][i] = int(result / filter_size)
                result = 0

    # deal with filter size = 5x5
    elif filter_size == 25:
        for j in range(2, image.shape[0]-2):
            for i in range(2, image.shape[1]-2):
                for y in range(-2, 3):
                    for x in range(-2, 3):
                        result = result + image[j+y, i+x]
                output[j][i] = int(result / filter_size)
                result = 0

    return output


def MedianFilter(image, filter_size):
    # create an empty array with same size as input image
    output = np.zeros(image.shape, np.uint8)

    # create the kernel array of filter as same size as filter_size
    filter_array = [image[0][0]] * filter_size

    # deal with filter size = 3x3
    if filter_size == 9:
        for j in range(1, image.shape[0]-1):
            for i in range(1, image.shape[1]-1):
                filter_array[0] = image[j-1, i-1]
                filter_array[1] = image[j, i-1]
                filter_array[2] = image[j+1, i-1]
                filter_array[3] = image[j-1, i]
                filter_array[4] = image[j, i]
                filter_array[5] = image[j+1, i]
                filter_array[6] = image[j-1, i+1]
                filter_array[7] = image[j, i+1]
                filter_array[8] = image[j+1, i+1]

                # sort the array
                filter_array.sort()

                # put the median number into output array
                output[j][i] = filter_array[4]

    # deal with filter size = 5x5
    elif filter_size == 25:
        for j in range(2, image.shape[0]-2):
            for i in range(2, image.shape[1]-2):
                filter_array[0] = image[j-2, i-2]
                filter_array[1] = image[j-1, i-2]
                filter_array[2] = image[j, i-2]
                filter_array[3] = image[j+1, i-2]
                filter_array[4] = image[j+2, i-2]
                filter_array[5] = image[j-2, i-1]
                filter_array[6] = image[j-1, i-1]
                filter_array[7] = image[j, i-1]
                filter_array[8] = image[j+1, i-1]
                filter_array[9] = image[j+2, i-1]
                filter_array[10] = image[j-2, i]
                filter_array[11] = image[j-1, i]
                filter_array[12] = image[j, i]
                filter_array[13] = image[j+1, i]
                filter_array[14] = image[j+2, i]
                filter_array[15] = image[j-2, i+1]
                filter_array[16] = image[j-1, i+1]
                filter_array[17] = image[j, i+1]
                filter_array[18] = image[j+1, i+1]
                filter_array[19] = image[j+2, i+1]
                filter_array[20] = image[j-2, i+2]
                filter_array[21] = image[j-1, i+2]
                filter_array[22] = image[j, i+2]
                filter_array[23] = image[j+1, i+2]
                filter_array[24] = image[j+2, i+2]

                # sort the array
                filter_array.sort()

                # put the median number into output array
                output[j][i] = filter_array[12]
    return output


def main():
    # read image
    gray_lena = cv2.imread('lena.png', 0)

    # add salt and paper (0.01 is a proper parameter)
    noise_lena = SaltAndPaper(gray_lena, 0.01)

    # use 3x3 mean filter
    mean_3x3_lena = MeanFilter(noise_lena, 9)

    # use 3x3 median filter
    median_3x3_lena = MedianFilter(noise_lena, 9)

    # use 3x3 mean filter
    mean_5x5_lena = MeanFilter(noise_lena, 25)

    # use 5x5 median filter
    median_5x5_lena = MedianFilter(noise_lena, 25)

    # set up side-by-side image display
    fig = plt.figure()
    fig.set_figheight(10)
    fig.set_figwidth(8)

    # display the oringinal image
    fig.add_subplot(3, 2, 1)
    plt.title('Original Image')
    plt.imshow(gray_lena, cmap='gray')

    # display the salt and paper image
    fig.add_subplot(3, 2, 2)
    plt.title('Adding Salt & Paper Image')
    plt.imshow(noise_lena, cmap='gray')

    # display 3x3 mean filter
    fig.add_subplot(3, 2, 3)
    plt.title('3x3 Mean Filter')
    plt.imshow(mean_3x3_lena, cmap='gray')

    # display 3x3 median filter
    fig.add_subplot(3, 2, 4)
    plt.title('3x3 Median Filter')
    plt.imshow(median_3x3_lena, cmap='gray')

    # display 5x5 median filter
    fig.add_subplot(3, 2, 5)
    plt.title('5x5 Mean Filter')
    plt.imshow(mean_5x5_lena, cmap='gray')

    # display 5x5 median filter
    fig.add_subplot(3, 2, 6)
    plt.title('5x5 Median Filter')
    plt.imshow(median_5x5_lena, cmap='gray')

    plt.show()


if __name__ == "__main__":
    main()
