import numpy as np
import os
root = "positionVarianceByLineCount/"
import matplotlib.pyplot as plt
print "==============================================================="

out = open("../variance.dat", "w")
out.write("lines sigma\n")
for file in sorted(os.listdir(root)):
    lines = file.split("lines")[0]
    
    lines = str(int(lines, base=10))
    print lines

    data = open(root + file).readlines()


    data = np.array([map(float, point.split("]")[0].split("[")[1].split(", ")) for point in data])
    data = data[2:]
    average = np.sum(data, 0) / data.shape[0]

    error = data - average
    rms = np.sqrt(np.sum(error * error) / error.shape[0])
    print "rms:", rms
    plt.scatter(error.transpose()[0], error.transpose()[2])
    plt.show()
    plt.plot(error)
    plt.show()
    out.write(str(lines) + " " + str(rms)+ "\n")
    print np.cov(data.transpose())

out.close()
    
