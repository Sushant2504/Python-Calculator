from django.shortcuts import render
from .models import Mplinit, TNN, ULLIM
from .utils import plotter, wolf_solution
from .utils import wolf_step_by_step, tn, area_c, summery
from django.contrib import messages
# Create your views here.
def main(request):
    # if request.GET.get('Plot') == 'Plot':
   
    return render(request, 'main.html')
    #  print('user clicked button')

    # qs = Mplinit.objects.all()
    # x = [x.item for x in qs]
    # y = [y.price for y in qs]

def graph(request):
   
    return render(request, 'graph.html', {})

def algebra(request):
    if request.method == "POST":
        expr = request.POST.get('expr')
        expression = Mplinit(expr = expr)
        expression.save()
        res_exp = wolf_solution(expression)
        # step_by_step = wolf_setp_by_step(expression)
        # sol = {'res_exp': res_exp, 'step_by_step':step_by_step}
        return render(request, 'algebra.html', {'res_exp': res_exp})
    # if request.method == 'POST':
    #     # expr = request.POST.get('expr')
    #     expr = Mplinit.objects.last()
    #     steps = wolf_setp_by_step(expr)
    #     return render(request, 'algebra.html', {'steps': steps})
    return render(request, 'algebra.html', {})

def steps(request):
    if request.method == "POST":
        expr = request.POST.get('expr')
        expression = Mplinit(expr = expr)
        expression.save()
        steps = wolf_step_by_step(expression)
        return render(request, 'steps.html', {'steps': steps})
    return render(request, 'steps.html', {})

def tangent_n_normal(request):
    # pass
    if request.method == "POST":
        expr = request.POST.get('expr')
        x_value = request.POST.get('x_value')
        expression = TNN(expr = expr, x_value=x_value)
        expression.save()
        tangent, normal, whole_graph = tn(expr, x_value)
        return render(request, 'tangent_n_normal.html', {'graph': whole_graph, 'tangent': tangent, 'normal': normal})
    return render(request, 'tangent_n_normal.html', {})

def normal_plot(request):
    # pass
    if request.method == "POST":
        expr = request.POST.get('expr')
        expression = Mplinit(expr = expr)
        expression.save()
        chart = plotter(expression)
        return render(request, 'normal_plot.html', {'chart': chart})
    return render(request, 'normal_plot.html', {})

def area_curve(request):
    # pass
    if request.method == "POST":
        f = request.POST.get('f')
        g = request.POST.get('g')
        l_lim = request.POST.get('l_lim')
        u_lim = request.POST.get('u_lim')
        expression = ULLIM(f=f, g=g, l_lim=l_lim, u_lim=u_lim)
        area, graph = area_c(f, g, l_lim, u_lim)
        return render(request, 'area_curve.html', {'area': area, 'graph': graph})
    return render(request, 'area_curve.html', {})

def summerizer(request):
    if request.method == "POST":
        text = request.POST.get('summ')
        perc = request.POST.get('perc')
        expression = TNN(expr = text, x_value=perc)
        expression.save()
        summery = summery(text, perc)
        return render(request, 'summerizer.html', {'summery': summery})
    return render(request, 'summerizer.html', {})