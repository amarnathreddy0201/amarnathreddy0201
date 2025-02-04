import cv2
import numpy as np

polygon_points = [(40,48) ,(883,117),(835,402),(30,449)]

original_polygon_points = np.array([[40,48] ,[883,117],[835,402],[30,449]],np.int32)


image = cv2.imread(r"C:\Users\amarn\OneDrive\Pictures\signature.jpeg",1)

new_image_size = (640, 480, 3)

original_image_size = image.shape


# Scale the polygon coordinates to fit the resized image
scaled_polygon_points = (original_polygon_points * [new_image_size[1] / original_image_size[1], 
                                                  new_image_size[0] / original_image_size[0]]).astype(int)

# Draw the scaled polygon on the resized image
# resized_image_with_polygon = image.copy()

resized_image_with_polygon = cv2.resize(image,(640,480))

cv2.polylines(resized_image_with_polygon, [scaled_polygon_points], isClosed=True, color=(0, 0, 255), thickness=2)

# Display the image with the polygon
cv2.imshow("Image with Polygon", resized_image_with_polygon)
cv2.waitKey(0)
cv2.destroyAllWindows()

# cv2.polylines(image,[np.array(polygon_points)],True,(0,0,255),5)


cv2.imshow("image",image)
cv2.waitKey(0)
