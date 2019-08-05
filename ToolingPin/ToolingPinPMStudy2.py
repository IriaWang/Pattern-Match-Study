# This program reads several files, the positions and timings of the top and bottom corners for different templates.
# It analyzes the data by making several graphs (template length or width vs standard deviation, mean, time, efficiency).

import numpy as np
import glob
import matplotlib.pyplot as plt

# A "unit" is a bridge between the formatting of top/bottom files and the dictionaries wanted for each corner


class unit:

    # Reads CSV into a 2D array, and separates the coordinates into arrays for the right and left corners
    # self.right_coords
    # self.left_coords
    def __init__(self, filename):
        data = np.genfromtxt(filename, dtype=float, delimiter=",")
        self.raw_data = [data[::5], data[1::5], data[2::5], data[3::5], data[4::5]]

# This class holds all the data given in the files using dictionaries


class corner_data:

    # Create dictionaries for each corner (position and time), and the expected positions
    # self.A, self.B, self.C, self.D
    # self.A_time, self.B_time, self.C_time, self.D_time
    # self.expected
    # Parameters: expected_values_file (file containing expected positions for each corner)
    def __init__(self, R_expected_values_file, L_expected_values_file):
        self.right = [{}, {}, {}, {}, {}]
        self.right_time = [{}, {}, {}, {}, {}]
        self.left = [{}, {}, {}, {}, {}]
        self.left_time = [{}, {}, {}, {}, {}]
        self.right_expected = np.genfromtxt(R_expected_values_file, dtype=float, delimiter=",")
        self.left_expected = np.genfromtxt(L_expected_values_file, dtype=float, delimiter=",")


    # Adds data to the dictionaries, based on the given unit
    # Parameters: data (unit containing position data), data_time (unit containing time data), template_name
    #           (dimentions of the template in px), template_type (top or bottom)
    def add_data(self, data: unit, data_time: unit, template_name, right_left):
        if right_left == "right":
            for i in range(len(self.right)):
                self.right[i][template_name] = data.raw_data[i]
                self.right_time[i][template_name] = data_time.raw_data[i]
        else:
            for i in range(len(self.left)):
                self.left[i][template_name] = data.raw_data[i]
                self.left_time[i][template_name] = data_time.raw_data[i]

    # Graph standard deviation over length or width
    # Parameters: dimension (length or width), coordinate (standard deviation in x or y), mark (Fiducial mark)
    def scatter_std_vs_size(self, dimension, coordinate):
        x = []
        y_right, y_left = [[],[],[],[],[]], [[],[],[],[],[]]
        
        for key in self.right[0]:
            if dimension == "Length":
                x.append(int(key.split("x")[1]))
            else:
                x.append(int(key.split("x")[0]))
                
        if coordinate == "x":
            for i in range(len(self.right)):
                for key in self.right[i]:
                    y_right[i].append(np.std(self.right[i][key][:,0]) * 1000)
                    y_left[i].append(np.std(self.left[i][key][:,0]) * 1000)
        else:
            for i in range(len(self.right)):
                for key in self.right[i]:
                    y_right[i].append(np.std(self.right[i][key][:,1]) * 1000)
                    y_left[i].append(np.std(self.left[i][key][:,1]) * 1000)
                    
        R0 = plt.scatter(x, y_right[0])
        L0 = plt.scatter(x, y_left[0])
        R1 = plt.scatter(x, y_right[1])
        L1 = plt.scatter(x, y_left[1])
        R2 = plt.scatter(x, y_right[2])
        L2 = plt.scatter(x, y_left[2])
        R3 = plt.scatter(x, y_right[3])
        L3 = plt.scatter(x, y_left[3])
        R4 = plt.scatter(x, y_right[4])
        L4 = plt.scatter(x, y_left[4])
        plt.title("StDev in " + coordinate + " over Template " +
                  dimension)
        plt.xlabel(dimension + " of Template (px)")
        plt.ylabel("Standard Deviation in " + coordinate + " (um)")
        plt.legend((R0, R1, R2, R3, R4, L0, L1, L2, L3, L4), ("R0", "R1", "R2", "R3", "R4", "L0", "L1", "L2", "L3", "L4"))
        #plt.axvline(x = 35)
        #plt.axvline(x = 110)
        
        plt.ylim(0,5)
        plt.show()

    # Graph mean over length or width
    # Parameters: dimension (size varies in width or length?), coordinate (std or x or y coordinate?), mark (Fiducial Mark)
    def scatter_mean_vs_size(self, dimension, coordinate):
        x = []
        y_right, y_left = [[],[],[],[],[]], [[],[],[],[],[]]
        
        for key in self.right[0]:
            if dimension == "Length":
                x.append(int(key.split("x")[1]))
            else:
                x.append(int(key.split("x")[0]))
                
        if coordinate == "x":
            for i in range(len(self.right)):
                for key in self.right[i]:
                    y_right[i].append(np.mean(self.right[i][key][:,0]) * 1000)
                    y_left[i].append(np.mean(self.left[i][key][:,0]) * 1000)
        else:
            for i in range(len(self.right)):
                for key in self.right[i]:
                    y_right[i].append(np.mean(self.right[i][key][:,1]) * 1000)
                    y_left[i].append(np.mean(self.left[i][key][:,1]) * 1000)
                    
        R0 = plt.scatter(x, y_right[0])
        L0 = plt.scatter(x, y_left[0])
        R1 = plt.scatter(x, y_right[1])
        L1 = plt.scatter(x, y_left[1])
        R2 = plt.scatter(x, y_right[2])
        L2 = plt.scatter(x, y_left[2])
        R3 = plt.scatter(x, y_right[3])
        L3 = plt.scatter(x, y_left[3])
        R4 = plt.scatter(x, y_right[4])
        L4 = plt.scatter(x, y_left[4])
        plt.title("Mean in " + coordinate + " over Template " +
                  dimension)
        plt.xlabel(dimension + " of Template (px)")
        plt.ylabel("Mean in " + coordinate + " (um)")
        plt.legend((R0, R1, R2, R3, R4, L0, L1, L2, L3, L4), ("R0", "R1", "R2", "R3", "R4", "L0", "L1", "L2", "L3", "L4"))
        #plt.axvline(x = 35)
        #plt.axvline(x = 110)
        #plt.ylim(-49250,-48500)
        plt.show()

    # Graph time over length or width
    # Parameters: dimension (length or width), mark (Fiducial Mark)
    def scatter_time_vs_size(self, dimension):
        x = []
        y_right, y_left = [[],[],[],[],[]], [[],[],[],[],[]]
        
        for key in self.right[0]:
            if dimension == "Length":
                x.append(int(key.split("x")[1]))
            else:
                x.append(int(key.split("x")[0]))
                

        for i in range(len(self.right)):
            for key in self.right[i]:
                y_right[i].append(np.mean(self.right_time[i][key]))
                #print(self.right_time[i][key])
                y_left[i].append(np.mean(self.left_time[i][key]))
                    
        R0 = plt.scatter(x, y_right[0])
        L0 = plt.scatter(x, y_left[0])
        R1 = plt.scatter(x, y_right[1])
        L1 = plt.scatter(x, y_left[1])
        R2 = plt.scatter(x, y_right[2])
        L2 = plt.scatter(x, y_left[2])
        R3 = plt.scatter(x, y_right[3])
        L3 = plt.scatter(x, y_left[3])
        R4 = plt.scatter(x, y_right[4])
        L4 = plt.scatter(x, y_left[4])
        plt.title("Time over Template " + dimension)
        plt.xlabel(dimension + " of Template (px)")
        plt.ylabel("Time (ms)")
        plt.legend((R0, R1, R2, R3, R4, L0, L1, L2, L3, L4), ("R0", "R1", "R2", "R3", "R4", "L0", "L1", "L2", "L3", "L4"))
        #plt.ylim(0, 100)
        #plt.axvline(x=26)
        #plt.axvline(x=1336)
        plt.show()

    # Graph efficiency (defined as the fraction of data points that are close to the
    #           expected position and are under a certain time) over length or width
    # Parameters: dimension (length or width), mark (Fiducial Mark)
    def scatter_efficiency_vs_size(self, dimension):
        x = []
        y_right, y_left = [[],[],[],[],[]], [[],[],[],[],[]]
        count_R = 0
        count_L = 0
        
        for key in self.left[0]:
            if dimension == "Length":
                x.append(int(key.split("x")[1]))
            else:
                x.append(int(key.split("x")[0]))
                
        time_cut = 700000000  # cut-off for how long it took to pattern match
        # cut-off for how far the pattern match is from expected (mm)
        position_cut = .05
        for j in range(len(self.left)):
            for key in self.left[j]:  # iterate over the tempalates
                for i in range(len(self.left[j][key])):  # iterate over the data points
                    if abs(self.right[j][key][i, 0] - self.right_expected[j, 0]) < position_cut and abs(self.right[j][key][i, 1] - self.right_expected[j, 1]) < position_cut and self.right_time[j][key][i] < time_cut:
                        count_R += 1
                    if abs(self.left[j][key][i, 0] - self.left_expected[j, 0]) < position_cut and abs(self.left[j][key][i, 1] - self.left_expected[j, 1]) < position_cut and self.left_time[j][key][i] < time_cut:
                        count_L += 1
                y_right[j].append(count_R/len(self.right[j][key]))
                y_left[j].append(count_L/len(self.left[j][key]))
                count_R, count_L = 0, 0
        
        R0 = plt.scatter(x, y_right[0])
        L0 = plt.scatter(x, y_left[0])
        R1 = plt.scatter(x, y_right[1])
        L1 = plt.scatter(x, y_left[1])
        R2 = plt.scatter(x, y_right[2])
        L2 = plt.scatter(x, y_left[2])
        R3 = plt.scatter(x, y_right[3])
        L3 = plt.scatter(x, y_left[3])
        R4 = plt.scatter(x, y_right[4])
        L4 = plt.scatter(x, y_left[4])
        plt.title("Efficiency over Template " +
                  dimension)
        plt.xlabel(dimension + " of the Template (px)")
        plt.ylabel("Efficiency")
        plt.legend((R0, R1, R2, R3, R4, L0, L1, L2, L3, L4), ("R0", "R1", "R2", "R3", "R4", "L0", "L1", "L2", "L3", "L4"))
        # plt.ylim(.8,1.1)
        #plt.axvline(x=24)
        #plt.axvline(x=40)
        plt.show()


###~~~MAIN~~~###
# To the user: this is the input, fill these out before running
R_expected_positions = "right_expected.csv"
L_expected_positions = "left_expected.csv"
right_positions = "./Data2/WithPaper-Right-Width/*Pattern*.csv"
right_times = "./Data2/WithPaper-Right-Width/*Timing*.csv"
left_positions = "./Data2/WithPaper-Left-Width/*Pattern*.csv"
left_times = "./Data2/WithPaper-Left-Width/*Timing*.csv"
length_or_width = "Width"

all_data = corner_data(R_expected_positions, L_expected_positions)

# This part stores all the data for the top
#add_data(self, right_data, left_data, right_time, left_time, template_name):
right_files = glob.glob(right_positions)
right_time_files = glob.glob(right_times)
for right_file, time_file in zip(right_files, right_time_files):
    filename = right_file.split("-")[-1][:-4]
    right_file_unit = unit(right_file)
    time_file_unit = unit(time_file)
    all_data.add_data(right_file_unit, time_file_unit, filename, "right")

# This part stores all the data for the bottom
left_files = glob.glob(left_positions)
left_time_files = glob.glob(left_times)
for left_file, time_file in zip(left_files, left_time_files):
    filename = left_file.split("-")[-1][:-4]
    left_file_unit = unit(left_file)
    time_file_unit = unit(time_file)
    all_data.add_data(left_file_unit, time_file_unit, filename, "left")


# This part calls the functions to graph the data
all_data.scatter_std_vs_size(length_or_width, "x")
all_data.scatter_std_vs_size(length_or_width, "y")
all_data.scatter_mean_vs_size(length_or_width, "x")
all_data.scatter_mean_vs_size(length_or_width, "y")
all_data.scatter_time_vs_size(length_or_width)
all_data.scatter_efficiency_vs_size(length_or_width)