from sympy import symbols, diff, tan, solve
from sympy import sympify, integrate, Abs
import base64
from io import BytesIO
def calculate_area(f, g, x, a, b):
    area = integrate(Abs(f - g), (x, a, b))
    return area

import matplotlib.pyplot as plt
from sympy import*
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

x = symbols('x')


def draw_figure():
    buffer = BytesIO()
    plt.savefig(buffer, format= 'png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph
   
def plot_area(v, u, a, b):
        dataSize = 1000
        x = np.linspace(-5,5,100)
        y1 = eval(str(v))
        y2 = eval(str(u))

        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        
        plt.plot(x, y1, 'r', label="f(x)")
        plt.plot(x, y2, 'b', label="g(x)")
        # plt.plot(x, y3, 'r', label = 'function')
        plt.title("Area between f(x) and g(x)")
        plt.fill_between(x, y1, y2, color="grey", alpha=0.3, hatch='|')
        plt.legend()
        return draw_figure()