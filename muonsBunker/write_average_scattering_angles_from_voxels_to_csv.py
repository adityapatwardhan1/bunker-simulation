from voxelize_data import get_avg_scattering_angle_among_voxels
import sys
import csv
# Arguments: filename, number of muons used, cube side length (120 is good since it's highly divisible)
if __name__ == '__main__':
    if len(sys.argv) == 4: # Specified voxel size
        filename = sys.argv[1].replace("_","")
        cube_side_length = sys.argv[3]
        filename = sys.argv[1][0:(len(filename)-len("ntHits.csv"))]+"AverageScatteringAnglesCubeSideLength"+cube_side_length+"mm.csv"
        with open(filename, "w") as avg_voxel_angles_csv:
            writer = csv.writer(avg_voxel_angles_csv)
            writer.writerow(["Voxel Side Length (mm)", "Avg Scattering Angle (Degrees)"])
            for i in range(1,int(cube_side_length)):
                if int(sys.argv[3]) % i == 0:
                    writer.writerow([i, get_avg_scattering_angle_among_voxels(sys.argv[1], int(sys.argv[2]), i)])
        print("wrote output to "+filename)
    else:
        print("Missing arguments. Terminating program")
