import matplotlib.pyplot as plt
import argparse
import pandas as pd

def plot_images(voxel_file):
    """
    Plot 2D and 3D images of scattering points with their scattering angle
    :param voxel_file: Path to the voxels file

    """

    df = pd.read_csv(voxel_file, comment='#', header=None)
    df.columns = ['detectorNo', 'fX', 'fY', 'fZ', 'theta']
    
    # Get x, y, z coordinates and scattering angle
    x_coordinates = df['fX']
    y_coordinates = df['fY']
    z_coordinates = df['fZ']

    theta = df['theta']

    # 2D image
    fig_2d = plt.figure()
    axes_2d = fig_2d.add_subplot()
    scatter_2d = axes_2d.scatter(x_coordinates, y_coordinates, c=theta, marker='s', cmap='viridis')
    fig_2d.colorbar(scatter_2d, ax=axes_2d, label='Theta (angle)')
    axes_2d.set_xlabel('fX')
    axes_2d.set_ylabel('fY')
    axes_2d.set_title('Points of Closest Approach: 2D Projection')

    # 3D image
    fig_3d = plt.figure()
    axes_3d = fig_3d.add_subplot(projection='3d')
    scatter_3d = axes_3d.scatter(x_coordinates, y_coordinates, z_coordinates, c=theta, marker='s', cmap='viridis')
    fig_2d.colorbar(scatter_3d, ax=axes_3d, label='Theta (angle)')
    axes_3d.set_xlabel('fX')
    axes_3d.set_ylabel('fY')
    axes_3d.set_zlabel('fZ')
    axes_3d.set_title('Points of Closest Approach: 3D Coordinates')

    # Show both
    plt.show()


def plot_accuracy(hit_percentages_file):
    df = pd.read_csv(hit_percentages_file)
    
    # Get x, y, z coordinates and scattering angle
    x = df['voxelSize(mm)']
    y = df['percentDetected']
    
    plt.plot(x, y, '-o')
    plt.title('Voxel Overlap Dice-Sorensen Coefficient vs Resolution (mm)')
    plt.xlabel('Voxel Resolution')
    plt.ylabel('Voxel Overlap Dice-Sorensen Coefficient (%)')
    
    plt.show()


def plot_scattering_angles(scattering_angles_file):
    ...


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--voxel_file", help="Path to voxels file")
    parser.add_argument("--hit_percentages_file", help="Path to hit percentages file")
    parser.add_argument("--scattering_angles_file", help="Path to scattering angles file")
    args = parser.parse_args()
    # Plot whatever there is an argument for
    if args.voxel_file:
        try:
            plot_images(args.voxel_file)
        except Exception as e:
            print("An exception occurred when plotting voxels:", e)
    if args.hit_percentages_file:
        try:
            plot_accuracy(args.hit_percentages_file)
        except Exception as e:
            print("An exception occurred when plotting accuracy:", e)
    if args.scattering_angles_file:
        ...
        """
        try:
            plot_scattering_angles(args.scattering_angles_file)
        except Exception as e:
            print("An exception occurred when plotting scattering angles:", e)
        """
