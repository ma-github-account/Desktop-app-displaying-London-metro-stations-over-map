
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib.pyplot as plt 
import numpy as np
import cartopy.crs as ccrs
import cartopy.io.img_tiles as cimgt
from tkinter import ttk

def create_map():

    osm_img = cimgt.OSM()
    
    fig = plt.figure(figsize=(12,9))
    ax1 = plt.axes(projection=osm_img.crs)
    
    center_pt = [51.5098, -0.1180]
    zoom = 0.16
    extent = [center_pt[1]-(zoom*2.0),center_pt[1]+(zoom*2.0),center_pt[0]-zoom,center_pt[0]+zoom]
    ax1.set_extent(extent)
    
    scale = np.ceil(-np.sqrt(2)*np.log(np.divide(zoom,350.0)))
    scale = (scale<20) and scale or 19
    ax1.add_image(osm_img, int(scale))
    
    ax1.set_title ('London Metro Stations Locations')

    return fig , ax1

fig, ax1 = create_map()

window=tk.Tk()
window.wm_title("Map Displayer")
window.columnconfigure(0, weight=1)

zoom_info = tk.LabelFrame(window, text='Metro line setting')
zoom_info.grid(sticky=(tk.W + tk.E))
for i in range(2):
  zoom_info.columnconfigure(i, weight=1 )

lines_list = ["Picadilly","Bakerloo","East London","Jubilee","Metropolitan", "Northern", "Victoria"]

lines_variable = tk.StringVar()
ttk.Label(zoom_info, text='Metro line choice dropdown').grid(row=1, column=0)
ttk.Combobox(
  zoom_info,
  textvariable=lines_variable,
  values=lines_list
).grid(row=2, column=0, sticky=(tk.W + tk.E))

map_type_list = ["Map","Satellite Photo"]

reload_button_frame = tk.LabelFrame(window, text='Reload button')
reload_button_frame.grid(sticky=(tk.W + tk.E))

for i in range(3):
  reload_button_frame.columnconfigure(i, weight=1 )

tk.Label(reload_button_frame , text='Click Reload button to refresh the map after setting changes').pack(side=tk.TOP)
Reload_button = tk.Button(reload_button_frame, text='RELOAD')
Reload_button.pack(side=tk.LEFT)

canvas = FigureCanvasTkAgg(fig, master=window)
canvas.draw()
canvas.get_tk_widget().grid(row=7, column=0, sticky=(tk.W + tk.E))

Picadilly = [
[51.54097 ,-0.30061],
[51.61625 ,-0.13355],
[51.55847 ,-0.10561],
[51.495371 ,-0.325573],
[51.60700 ,-0.12418],
[51.54850 ,-0.11802],
[51.65117 ,-0.14811],
[51.51308 ,-0.12427],
[51.466988 ,-0.423035],
[51.4712899 ,-0.4527438],
[51.4594777 ,-0.44689658],
[51.55290 ,-0.11278],
[51.471290 ,-0.365853],
[51.473540 ,-0.356000],
[51.473689 ,-0.386471],
[51.50313 ,-0.15278],
[51.50169 ,-0.16030],
[51.57038 ,-0.09601],
[51.51807 ,-0.28838],
[51.499856 ,-0.313188],
[51.64739 ,-0.13192],
[51.481569 ,-0.351960],
[51.52671 ,-0.28417],
[51.523243 ,-0.124336],
[51.500801 ,-0.307856],
[51.56461 ,-0.35210],
[51.63240 ,-0.12765],
[51.556998 ,-0.335949],
[51.55093 ,-0.31598],
[51.59031 ,-0.10308],
[51.59709 ,-0.10939]
]

Bakerloo = [
[51.519560, -0.169068],
[51.53628278, -0.257622488],
[51.59205973, -0.334725352],
[51.53060655, -0.224253545],
[51.58173809, -0.316870809],
[51.53495818, -0.193963023],
[51.49894, -0.11216],
[51.52989409, -0.185888819],
[51.522660,-0.162996],
[51.56258091, -0.304072648],
[51.534179, -0.205257721],
[51.52344, -0.14713],
[51.57044666, -0.308566354],
[51.54402388, -0.275978856],
[51.52329728, -0.183777837],
[51.55122817, -0.29577538],
[51.53032031, -0.229378995]
]

East_London = [
[51.49787, -0.04967],
[51.477363, -0.0338817],
[51.47585, -0.04049],
[51.50089, -0.05211],
[51.51115, -0.05693],
[51.50451, -0.05607]
]

Jubilee = [
[51.49813 ,-0.06350],
[51.50362 ,-0.01987],
[51.60810 ,-0.29487],
[51.55250 ,-0.23884],
[51.5471715 ,-0.2050020],
[51.58422 ,-0.27880],
[51.55427 ,-0.25042],
[51.50056 ,+0.00360],
[51.59437 ,-0.28655],
[51.50384 ,-0.10478],
[51.53472 ,-0.17428],
[51.61895 ,-0.30241],
[51.54333 ,-0.17436],
[51.54678865 ,-0.191016868],
[51.54657 ,-0.19055],
[51.54919 ,-0.22106]
]

Metropolitan = [
[51.51394 ,-0.07537],
[51.67435 ,-0.60732],
[51.66822 ,-0.56053],
[51.70522733 ,-0.610986426],
[51.65429872 ,-0.518373353],
[51.64733268 ,-0.441479115],
[51.579335 ,-0.337052],
[51.62970512 ,-0.432070848],
[51.58503612 ,-0.362595264],
[51.57850117 ,-0.317857023],
[51.61098984 ,-0.423584422],
[51.60043795 ,-0.408812575],
[51.59270271 ,-0.380539158],
[51.57229051 ,-0.295813875],
[51.64027898 ,-0.473521454],
[51.65741058 ,-0.41745306],
[51.5795432 ,-0.353144584]
]

Northern = [
[51.53253 ,-0.10579],
[51.56536 ,-0.13474],
[51.44344113 ,-0.152945844],
[51.47950 ,-0.14200],
[51.55036 ,-0.16465],
[51.50095 ,-0.09446],
[51.57693 ,-0.21414],
[51.60300 ,-0.26427],
[51.53930 ,-0.14316],
[51.54390 ,-0.15384],
[51.46156 ,-0.13802],
[51.46522 ,-0.12950],
[51.45292257 ,-0.147562148],
[51.59556 ,-0.24996],
[51.41823649 ,-0.17800983],
[51.5872974705487, -0.16495632312818],
[51.61385, -0.27515],
[51.52774, -0.13303],
[51.60102, -0.19240],
[51.57249, -0.19410],
[51.52060, -0.13441],
[51.55645, -0.17851],
[51.58346, -0.22653],
[51.6506519031751, -0.194138165994553],
[51.57722 ,-0.14553],
[51.48823 ,-0.10587],
[51.55046 ,-0.14067],
[51.60892 ,-0.20965],
[51.40222413 ,-0.194599126],
[51.53427 ,-0.13901],
[51.480000 ,-0.128460],
[51.48214 ,-0.11284],
[51.41543048 ,-0.192262754],
[51.43578971 ,-0.159635693],
[51.42780008 ,-0.167910811],
[51.63022 ,-0.17917],
[51.55663 ,-0.13813],
[51.60922281219, -0.188711152265457],
[51.6181717295887, -0.185578887883903]
]

Victoria = [
[51.58698 ,-0.04104],
[51.46239 ,-0.115421],
[51.489081 ,-0.133037],
[51.58318 ,-0.07495],
[51.588878 ,-0.059808],
[51.48603 ,-0.12369],
[51.58293 ,-0.01996]
]

def display_list_of_stations_on_the_map(ax, list_of_stations):

    for station in list_of_stations:

        ax.scatter(station[1], station[0], color='r', s=35, alpha=1, transform=ccrs.PlateCarree())

def on_reset():

    lines_variable_value = lines_variable.get()

    fig, ax1 = create_map()

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().grid(row=7, column=0, sticky=(tk.W + tk.E))

    ax1.set_title ('London Metro Stations Locations \n Currently displayed metro line: ' + str(lines_variable_value))

    if lines_variable_value == "Picadilly":

        display_list_of_stations_on_the_map(ax1, Picadilly)

    elif lines_variable_value == "Bakerloo":

        display_list_of_stations_on_the_map(ax1, Bakerloo)

    elif lines_variable_value == "East London":

        display_list_of_stations_on_the_map(ax1, East_London)

    elif lines_variable_value == "Jubilee":

        display_list_of_stations_on_the_map(ax1, Jubilee)   

    elif lines_variable_value == "Metropolitan":

        display_list_of_stations_on_the_map(ax1, Metropolitan)   

    elif lines_variable_value == "Northern":

        display_list_of_stations_on_the_map(ax1, Northern) 

    elif lines_variable_value == "Victoria":

        display_list_of_stations_on_the_map(ax1, Victoria) 

Reload_button.configure(command=on_reset)

tk.mainloop()