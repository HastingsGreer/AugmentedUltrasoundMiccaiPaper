import numpy as np
import os
root = "std_dev_x_lines/"
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
print( "===============================================================")

out = open("../variance.dat", "w")
out.write("lines sigma\n")
for file in sorted(os.listdir(root)):

    lines = file.split("lines")[0]
    
    lines = str(int(lines, base=10))
    print( lines)

    rinput = open("rinputlines" + lines, "w")
    


    data = open(root + file).readlines()


    data = np.array([list(map(float, point.split("]")[0].split("[")[1].split(", "))) for point in data])
    data = data[2:]
    
    rinput.write("x, y, z\n")

    
    average = np.sum(data, 0) / data.shape[0]

    error = data - average
    rms = np.sqrt(np.sum(error * error) / error.shape[0])
    for point in error:
       rinput.write(", ".join(map(str, point)) + "\n")
    
    rinput.close()
    print( "rms:", rms)
    #plt.scatter(error.transpose()[0], error.transpose()[2])
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.scatter(error[:, 0], error[:,1], error[:,2])

    ax.set_xlim([-.3, .3])
    ax.set_ylim([-.3, .3])
    ax.set_zlim([-.3, .3])

    ax.set_xlabel("x (cm)") 
    ax.set_ylabel("y (cm)") 
    ax.set_zlabel("z (cm)") 
    
    plt.show()


    #plt.plot(error)
    #plt.show()
    out.write(str(lines) + " " + str(rms)+ "\n")
    print( np.cov(data.transpose()))

out.close()

#Maeliss
# out = open("std_dev.dat", "w")
# out.write("lines sigma\n")
# for file in sorted(os.listdir(root)):
    
    # lines = file.split("lines")[0]
    # lines = str(int(lines, base=10))
    # print lines

    # data = open(root + file).readlines()
    # data = np.array([map(float, point.split()) for point in data])
    
    # mean = np.mean(data, 0)
    # print mean
    
    # std_dev = np.std(data,0)
    # print "std dev = ",std_dev

    # out.write(str(lines) + " lines :    mean = " + str(mean) + " std_dev = " + str(std_dev) + "\n")
    
# out.close()
