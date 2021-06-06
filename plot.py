from mpl_toolkits.mplot3d import Axes3D
from matplotlib.lines import Line2D
from stl import mesh as meshes
from mpl_toolkits import mplot3d
from matplotlib import pyplot as plt
import pymesh as msh
import trimesh as tm
import numpy as np

print('Welcome to the assignment solution by Bushra Naqvi. Please keep on closing the windows opening while the code runs to proceed further.')

mesh = tm.load('./assignment.stl')


def slicer(height, origin=[-999, -999, -999], normal=[0, 1, 0], mode='any'):

    if(mode == 'base'):
        normalx = normal
        originx = [0, height, 0]

    else:
        normalx = [- normal[0], - normal[1], - normal[2]]
        originx = origin + np.multiply(normalx, height)

    slice = mesh.section(plane_origin=originx,
                         plane_normal=normalx)

    slice_2D, slice_3D = slice.to_planar()

    fig, ax = plt.subplots()

    custom_lines = [Line2D([0], [0], color='black', lw=2),
                    Line2D([0], [0], color='green', lw=2)]

    ax.legend(custom_lines, ['Outer Loops', 'Inner Loops'])

    strin = ''

    if(origin[1] == height):
        strin = 'height'
    else:
        strin = 'distance from selected base'

    plt.title('At ' + strin + ' - ' + str(height) + " mm")

    slice_2D.show()


def assignment1():
    print('Running Assignment Code for Part 1')
    print('Please enter the height of figure in mm (enter 50 for the figure given in assignment)')
    height = int(input())

    print('Running for heights 10, 30 and 50 mm as given in the question')

    slicer(10, mode='base')
    slicer(30, mode='base')
    slicer(50, mode='base')


def assignment2():
    print('Running Assignment Code for Part 2')
    print('Please enter the height of figure in mm (enter 50 for the figure given in assignment)')
    height = int(input())
    print('Please enter the step height in mm')
    step = int(input())

    for i in range(0, height, step):
        slicer(i, mode='base')


def assignment3():
    print('Running Assignment Code for Part 3')

    fig = plt.figure()
    ax = Axes3D(fig)

    m = []

    for i in range(0, len(mesh.facets)):

        if(mesh.facets_area[i] > 50):
            m.append(mesh.facets_origin[i])

    for i in range(len(m)):  # plot each point + it's index as text above
        ax.scatter(m[i][0], m[i][1], m[i][2], color='b', zorder=999)
        ax.text(m[i][0], m[i][1], m[i][2],  '%s' % (str(i)), size=20, zorder=999,
                color='k')

    your_mesh = meshes.Mesh.from_file('./assignment.stl')

    ax.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors))

    # Auto scale to the mesh size
    scale = your_mesh.points.flatten()
    ax.auto_scale_xyz(scale, scale, scale)

    plt.show()

    print('You would have seen a plot opened, sorry for unclarity in the same. Please enter the number of the base (enter 0 for the figure given in assignment)')
    number = int(input())

    print('Base set to the face 0. Confirming the same by scrolling around with the 3D plot opened in the parallel window')
    mesh.visual.face_colors[mesh.facets[number]] = [255, 200, 80, 255]

    mesh.show()

    print('Enter distance from the plane in mm which you need to slice')
    distance = int(input())

    slicer(distance, mesh.facets_origin[number],
           mesh.facets_normal[number], mode='any')


def main():
    # print('Enter The Step Height in mm')
    # step = int(input())

    m = []

    for i in range(0, len(mesh.facets)):

        if(mesh.facets_area[i] > 50):
            m.append(mesh.facets_origin[i])

    assignment1()
    assignment2()
    assignment3()

    # mesh.show()

    # for i in range(0, 50, step):
    #     slicer(i)


if __name__ == '__main__':
    main()
