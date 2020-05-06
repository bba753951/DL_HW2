import cv2
import numpy as np
from matplotlib import pyplot as plt
import heapq


def drawPT(img_name):
	img = cv2.imread(img_name, cv2.IMREAD_GRAYSCALE)

	sift = cv2.xfeatures2d.SIFT_create()

	keypoints_sift, descriptors = sift.detectAndCompute(img, None)

	kp_size=[keypoints_sift[i].size for i in range(len(keypoints_sift))]


	max_kp_index_list = map(kp_size.index, heapq.nlargest(20, kp_size))
	max_kp_index_list=list(max_kp_index_list)
	kp_max6=[keypoints_sift[i] for i in max_kp_index_list]

	count=0
	pos=[]
	final_max6=[]
	for i in kp_max6:
		if i.pt not in pos:
			pos.append(i.pt)
			final_max6.append(i)
			count+=1;
			if count ==6:
				break
	# print(final_max6)


	img = cv2.drawKeypoints(img, final_max6, None)

	# cv2.namedWindow('image')
	cv2.imwrite('Feature'+img_name,img)
	cv2.imshow(img_name, img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
def hw2_3_1():
	drawPT("Aerial1.jpg")
	drawPT("Aerial2.jpg")


def findmax6(keypoints_sift,des):
	kp_size=[keypoints_sift[i].size for i in range(len(keypoints_sift))]


	max_kp_index_list = map(kp_size.index, heapq.nlargest(20, kp_size))
	max_kp_index_list=list(max_kp_index_list)
	kp_max6=[keypoints_sift[i] for i in max_kp_index_list]

	count=0
	pos=[]
	final_max6=[]
	des_max6=[]
	index_max6=[]
	for i in max_kp_index_list:
		if keypoints_sift[i].pt not in pos:
			pos.append(keypoints_sift[i].pt)
			final_max6.append(keypoints_sift[i])
			des_max6.append(des[i])
			index_max6.append(i)
			count+=1;
			if count ==6:
				break
	return final_max6,index_max6,des_max6



def drawMatch():
	img1 = cv2.imread("Aerial1.jpg", cv2.IMREAD_GRAYSCALE)
	img2 = cv2.imread("Aerial2.jpg", cv2.IMREAD_GRAYSCALE)

	sift = cv2.xfeatures2d.SIFT_create()

	kp1, des1 = sift.detectAndCompute(img1, None)
	kp2, des2 = sift.detectAndCompute(img2, None)

	print(len(kp1),des1.shape)

		# Initiate SIFT detector
	# orb = cv2.ORB_create()

	# # find the keypoints and descriptors with SIFT
	# orb_kp1, orb_des1 = orb.detectAndCompute(img1,None)
	# orb_kp2, orb_des2 = orb.detectAndCompute(img2,None)





	final_1,index1,des11=findmax6(kp1,des1)
	final_2,index2,des22=findmax6(kp2,des2)


	print(len(des22))

	# create BFMatcher object
	bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)

	# des11=np.array([des1[i] for i in index1])
	# des22=np.array([des2[i] for i in index2])

	print(des1.shape)
	print(des2.shape)

	# Match descriptors.
	matches = bf.match(np.array(des11),np.array(des22))
	print(matches)

	# Sort them in the order of their distance.
	matches = sorted(matches, key = lambda x:x.distance)

	# Draw first 10 matches.
	img3 = cv2.drawMatches(img1,final_1,img2,final_2,matches[0:4], None,flags=2)
	# img3 = cv2.drawMatches(img1,final_1,img2,final_2,matches, None,flags=2)




	plt.imshow(img3),plt.show()

def hw2_3_2():
	drawMatch()