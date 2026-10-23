import cv2
img=cv2.imread(r"C:\Users\user\Downloads\pic1.jpeg",0)
print(img)
status = cv2.imwrite('pic1.jpeg',img)
print("Image written to file-system : ", status)
