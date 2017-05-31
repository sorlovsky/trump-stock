
import numpy as np
import matplotlib.pyplot as plt
import pylab
import sys
import math


def euclidean(test_image,train_data,train_labels,k):

	cal_dis = list()
	for y in range(0, np.shape(train_data)[0]):
		cal_dis.append(math.sqrt(np.sum(np.subtract(test_image,train_data[y])**2)))

	voters = np.argsort(cal_dis,axis=-1,kind="mergesort",order=None)
	votes = list()

	for i in range(0,k):
		votes.append(train_labels[voters[i]])

	#handle ties please
	counts = np.bincount(votes)
	pred_label = np.argmax(counts)
	return np.argmax(counts)

def manhattan(test_image,train_data,train_labels,k):

	cal_dis = list()
	for y in range(0, np.shape(train_data)[0]):
		cal_dis.append(np.sum(np.absolute(np.subtract(test_image,train_data[y]))))

	voters = np.argsort(cal_dis,axis=-1,kind="mergesort",order=None)
	votes = list()

	for i in range(0,k):
		votes.append(train_labels[voters[i]])

	#handle ties please
	counts = np.bincount(votes)
	pred_label = np.argmax(counts)
	return np.argmax(counts)

def create_conf_matrix(actual, predicted, labels):

	cm = np.zeros((len(labels), len(labels)))
	for a, p in zip(actual, predicted):
		if a==1:
			a=0
		if a==2:
			a=1
		if a==7:
			a=2

		if p==1:
			p=0
		if p==2:
			p=1
		if p==7:
			p=2
		cm[a][p] += 1
	return cm

def print_cm(cm, labels, hide_zeroes=False, hide_diagonal=False, hide_threshold=None):
    """pretty print for confusion matrixes"""
    columnwidth = max([len(x) for x in labels]+[5]) # 5 is value length
    empty_cell = " " * columnwidth
    # Print header
    print "    " + empty_cell,
    for label in labels:
        print "%{0}s".format(columnwidth) % label,
    print
    # Print rows
    for i, label1 in enumerate(labels):
        print "    %{0}s".format(columnwidth) % label1,
        for j in range(len(labels)):
            cell = "%{0}.1f".format(columnwidth) % cm[i, j]
            if hide_zeroes:
                cell = cell if float(cm[i, j]) != 0 else empty_cell
            if hide_diagonal:
                cell = cell if i != j else empty_cell
            if hide_threshold:
                cell = cell if cm[i, j] > hide_threshold else empty_cell
            print cell,
        print

def display_image(actual, predicted, test_data):
	#Displays a list of 784 gray-scale values as an image

	cr_count = 5
	incr_count = 5

	cr = np.where(actual == predicted)
	cr = np.random.choice(cr[0],5)
	incr = np.where(actual != predicted)
	incr = np.random.choice(incr[0],5)


	to_draw_cr = test_data[cr]
	to_draw_incr = test_data[incr]

	for x in to_draw_cr:
		data = np.array(x)
		data = np.reshape(data,(-1,28))
		plt.imshow(data)
		plt.show()

	for y in to_draw_incr:
		data = np.array(y)
		data = np.reshape(data,(-1,28))
		plt.imshow(data)
		plt.show()

def main():
    train_data = np.loadtxt("train_data.txt",dtype=int,delimiter=",")
    train_labels = np.loadtxt("train_labels.txt",dtype=int,delimiter="\n")

    test_data = np.loadtxt("test_data.txt",dtype=int,delimiter=",")
    test_labels = np.loadtxt("test_labels.txt",dtype=int,delimiter="\n")

    if len(sys.argv) < 3:
    	print("Not enough args")
    	exit()
    else:

		k = int(sys.argv[1])
		mode = sys.argv[2]

		if mode == "euclidean":
			print "k : ",k
			print "Distance : ",mode

			pred_labels = list()

			for x in range (0, np.shape(test_data)[0]):
				pred_labels.append(euclidean(test_data[x],train_data,train_labels,k))

			C = create_conf_matrix(test_labels, pred_labels,("1","2","7"))
			accuracy = (test_labels == pred_labels).sum() / float(len(test_labels))

			print "Confusion Matrix:"
			print_cm(C,("1","2","7"))
			print "Accuracy:" , accuracy
			display_image(test_labels, pred_labels, test_data)

		else:
			print "k : ",k
			print "Distance : ",mode

			pred_labels = list()
			for x in range (0, np.shape(test_data)[0]):
				pred_labels.append(manhattan(test_data[x],train_data,train_labels,k))

			C = create_conf_matrix(test_labels, pred_labels,("1","2","7"))
			accuracy = (test_labels == pred_labels).sum() / float(len(test_labels))

			print "Confusion Matrix:"
			print_cm(C,("1","2","7"))
			print "Accuracy:" , accuracy
			display_image(test_labels, pred_labels, test_data)




if __name__ == '__main__':
    main()
