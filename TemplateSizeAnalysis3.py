
import numpy as np
import glob
import matplotlib.pyplot as plt


class unit:

    # Reads CSV into a 2D array, and separates the coordinates into those for the right and left corners
    # self.right_coords
    # self.left_coords
    def __init__(self, filename):
        data = np.genfromtxt(filename, dtype=float, delimiter=",")
        self.right_coords = data[::2]
        self.left_coords = data[1::2]
    

class corner_data:

    # Create dictionaries for each corner
    # self.A
    # self.B
    # self.C
    # self.D
    def __init__(self, expected_values_file):
        self.A, self.B, self.C, self.D = {}, {}, {}, {}
        self.A_time, self.B_time, self.C_time, self.D_time = {}, {}, {}, {}
        self.expected = np.genfromtxt(expected_values_file, dtype=float, delimiter=",")

    # Adds data to the dictionaries, based on the given unit
    # Parameters: data (unit containing data), template_name (dimentions of the template in px),
    #           template_type (top or bottom)
    def add_data(self, data: unit, data_time: unit, template_name, template_type):
        if template_type == "top":
            self.C[template_name] = data.right_coords
            self.D[template_name] = data.left_coords
        else:
            self.B[template_name] = data.right_coords
            self.A[template_name] = data.left_coords
        if template_type == "top":
            self.C_time[template_name] = data_time.right_coords
            self.D_time[template_name] = data_time.left_coords
        else:
            self.B_time[template_name] = data_time.right_coords
            self.A_time[template_name] = data_time.left_coords


    # Parameters: all_data (the data), dimension (size varies in width or length?),
    #            coordinate (std or x or y coordinate?)
    def scatter_std_vs_size(self, dimension, coordinate, mark):
        x = []
        y_A, y_B, y_C, y_D = [], [], [], []
        for key in self.A:
            if dimension == "Length":
                x.append(int(key.split("x")[1]))
            else:
                x.append(int(key.split("x")[0]))
            if coordinate == "x":
                y_A.append(np.std(self.A[key][:, 0]) * 1000)
                y_B.append(np.std(self.B[key][:, 0]) * 1000)
                y_C.append(np.std(self.C[key][:, 0]) * 1000)
                y_D.append(np.std(self.D[key][:, 0]) * 1000)
            else:
                y_A.append(np.std(self.A[key][:, 1]) * 1000)
                y_B.append(np.std(self.B[key][:, 1]) * 1000)
                y_C.append(np.std(self.C[key][:, 1]) * 1000)
                y_D.append(np.std(self.D[key][:, 1]) * 1000)
        A = plt.scatter(x, y_A)
        B = plt.scatter(x, y_B)
        C = plt.scatter(x, y_C)
        D = plt.scatter(x, y_D)
        plt.title("StDev in " + coordinate + " over Template " + dimension + " (Mark " + mark + ")")
        plt.xlabel(dimension + " of Template (px)")
        plt.ylabel("Standard Deviation in " + coordinate + " (um)")
        plt.legend((A, B, C, D), ("Corner A", "Corner B", "Corner C", "Corner D"))
        #plt.axvline(x = 35)
        #plt.axvline(x = 110)
        #plt.ylim(0,1)
        plt.show()


    # Parameters: all_data (the data), dimension (size varies in width or length?),
    #            coordinate (std or x or y coordinate?)
    def scatter_mean_vs_size(self, dimension, coordinate, mark):
        x = []
        y_A, y_B, y_C, y_D = [], [], [], []
        for key in self.A:
            if dimension == "Length":
                x.append(int(key.split("x")[1]))
            else:
                x.append(int(key.split("x")[0]))
            if coordinate == "x":
                y_A.append(np.mean(self.A[key][:, 0]) * 1000)
                y_B.append(np.mean(self.B[key][:, 0]) * 1000)
                y_C.append(np.mean(self.C[key][:, 0]) * 1000)
                y_D.append(np.mean(self.D[key][:, 0]) * 1000)
            else:
                y_A.append(np.mean(self.A[key][:, 1]) * 1000)
                y_B.append(np.mean(self.B[key][:, 1]) * 1000)
                y_C.append(np.mean(self.C[key][:, 1]) * 1000)
                y_D.append(np.mean(self.D[key][:, 1]) * 1000)
        A = plt.scatter(x, y_A)
        B = plt.scatter(x, y_B)
        C = plt.scatter(x, y_C)
        D = plt.scatter(x, y_D)
        plt.title("Mean in " + coordinate + " over Template " + dimension + " (Mark " + mark + ")")
        plt.xlabel(dimension + " of Template (px)")
        plt.ylabel("Mean in " + coordinate + " (um)")
        plt.legend((A, B, C, D), ("Corner A", "Corner B", "Corner C", "Corner D"))
        #plt.axvline(x = 35)
        #plt.axvline(x = 110)
        plt.show()


    def scatter_time_vs_size(self, dimension, mark):
        x = []
        y_A, y_B, y_C, y_D = [], [], [], []
        if dimension == "Length":
            for key in self.A:
                x.append(int(key.split("x")[1]))
        else:
            for key in self.A:
                x.append(int(key.split("x")[0]))
        for key in all_data.A_time:
            y_A.append(np.mean(self.A_time[key]))
            y_B.append(np.mean(self.B_time[key]))
            y_C.append(np.mean(self.C_time[key]))
            y_D.append(np.mean(self.D_time[key]))
        A = plt.scatter(x, y_A)
        B = plt.scatter(x, y_B)
        C = plt.scatter(x, y_C)
        D = plt.scatter(x, y_D)
        plt.title("Time over Template " + dimension + " (Mark " + mark + ")")
        plt.xlabel(dimension + " of Template (px)")
        plt.ylabel("Time (ms)")
        plt.legend((A, B, C, D), ("Corner A", "Corner B", "Corner C", "Corner D"), fontsize=8)
        plt.ylim(0,100)
        plt.axvline(x = 26)
        plt.axvline(x = 34)
        plt.show()


    def scatter_efficiency_vs_size(self, dimension, mark):
        x = []
        y_A, y_B, y_C, y_D = [], [], [], []
        count_A, count_B, count_C, count_D = 0, 0, 0, 0
        if dimension == "Length":
            for key in self.A:
                x.append(int(key.split("x")[1]))
        else:
            for key in self.A:
                x.append(int(key.split("x")[0]))
        time_cut = 57.0 #cut-off for how long it took to pattern match
        position_cut = .002  #cut-off for how far the pattern match is from expected
        for key in self.A: #iterate over the tempalates
            for i in range(len(self.A[key])): #iterate over the data points
                if abs(self.A[key][i, 0] - self.expected[0,0]) < position_cut and abs(self.A[key][i, 1] - self.expected[0,1]) < position_cut and self.A_time[key][i] < time_cut:
                    count_A += 1
                if abs(self.B[key][i, 0] - self.expected[1,0]) < position_cut and abs(self.B[key][i, 1] - self.expected[1,1]) < position_cut and self.B_time[key][i] < time_cut:
                    count_B += 1
                if abs(self.C[key][i, 0] - self.expected[2,0]) < position_cut and abs(self.C[key][i, 1] - self.expected[2,1]) < position_cut and self.C_time[key][i] < time_cut:
                    count_C += 1
                if abs(self.D[key][i, 0] - self.expected[3,0]) < position_cut and abs(self.D[key][i, 1] - self.expected[3,1]) < position_cut and self.D_time[key][i] < time_cut:
                    count_D += 1
            y_A.append(count_A/len(self.A[key]))
            y_B.append(count_B/len(self.B[key]))
            y_C.append(count_C/len(self.C[key]))
            y_D.append(count_D/len(self.D[key]))
            count_A, count_B, count_C, count_D = 0, 0, 0, 0
        A = plt.scatter(x, y_A)
        B = plt.scatter(x, y_B)
        C = plt.scatter(x, y_C)
        D = plt.scatter(x, y_D)
        plt.title("Efficiency over Template " + dimension + " (Mark " + mark + ")")
        plt.xlabel(dimension + " of the Template (px)")
        plt.ylabel("Efficiency")
        plt.legend((A, B, C, D), ("Corner A", "Corner B", "Corner C", "Corner D"))
        #plt.ylim(.8,1.1)
        plt.axvline(x = 24)
        plt.axvline(x = 40)
        plt.show()


###~~~MAIN~~~###
all_data = corner_data("E_expected_6-24.csv")

# This part stores all the data for the top
top_files = glob.glob("./Data V3/6-24/E_top_positions*/*Pattern*.csv")
top_time_files = glob.glob("./Data V3/6-24/E_top_positions*/*Timing*.csv")
for file, time_file in zip(top_files, top_time_files):
    filename = file.split("-")[-1][:-4]
    all_data.add_data(unit(file), unit(time_file), filename, "top")

# This part stores all the data for the bottom
bottom_files = glob.glob("./Data V3/6-24/E_bottom_positions*/*Pattern*.csv")
bottom_time_files = glob.glob("./Data V3/6-24/E_bottom_positions*/*Timing*.csv")
for file, time_file in zip(bottom_files, bottom_time_files):
    filename = file.split("-")[-1][:-4]
    all_data.add_data(unit(file), unit(time_file), filename, "bottom")

# This part calls the functions to graph the data
mark = "E"
all_data.scatter_std_vs_size("Length", "x", mark)
all_data.scatter_std_vs_size("Length", "y", mark)
all_data.scatter_mean_vs_size("Length", "x", mark)
all_data.scatter_mean_vs_size("Length", "y", mark)
all_data.scatter_time_vs_size("Length", mark)
all_data.scatter_efficiency_vs_size("Length", mark)
