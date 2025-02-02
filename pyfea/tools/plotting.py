# -*- coding: utf-8 -*-
#Created on Thu Jun 20 23:13:03 2019
#@author: Christophe

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D; _ = Axes3D #hide spyder warning msg
import numpy as np
import pyvista as pv

def scatter3d_mpl(points):
    # plot the surface
    plt3d = plt.figure().gca(projection='3d')
    ax = plt.gca()
    ax.scatter(points[:,0], points[:,1], points[:,2], color='green')
    
    #Set equal axes. Thank you P. Sharpe :)
    def set_axes_equal(ax):
        '''Make axes of 3D plot have equal scale so that spheres appear as spheres,
        cubes as cubes, etc..  This is one possible solution to Matplotlib's
        ax.set_aspect('equal') and ax.axis('equal') not working for 3D.
        Input
          ax: a matplotlib axis, e.g., as output from plt.gca().
        '''
    
        x_limits = ax.get_xlim3d()
        y_limits = ax.get_ylim3d()
        z_limits = ax.get_zlim3d()
    
        x_range = abs(x_limits[1] - x_limits[0])
        x_middle = np.mean(x_limits)
        y_range = abs(y_limits[1] - y_limits[0])
        y_middle = np.mean(y_limits)
        z_range = abs(z_limits[1] - z_limits[0])
        z_middle = np.mean(z_limits)
    
        # The plot bounding box is a sphere in the sense of the infinity
        # norm, hence I call half the max range the plot radius.
        plot_radius = 0.5*max([x_range, y_range, z_range])
    
        ax.set_xlim3d([x_middle - plot_radius, x_middle + plot_radius])
        ax.set_ylim3d([y_middle - plot_radius, y_middle + plot_radius])
        ax.set_zlim3d([z_middle - plot_radius, z_middle + plot_radius])
    
        plt.tight_layout()
        
    set_axes_equal(ax)

def scatter3d(points):
    p = pv.BackgroundPlotter()
    point_cloud = pv.PolyData(points)
    p.add_mesh(point_cloud)
    p.enable_eye_dome_lighting()
    p.show(window_size=[1024, 768])