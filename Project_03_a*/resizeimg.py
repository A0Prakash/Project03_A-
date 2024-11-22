import cv2
img=cv2.imread("images/2024_Field_Crop.png")
print('resizing...')
resized_image = cv2.resize(img, (649*2,319*2), interpolation=cv2.INTER_CUBIC)
print('done')
cv2.imwrite("n2024.png", resized_image)

