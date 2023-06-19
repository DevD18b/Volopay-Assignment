import datetime
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Data
from .serializer import DataSerializer
from django.db.models import Sum

@api_view(['GET'])
def getData(request):
    # get the first 5 from the database
    data = Data.objects.all()[:5]
    serializer = DataSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def total_items(request):
    # get the parameters from the request
    department = request.GET.get('department') # string 
    start_date = request.GET.get('start_date') # date
    end_date = request.GET.get('end_date') # date

    print(department)

    # validate the parameters
    if department is None or start_date is None or end_date is None:
        return Response({"error": "Please provide all the parameters"})
    # check if the department is string
    if not isinstance(department, str):
        return Response({"error": "Department should be a string"})
    # check if the start_date and end_date are in the Date format
    try:
        start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
    except ValueError:
        return Response({"error": "Please provide the date in the format YYYY-MM-DD"})
    
    #get the count of total number of seats sold between the start date and the enddate of the deartment
    listofseats = Data.objects.filter(department=department, date__range=[start_date, end_date]).values_list('seats', flat=True)
    total_seats = sum(listofseats)
    return Response({"total_seats_sold": total_seats})




@api_view(['GET'])
def nth_most_total_item(request):
    # get the parameters from the request
    item_by = request.GET.get('item_by')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    n = int(request.GET.get('n'))

    # Validate Paramerets
    try:
        n = int(n)
        if n <= 0:
            raise ValueError
    except (ValueError, TypeError):
        return Response({'error': 'Invalid value for parameter "n".'})

    if item_by not in ['quantity', 'price']:
        return Response({'error': 'Invalid value for parameter "item_by".'})
      # check if the start_date and end_date are in the Date format
    try:
        start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
    except ValueError:
        return Response({"error": "Please provide the date in the format YYYY-MM-DD"})

   # Get the nth most sold item
    sold_items = None

    if item_by == 'quantity':  
        # get the second most sold software in terms of quantity sold
        sold_items = Data.objects.filter(date__range=(start_date, end_date)) # get the data between the start and end date
        sold_items = sold_items.values('software') # get the software name
        sold_items = sold_items.annotate(total_quantity=Sum('seats')) # get the total quantity sold
        sold_items = sold_items.order_by('-total_quantity') # order by the total quantity sold

    elif item_by == 'price':
        sold_items = Data.objects.filter(date__range=(start_date, end_date)) # get the data between the start and end date
        sold_items = sold_items.values('software') # get the software name
        sold_items = sold_items.annotate(total_price=Sum('amount')) # get the total price sold
        sold_items = sold_items.order_by('-total_price') # order by the total price sold
    
    # check if the sold_items is empty
    if sold_items is None or not sold_items.exists():
        return Response({'error': 'No data found for the given date range.'})
    # check if the n is greater than the length of the sold_items
    if n <= 0 or n > len(sold_items):
        return Response({'error': 'Invalid value of n.'})
    # get the nth most sold item
    ans = sold_items[n - 1]['software']
    return Response({'n_most_sold_item': ans, 'item_by': item_by})

    

@api_view(['GET'])
def get_percent(request):
    # get the parameters from the request
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    # Validate Paramerets
    try:
        start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
    except ValueError:
        return Response({"error": "Please provide the date in the format YYYY-MM-DD"})
    
    # get the total number of seats sold between the start date and the enddate of the deartment
    seats_sold = Data.objects.filter(date__range=[start_date, end_date]).values_list('seats', flat=True)
    # convert the seats_sold to int
    seats_sold = [int(seats) for seats in seats_sold]
    # get the total number of seats sold
    total_seats_sold = sum(seats_sold)

    # get the percentage of seats sold department wise
    depwise_seats_sold = Data.objects.filter(date__range=[start_date, end_date]).values('department').annotate(total_seats=Sum('seats'))
    
    for item in depwise_seats_sold: # calculate the percentage of seats sold
        item['percentage'] = (item['total_seats']/total_seats_sold)*100

    ans = {} 
    for item in depwise_seats_sold:
        # add the department and percentage to the ans dictionary
        ans[item['department']] = item['percentage']
    return Response(ans) 
    

@api_view(['GET'])
def monthly_sales(request):
    # get the parameters from the request
    product = request.GET.get('product')
    year = request.GET.get('year')

    # Validate Paramerets
    try:
        year = int(year)
        if year <= 0:
            raise ValueError
    except (ValueError, TypeError):
        return Response({'error': 'Invalid value for parameter "year".'})
    # check if the product is string
    if not isinstance(product, str):
        return Response({"error": "Product should be a string"})
    
    # get the monthly sales for the given product and year
    monthly_sales = Data.objects.filter(software=product, date__year=year) # get the data for the given product and year
    monthly_sales = monthly_sales.values('date__month') # get the month
    monthly_sales = monthly_sales.annotate(total_sales=Sum('amount')) # get the total sales
    
    ans = [0] * 12 # initialize the ans array
    for item in monthly_sales: # add the total sales to the ans array
        ans[item['date__month'] - 1] = item['total_sales'] 

    return Response(ans)
