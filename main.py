import numpy as np
import matplotlib.pyplot as plt
import random
import cv2


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
    pass


def MedianFilter(image, filter_size):
    # create an empty array with same size as input image
    output = np.zeros(image.shape, np.uint8)

    # deal with filter size = 9
    if filter_size == 9:
        filter_array = [image[0][0]] * filter_size
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
    return output


def main():
    # read image
    gray_lena = cv2.imread('lena.png', 0)

    # add salt and paper
    noise_lena = SaltAndPaper(gray_lena, 0.005)

    # use 3x3 median filter
    median_3x3_lena = MedianFilter(noise_lena, 9)

    # set up side-by-side image display
    fig = plt.figure()
    fig.set_figheight(15)
    fig.set_figwidth(10)

    # display the oringinal image
    fig.add_subplot(3, 2, 1)
    plt.title('Original Image')
    plt.imshow(gray_lena, cmap='gray')

    # display the salt and paper image
    fig.add_subplot(3, 2, 2)
    plt.title('Adding Salt & Paper Image')
    plt.imshow(noise_lena, cmap='gray')

    # display 3x3 median filter
    fig.add_subplot(3, 2, 4)
    plt.title('3x3 Median Filter')
    plt.imshow(median_3x3_lena, cmap='gray')

    plt.show()


if __name__ == "__main__":
    main()
