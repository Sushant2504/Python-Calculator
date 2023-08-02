from sympy import symbols, diff, tan, solve
import base64
from io import BytesIO

def draw_figure():
    buffer = BytesIO()
    plt.savefig(buffer, format= 'png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph
   
def find_tangent_normal(expression, x_value):
    x = symbols('x')
    
    derivative = diff(expression, x)

    slope = derivative.subs(x, x_value)

   
    y_value = expression.subs(x, x_value)

    
    tangent_line = slope * (x - x_value) + y_value

    normal_slope = -1 / slope
    normal_line = normal_slope * (x - x_value) + y_value

    return tangent_line, normal_line


from sympy import sympify

# x_value = float(input("Enter the x-coordinate of the point: "))

# tangent, normal = find_tangent_normal(expression, x_value)
# print("Tangent line:", tangent)
# print("Normal line:", normal)

import matplotlib.pyplot as plt
from sympy import*
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



# def draw_figure(canvas, figure):
#         figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
#         figure_canvas_agg.draw()
#         figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
#         return figure_canvas_agg



def TN_plot(v, u, e):
        dataSize = 1000
        x = np.linspace(-5,5,100)
        y1 = eval(str(v))
        y2 = eval(str(u))
        y3 = eval(str(e))

        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('zero')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        
        plt.plot(x, y1, 'b--', label = 'tangent')
        plt.plot(x, y2, 'g--', label = 'normal')
        plt.plot(x, y3, 'r', label = 'function')
        plt.title("Tangent and Normal")
        plt.legend()
        return draw_figure()


# print("Graph of tangent, normal: ")
# plotter(tangent, normal, expression)
