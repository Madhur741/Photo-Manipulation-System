import cv2
image = cv2.imread("pic.jpg")
grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(grey_img)
blur = cv2.GaussianBlur(invert,(25,25),0)
invertedblur = cv2.bitwise_not(blur)
sketch = cv2.divide(grey_img, invertedblur, scale=200)

cv2.imwrite("pencilsketch.png", sketch)