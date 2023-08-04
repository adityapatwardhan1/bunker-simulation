from voxelize_data import percent_voxels_matching
import csv
import sys
from geant4_pybind import *
"""
Arguments: filename, total muons used
Only works when there is one cube defined in cubeInfo.txt, this is for testing the geometry for the study.
Writes percent detected for factors of the side length of the cube (mm) to ensure the formula is correct.
"""
if __name__ == '__main__':
    if len(sys.argv) > 2:
        raw_data_filename = sys.argv[1]
        out_filename = raw_data_filename.replace("_","")
        out_filename = out_filename[0:(len(out_filename)-len("ntHits.csv"))]+"CubeHitPercentages.csv"
        rows_to_write = []
        cube_info_filename = "cubeInfo.txt"
        mu_tot = int(sys.argv[2])
            
        with open(cube_info_filename, "r") as cube_info:
            reader = csv.reader(cube_info)
            next(reader)
            for row in reader:
                pX = float(row[0])*m
                pY = float(row[1])*m
                pZ = float(row[2])*m
                sL = float(row[3])*m
                for voxel_size in range(1, int(2*sL)+1):
                    single_row_to_write = row.copy()
                    if 2*sL % voxel_size == 0:
                        single_row_to_write.append(voxel_size)
                        single_row_to_write.append(percent_voxels_matching(raw_data_filename, mu_tot, voxel_size, pX-sL,pX+sL,pY-sL,pY+sL,pZ-sL,pZ+sL))
                        rows_to_write.append(single_row_to_write)
        
        with open(out_filename, "w") as output:
            writer = csv.writer(output)
            writer.writerow(["pX(m)","pY(m)","pZ(m)","sideLengthHalf(m)","mat","voxelSize(mm)","percentDetected"])
            for row in rows_to_write:
                writer.writerow(row)
        print("wrote output to "+out_filename)
        
    else:
        print("Missing arguments. Terminating program")
