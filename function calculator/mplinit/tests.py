from django.test import TestCase

# Create your tests here.
# from sympy import symbols, diff, tan, solve

# # def find_tangent_normal(expression, x_value):
# #     x = symbols('x')
    
# #     derivative = diff(expression, x)

# #     slope = derivative.subs(x, x_value)

   
# #     y_value = expression.subs(x, x_value)

    
# #     tangent_line = slope * (x - x_value) + y_value

# #     normal_slope = -1 / slope
# #     normal_line = normal_slope * (x - x_value) + y_value

# #     return tangent_line, normal_line


# # from sympy import sympify

# # expression_str = input("Enter a function: ")
# # expression = sympify(expression_str)

# # x_value = float(input("Enter the x-coordinate of the point: "))

# # tangent, normal = find_tangent_normal(expression, x_value)
# # print("Tangent line:", tangent)
# # print("Normal line:", normal)

# # import matplotlib.pyplot as plt
# # from sympy import*
# # import numpy as np
# # from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



# # def draw_figure(canvas, figure):
# #         figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
# #         figure_canvas_agg.draw()
# #         figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
# #         return figure_canvas_agg



# # def plotter(v, u, e):
# #         dataSize = 1000
# #         x = np.linspace(-5,5,100)
# #         y1 = eval(str(v))
# #         y2 = eval(str(u))
# #         y3 = eval(str(e))

# #         fig = plt.figure()
# #         ax = fig.add_subplot(1, 1, 1)
# #         ax.spines['left'].set_position('center')
# #         ax.spines['bottom'].set_position('zero')
# #         ax.spines['right'].set_color('none')
# #         ax.spines['top'].set_color('none')
# #         ax.xaxis.set_ticks_position('bottom')
# #         ax.yaxis.set_ticks_position('left')
        
# #         plt.plot(x, y1, 'b--', label = 'tangent')
# #         plt.plot(x, y2, 'g--', label = 'normal')
# #         plt.plot(x, y3, 'r', label = 'function')
# #         plt.title("Tangent and Normal")
# #         plt.legend()
# #         plt.show()


# # print("Graph of tangent, normal: ")
# # plotter(tangent, normal, expression)



# from sympy import symbols, diff, tan, solve
# from sympy import sympify, Abs, integrate

# def calculate_area(f_expr, g_expr, x, a, b):
#     f = f_expr
#     g = g_expr
#     area = integrate(Abs(f - g), (x, a, b))
#     return area

# # Define the symbolic variable
# x = symbols('x')

# # Get the function expressions from the user
# f_expr = sympify(input("Enter the function f(x): "))
# g_expr = sympify(input("Enter the function g(x): "))

# # Get the integration limits from the user
# a = float(input("Enter the lower limit: "))
# b = float(input("Enter the upper limit: "))

# # Calculate the area between the curves
# area = calculate_area(f_expr, g_expr, x, a, b)

# # Print the area
# print("Area between curves:", area)

# import matplotlib.pyplot as plt
# from sympy import*
# import numpy as np
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



# def draw_figure(canvas, figure):
#         figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
#         figure_canvas_agg.draw()
#         figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
#         return figure_canvas_agg



# def plotter(v, u):
#         plt.rcParams["figure.figsize"] = [7.50, 3.50]
#         plt.rcParams["figure.autolayout"] = True
#         x = np.linspace(0, 1, 100)
#         c1 = v
#         c2 = u
#         plt.plot(x, c1)
#         plt.plot(x, c2)
#         plt.fill_between(x, c1, c2, color="grey", alpha=0.3, hatch='|')
#         plt.show()

# plotter(f_expr, g_expr)



