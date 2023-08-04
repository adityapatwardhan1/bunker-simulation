from voxelize_data import voxelize
import sys
import csv

def output_voxels_to_csv(orig_filename, mu_tot, voxel_size):
    # Write output to voxelized CSV
    filename = orig_filename.replace("_","")
    filename = orig_filename[0:(len(filename)-len("ntHits.csv"))]+"VoxelsResolution"+str(voxel_size)+"mm.csv"
    coordinate_to_median, headers = voxelize(orig_filename, mu_tot, voxel_size)
    with open(filename, "w") as voxelized_csv:
        writer = csv.writer(voxelized_csv)
        for header in headers:
            writer.writerow(header)
        for key in coordinate_to_median.keys():
            row = [0, key[0], key[1], key[2], coordinate_to_median[key]]
            writer.writerow(row)
    print("wrote voxelized data to "+filename)

# Run script
if __name__ == '__main__':
    if len(sys.argv) == 4:
        output_voxels_to_csv(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
    else:
        print("Missing arguments. Terminating program")
