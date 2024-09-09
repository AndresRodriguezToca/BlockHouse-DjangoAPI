from django.http import JsonResponse

def candlestick_data(request):
    data = {
        'data': [
            {'x': '2024-01-01', 'open': 100, 'high': 130, 'low': 80, 'close': 120},
            {'x': '2024-01-02', 'open': 120, 'high': 140, 'low': 100, 'close': 110},
            {'x': '2024-01-03', 'open': 110, 'high': 150, 'low': 90, 'close': 140},
            {'x': '2024-01-04', 'open': 140, 'high': 170, 'low': 110, 'close': 115},
            {'x': '2024-01-05', 'open': 115, 'high': 160, 'low': 100, 'close': 145},
            {'x': '2024-01-06', 'open': 145, 'high': 180, 'low': 110, 'close': 125},
        ]
    }
    return JsonResponse(data)

def line_chart_data(request):
    data = {
        'data': [
            {
                "labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug"],
                "data": [10, 20, 30, 40, 20, 70, 190, 10]
            },
        ]
    }
    return JsonResponse(data)

def bar_chart_data(request):
    data = {
        'data': [
            {
                "labels": ["Product A", "Product B", "Product C", "Product D", "Product E"],
                "data": [100, 150, 200, 50, 300]
            },
        ]
    }
    return JsonResponse(data)

def pie_chart_data(request):
    data = {
        'data': [
            {
                "labels": ["Green", "Blue", "Purple", "Orange"],
                "data": [245, 150, 140, 198]
            },
        ]
    }
    return JsonResponse(data)
