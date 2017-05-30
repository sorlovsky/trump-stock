import numpy as np
import matplotlib.pyplot as plt

rand = np.random.rand(10)
ones = np.ones((10,2))
ones[:,1] = ones[:,1] - rand
ones[:,0] = rand

point = np.array([.5,.5])
plt.scatter(ones[:,0], ones[:,1])
plt.scatter(point[0], point[1])
plt.title('KNN To Find Magnitude')
plt.ylabel('Negative Likelihood Estimate')
plt.xlabel('Positive Likelihood Estimate')
plt.show()

# '''
# knn.py
# Simon Orlovsky
# 3/31/17
# '''

# import scipy.spatial
# import numpy as np
# import csv
# import sys
# from collections import Counter
# import matplotlib.pyplot as plt

# data = np.genfromtxt("train_data.txt", dtype=int, delimiter=",")
# labels = np.genfromtxt("train_labels.txt", dtype=int, delimiter=",")

# test_data = np.genfromtxt("test_data.txt", dtype=int, delimiter=",")
# test_labels = np.genfromtxt('test_labels.txt', dtype=int, delimiter=",")

# perm = np.random.permutation(np.shape(data)[0])
# data = data[perm]
# labels = labels[perm]

# def display_image(data):
#     data = np.reshape(data,(-1,28))
#     plt.imshow(data)
#     plt.show()

# def vote(neighbors):
#     counter = Counter(neighbors)
#     return counter.most_common()[0][0]

# def classify(data_point):
#     neighbors = []
#     distances = []
#     for dat in data:
#         if type == "euclidean":
#             distance = scipy.spatial.distance.euclidean(dat, data_point)
#         elif type == "manhattan":
#             distance = scipy.spatial.distance.cityblock(dat, data_point)
#         distances.append(distance)

#     neighbor_indices = np.argsort(distances)[0:k]
#     neighbors = labels[neighbor_indices]
#     return vote(neighbors)
        
# def create_conf_mat(data):
#     confusion_matrix  =  [[0 for i in range(3)] for i in range(3)]
#     for i in range(len(data)):
#         classification = classify(data[i])
#         if test_labels[i] == 1:
#             if classification == 1:
#                 confusion_matrix[0][0] += 1
#             elif classification == 2:
#                 confusion_matrix[0][1] += 1
#             else:
#                 confusion_matrix[0][2] += 1
#         if test_labels[i] == 2:
#             if classification == 2:
#                 confusion_matrix[1][1] += 1
#             elif classification == 1:
#                 confusion_matrix[1][0] += 1
#             else:
#                 confusion_matrix[1][2] += 1
#         if test_labels[i] == 7:
#             if classification == 7:
#                 confusion_matrix[2][2] += 1
#             elif classification == 2:
#                 confusion_matrix[2][1] += 1
#                 display_image(data[i])
#             else:
#                 confusion_matrix[2][0] += 1
#     return np.array(confusion_matrix)

# if len(sys.argv) == 3:
#     k = int(sys.argv[1])
#     type = sys.argv[2]
#     if type != "euclidean" and type != "manhattan":
#         print("USAGE: python3 <distance> <k>")
#     else:
#         print("Finding KNN with k =", k, "and", type, "distance.")
#         confusion_matrix = create_conf_mat(test_data)
#         print(confusion_matrix)
#         print("Percentage: ", (np.trace(confusion_matrix)/len(test_labels)))
# else:
#     print("USAGE: python3 <distance> <k>")
