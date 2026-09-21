import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as image

rgb_images= image.imread("rgb_img.jpg")
print(rgb_images.shape)

ar=np.array(rgb_images)
print(ar.shape)
r = ar[:, :, 0]
g = ar[:, :, 1]
b = ar[:, :, 2]
print(r.shape)
print(g.shape)
print(b.shape)
r_half=r//2
print(r_half.shape)

yeni_img=np.dstack((r_half,g,b))
plt.imshow(yeni_img)
plt.show()
print(yeni_img.dtype)
plt.imsave("kirmizisi_azaltilmis.jpg", yeni_img)