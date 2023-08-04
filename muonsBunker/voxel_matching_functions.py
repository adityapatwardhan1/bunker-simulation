from voxelize_data import voxelize
import sys
import csv
from geant4_pybind import *

# Percent of voxels matching between both the actual and the image out of all voxels in both the actual and image combined
# Only works if there is one cube
def percent_voxels_matching(filename, mu_tot, voxel_size, min_x, max_x, min_y, max_y, min_z, max_z):
    correct_num_voxels = round((max_x - min_x) / voxel_size) * round((max_y - min_y) / voxel_size) * round((max_z - min_z) / voxel_size) # Should it be round or ceil or floor, need voxel side length that is factor of cube side length
    all_voxels_with_object = voxelize(filename, mu_tot, voxel_size)[0]
    print("voxelsize = "+str(voxel_size))
    print(correct_num_voxels)
    counted_voxels_in_bounds = 0
    counted_voxels_outside_bounds = 0
    for key in all_voxels_with_object.keys():
        if min_x-voxel_size//2 <= key[0] <= max_x+voxel_size//2 and min_y-voxel_size//2 <= key[1] <= max_y+voxel_size//2 and min_z-voxel_size//2 <= key[2] <= max_z+voxel_size//2:
            counted_voxels_in_bounds += 1
        else:
            counted_voxels_outside_bounds += 1
    print(counted_voxels_in_bounds)
    print(counted_voxels_outside_bounds)
    # Overlap of correct and simulated set * 2 / union of all voxels correct and incorrect, as %
    # Weird metric but it is necessary to account for externally accidentally counted voxels
    return 100 * (2 * counted_voxels_in_bounds) / (correct_num_voxels + counted_voxels_in_bounds + counted_voxels_outside_bounds)


# Write analysis to CSV
# Only works with one cube
def output_voxel_match_percentages_to_csv(orig_filename, mu_tot, voxel_size, cube_info_filename, add_column_titles):
    rows_to_write = []
    filename = orig_filename.replace("_","")
    filename = filename[0:(len(filename)-len("ntHits.csv"))]+"CubeHitPercentages.csv"
    with open(cube_info_filename, "r") as cube_info:
        reader = csv.reader(cube_info)
        next(reader)
        for row in reader:
            pX = float(row[0])*m
            pY = float(row[1])*m
            pZ = float(row[2])*m
            sL = float(row[3])*m
            single_row_to_write = row.copy()
            single_row_to_write.append(voxel_size) # or whatever
            single_row_to_write.append(percent_voxels_matching(orig_filename, mu_tot, voxel_size, pX-sL,pX+sL,pY-sL,pY+sL,pZ-sL,pZ+sL))
            rows_to_write.append(single_row_to_write)
    with open(filename, "a") as write_percentages:
        writer = csv.writer(write_percentages)
        if add_column_titles:
            writer.writerow(["pX(m)","pY(m)","pZ(m)","sideLengthHalf(m)","mat","voxelSize(mm)","percentDetected"])
        for row in rows_to_write:
            writer.writerow(row)
