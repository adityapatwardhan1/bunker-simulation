import csv
import sys
import math
import configparser
from geant4_pybind import *

def voxelize(filename, mu_tot, voxel_size=10):
    coordinate_to_info_needed_for_median = dict()
    headers = []
    # Read file
    with open(filename, "r") as non_voxelized_csv:
        reader = csv.reader(non_voxelized_csv)
        for row in reader:
            # Get info needed for theta average
            if len(row) > 1:
                x = float(row[1])
                y = float(row[2])
                z = float(row[3])
                theta = float(row[4])
                
                voxel_coordinate = convert_to_voxel_coordinate((x, y, z), voxel_size)
                if not voxel_coordinate in coordinate_to_info_needed_for_median.keys():
                    coordinate_to_info_needed_for_median[voxel_coordinate] = [theta]
                else:
                    coordinate_to_info_needed_for_median[voxel_coordinate].append(theta)
            else:
                headers.append(row)
    # Calculate average
    coordinate_to_median = dict()
    min_hits_per_voxel = mu_tot * 0.00006 * (voxel_size / 25) ** 3 # Filter function to eliminate outliers
    
    for key in coordinate_to_info_needed_for_median:
        if len(coordinate_to_info_needed_for_median[key]) >= min_hits_per_voxel: # Ensure it's not an outlier
            coordinate_to_info_needed_for_median[key].sort()
            coordinate_to_median[key] = median(coordinate_to_info_needed_for_median[key])

    return coordinate_to_median, headers


def get_avg_scattering_angle_among_voxels(orig_filename, mu_tot, voxel_size):
    all_voxels = voxelize(orig_filename, mu_tot, voxel_size)[0]
    if len(all_voxels) == 0:
        return -1
    avg = sum(all_voxels[key] for key in all_voxels)/len(all_voxels)
    return avg


def convert_to_voxel_coordinate(coordinate, voxel_size):
    return (coordinate[0]//voxel_size*voxel_size + voxel_size//2, coordinate[1]//voxel_size*voxel_size + voxel_size//2, coordinate[2]//voxel_size*voxel_size + voxel_size//2)


def median(sorted_list):
    if len(sorted_list) == 0:
        return 0
    if len(sorted_list) % 2 == 1:
        return sorted_list[len(sorted_list)//2]
    return 0.5*(sorted_list[len(sorted_list)//2] + sorted_list[len(sorted_list)//2 - 1])    

# Percent of voxels matching between both the actual and the image out of all voxels in both the actual and image combined
# Only works if there is one cube
def percent_voxels_matching(filename, mu_tot, voxel_size, min_x, max_x, min_y, max_y, min_z, max_z):
    correct_num_voxels = round((max_x - min_x) / voxel_size) * round((max_y - min_y) / voxel_size) * round((max_z - min_z) / voxel_size) # Should it be round or ceil or floor, need voxel side length that is factor of cube side length
    all_voxels_with_object = voxelize(filename, mu_tot, voxel_size)[0]
    counted_voxels_in_bounds = 0
    counted_voxels_outside_bounds = 0
    for key in all_voxels_with_object.keys():
        if min_x-voxel_size//2 <= key[0] <= max_x+voxel_size//2 and min_y-voxel_size//2 <= key[1] <= max_y+voxel_size//2 and min_z-voxel_size//2 <= key[2] <= max_z+voxel_size//2:
            counted_voxels_in_bounds += 1
        else:
            counted_voxels_outside_bounds += 1
    # Overlap of correct and simulated set * 2 / union of all voxels correct and incorrect, as %
    # Weird metric but it is necessary to account for externally accidentally counted voxels
    return 100 * (2 * counted_voxels_in_bounds) / (correct_num_voxels + counted_voxels_in_bounds + counted_voxels_outside_bounds)       
