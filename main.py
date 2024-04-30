# imports the OpenCV library
import cv2  


source = 'vk1.jpeg'
destination = 'newImage.png'
# the image will be resize to 50% of its original size.
scale_image = 50


image = cv2.imread(source)
# cv2.imshow('title',image)

new_width = int(image.shape[1] * scale_image / 100 )
new_height = int(image.shape[0] * scale_image / 100 )


output = cv2.resize(image, (new_width, new_height))


cv2.imwrite(destination, output)
cv2.waitKey(0)