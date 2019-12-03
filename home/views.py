import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from plotly.offline import plot
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from .predictor import rf_model, size


# Create your views here.
@login_required
def home(request):
    return render(request, 'home/home.html')


@login_required
def chart(request):
    return render(request, 'home/chart.html')


@login_required
def tree(request):
    return render(request, 'home/tree.html')


@login_required
def table(request):
    return render(request, 'home/table.html')


@login_required
def graph(request):
    return render(request, 'home/graph.html')


@login_required
def pie(request):
    def get_pie():
        labels = ['Male', 'Female']
        fig = go.Figure(data=[go.Pie(labels=labels, values=size, hole=.3)])
        fig.update_layout(title_text="Gender Count in Dataset")
        plot_div = plot(fig, output_type='div', include_plotlyjs=False)
        return plot_div

    context = {
        'plot_graph': get_pie()
    }

    return render(request, 'home/pie.html', context)


@login_required
def result(request):
    context = {'form': {}}
    if request.method == 'POST':
        context['form']['age'] = request.POST.get('age', 'Missing Data')
        context['form']['sex'] = request.POST.get('sex', 'Missing Data')
        context['form']['cp'] = request.POST.get('cp', 'Missing Data')
        context['form']['trestbps'] = request.POST.get('trestbps', 'Missing Data')
        context['form']['chol'] = request.POST.get('chol', 'Missing Data')
        context['form']['fbs'] = request.POST.get('fbs', 'Missing Data')
        context['form']['restecg'] = request.POST.get('restecg', 'Missing Data')
        context['form']['thalach'] = request.POST.get('thalach', 'Missing Data')
        context['form']['exang'] = request.POST.get('exang', 'Missing Data')
        context['form']['oldpeak'] = request.POST.get('oldpeak', 'Missing Data')
        context['form']['slope'] = request.POST.get('slope', 'Missing Data')
        context['form']['ca'] = request.POST.get('ca', 'Missing Data')
        context['form']['thal'] = request.POST.get('thal', 'Missing Data')
        context['prediction'] = rf_model.predict([[int(x) if type(x) == 'int' else float(x) for x in context['form'].values()]])[0]
    else:
        context['message'] = 'No information was provided'
    return render(request, 'home/result.html', context)
