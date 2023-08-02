
# import PySimpleGUI as sg
import numpy as np
from math import *
import matplotlib.pyplot as plt
from sympy import*
from bs4 import BeautifulSoup
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import requests
from letter_to_symbol.letters_to_symbol import convert
import tangent_n_normal.draw_tangent as tnnd
from tangent_n_normal import area as ar
from summery.summerizer import summerizer
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
   
def plotter(v):
    dataSize = 1000
    expr = sympify(v)
    x = np.linspace(-5,5,100)
    y = (eval(str(expr)))
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    
    plt.plot(x, y, 'r')
    # Instead of plt.show
    graph = draw_figure()
    return graph

# //wolfram

# from PIL import ImageTk, Image

# from io import BytesIO

# API endpoint
api_url = 'https://api.wolframalpha.com/v1/result'

# Your Wolfram|Alpha API key
api_key = 'AUPQ3J-YGJUQ875AU'

# User input query
def wolf_solution(v):
    query = str(v)

    params = {
        'appid': api_key,
        'i': query
    }

    response = requests.get(api_url, params=params)

    result = response.text.strip()

    return convert(result)

       
def wolf_step_by_step(v):
    api_link = 'https://api.wolframalpha.com/v2/query'


    # api_key = 'AUPQ3J-YGJUQ875AU'

# User input query
    query = str(v)

    params = {
    'appid': api_key,
    'input': query,
    'podstate': 'Result__Step-by-step+solution',
    'format': 'plaintext'
    }

# Send GET request

    response = requests.get(api_link, params=params)
    result = response.text.strip()
    data = result
    Bs_data = BeautifulSoup(data, "xml")
 
    plaintext = Bs_data.find_all('plaintext')
    return_string = ''
    for text in plaintext:
        t = text.string
        if(t == None):
            return_string += "\n"
        else:
            return_string += t+"<br/>"
    
    return return_string

def tn(v, u):
    x = symbols('x')
    expr = sympify(v)
    x_val = eval(u)
    tangent, normal = tnnd.find_tangent_normal(expr, x_val)
    whole_graph = tnnd.TN_plot(tangent, normal, expr)
    return tangent, normal, whole_graph

def area_c(v, u, a, b):
    x = symbols('x')
    f = sympify(v)
    g = sympify(u)
    area = ar.calculate_area(f,g,x,a,b)
    graph = ar.plot_area(f, g, a, b)
    return area, graph

def summery(text, perc):
   return summerizer(text, perc)