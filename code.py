import tkinter as tk
import matplotlib.path as mplPath
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def check_inside_outside(vertices, point):
    poly_path = mplPath.Path(np.array(vertices))
    return poly_path.contains_point(point)

def is_inside_outside(vertices, n, point_entries, inside_label, outside_label):
    points = []
    inside = ["Inside"]
    outside = ["Outside"]
    for i in range(n):
        x_value = int(point_entries[i][0].get())
        y_value = int(point_entries[i][1].get())
        points.append([x_value, y_value])

    pts = np.array(vertices)
    p = Polygon(pts, ec='blue', fc='none')
    ax.add_patch(p)

    for i in points:
        if check_inside_outside(vertices, i):
            inside.append(i)
            color = 'green'
        else:
            outside.append(i)
            color = 'red'
        ax.scatter(i[0], i[1], color=color)

    canvas.draw()
    inside_label.config(text=inside)
    outside_label.config(text=outside)


def clear_input(vertex_entries, point_entries):
    for entry in vertex_entries:
        entry[0].delete(0, tk.END)
        entry[1].delete(0, tk.END)

    for point_entry in point_entries:
        point_entry[0].delete(0, tk.END)
        point_entry[1].delete(0, tk.END)


def clear_output(inside_label, outside_label):
    inside_label.config(text="")
    outside_label.config(text="")

def clear_all(vertex_entry, vertex_entries, point_entry, point_entries, inside_label, outside_label):
    vertex_entry.delete(0, tk.END)
    point_entry.delete(0, tk.END)
    clear_input(vertex_entries, point_entries)
    clear_output(inside_label, outside_label)


def show_result():
    vert = int(vertex_entry.get())
    vertices = []
    for i in range(vert):
        x_value = int(vertex_entries[i][0].get())
        y_value = int(vertex_entries[i][1].get())
        vertices.append([x_value, y_value])
    n = int(point_entry.get())
    result_window = tk.Toplevel()
    if vert > 2 and n > 0:
        result_window.title("Result")
    result_window.geometry("500x500")
    point_label = tk.Label(result_window, text="ENTER POINTS:", font = ('Arial', 15))
    point_label.pack(pady = 10)
    point_entries = []
    for i in range(n):
        point_x_label = tk.Label(result_window, text="Point " + str(i + 1) + " X," + str(i + 1) + " Y:", font=("Arial", 12))
        point_x_label.pack()
        point_x_entry = tk.Entry(result_window,width=12)
        point_y_entry = tk.Entry(result_window,width=12)
        point_x_entry.pack()
        point_y_entry.pack()
        point_entries.append((point_x_entry, point_y_entry))
    inside_label = tk.Label(result_window, text="")
    inside_label.pack()
    outside_label = tk.Label(result_window, text="")
    outside_label.pack()

    calculate_button = tk.Button(result_window, text="Calculate",font=("Noto Sans", 12), command=lambda: is_inside_outside(vertices, n,point_entries, inside_label, outside_label))
    calculate_button.pack()

    clear_all_button = tk.Button(result_window, text="Clear All", font=("Noto Sans", 12), command=lambda: clear_all(vertex_entry, vertex_entries, point_entry, point_entries, inside_label, outside_label))
    clear_all_button.pack()

root = tk.Tk()
root.title("Polygon Checker")
root.geometry("700x700")

input_frame = tk.Frame(root)
input_frame.pack(side="left", padx=20, pady=20)

graph_frame = tk.Frame(root)
graph_frame.pack(side="right", padx=20, pady=20, fill="both", expand=True)

frame = tk.Frame(root)
label = tk.Label(root, text = "GIVE INPUTS", font = ('Arial', 15))
label.pack(padx=20, pady=20)

vertex_label = tk.Label(root, text="Enter number of vertices:",font=("Noto Sans", 12))
vertex_label.pack()

vertex_entry = tk.Entry(root,font=(14))
vertex_entry.pack()

point_label = tk.Label(root, text="Enter number of points:",font=("Noto Sans", 12))
point_label.pack()

point_entry = tk.Entry(root,font=(14))
point_entry.pack()
vertex_entries = []

def create_vertex_entries():
    global vertex_entries
    vert = int(vertex_entry.get())
    vertex_entries = []
    for i in range(vert):
        vertex_x_label = tk.Label(root, text="Vertex " + str(i + 1) + " X," + str(i + 1) + " Y:",font=("Arial", 12))
        vertex_x_label.pack()
        vertex_x_entry = tk.Entry(root,font=("Arial", 12), width=12)
        vertex_y_entry = tk.Entry(root,font=("Arial", 12), width=12)
        vertex_x_entry.pack()
        vertex_y_entry.pack()
        vertex_entries.append((vertex_x_entry, vertex_y_entry))

vertex_button = tk.Button(root, text="Get Vertices",font=("Noto Sans", 12), command=create_vertex_entries)
vertex_button.pack()

result_button = tk.Button(root, text="Input Points",font=("Noto Sans", 12), command=show_result)
result_button.pack()

fig = plt.Figure(figsize=(5, 5), dpi=100)
ax = fig.add_subplot(111)
canvas = FigureCanvasTkAgg(fig, master=graph_frame)
canvas.draw()
canvas.get_tk_widget().pack(fill="both", expand=True)


root.mainloop()
