import cv2
import numpy as np
from matplotlib import pyplot as plt





def hw2_2_1():

	# matplotlib  use RGB,cv use BGR
	img_rgb = cv2.imread('ncc_img.jpg',4)
	img_rgb = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2RGB)



	img = cv2.imread('ncc_img.jpg',0)
	img2 = img.copy()
	template = cv2.imread('ncc_template.jpg',0)
	w, h = template.shape[::-1]


	# print(img.shape)
	# print(w,h)

	# All the 6 methods for comparison in a list
	# methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
	#             'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
	methods = ['cv2.TM_CCORR_NORMED']
	for meth in methods:
		img = img2.copy()
		method = eval(meth)

		# Apply template Matching
		res = cv2.matchTemplate(img,template,method)
		# print(res)
	    # min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

	    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
	    # print(min_val,max_val)
	    # if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
	        # top_left = min_loc
	    # else:
	        # top_left = max_loc
	    # bottom_right = (top_left[0] + w, top_left[1] + h)

		max5=np.sort(res,axis=None)[::-1][4]
		threshold = max5
		loc = np.where( res >= threshold)
		# print(loc)
		for pt in zip(*loc[::-1]):
			# print(pt)
			cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 3)



		plt.subplot(122),plt.imshow(res,cmap = 'gray')
		plt.title('Template matching feature'), plt.xticks([]), plt.yticks([])
		plt.subplot(121),plt.imshow(img_rgb)
		plt.title('ncc_img.jpg'), plt.xticks([]), plt.yticks([])
		plt.suptitle(meth)

		plt.show()














