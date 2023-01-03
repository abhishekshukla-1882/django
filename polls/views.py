from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.shortcuts import redirect
import json
# Create your views here.
def home(req):
    print(req)
    print('yes')
    
    url = 'https://url24.myshopify.com/admin/oauth/authorize?client_id=4b426dc6838c4a8ef11b9b0d1ab91330&scope=write_products,read_shipping&redirect_uri=http://127.0.0.1:8000/shop/shoping&state=1245'

    # location = "delhi technological university"
    
    # # defining a params dict for the parameters to be sent to the API
    # PARAMS = {'address':location}
    
    # sending get request and saving the response as response object
    # r = requests.get(url = url)
    # print(r)
    # print("r1")
    # extracting data in json format
    # data = r.json()
    # data = json.loads(r.text)
    # print(data)
    print('data')
    response = redirect(url)
    return response
    # return HttpResponse(url)
def shoping(req):
    print(req)
    url = 'https://url24.myshopify.com/admin/oauth/access_token?client_id=4b426dc6838c4a8ef11b9b0d1ab91330&client_secret=19cb29d1166b3767691d2d439c168ce1&code=a3f08db213e7547d026861eef003203e'
    r = requests.post(url = url)
    data = r.json()
    print(data)
    print(data['access_token'])
    # curl -X GET \
    print('access_token')
    url2 = 'https://url24.myshopify.com/admin/api/2022-10/products.json'
    header = {
        'Content-Type' : 'application/json',
        'X-Shopify-Access-Token' : 'shpua_85e6c1854b113a6c400a9216e9f98b67'
    }
    rr = requests.get(url = url2, headers=header)
    dataa = rr.json()
    print(rr)

    print('shop')
    print(dataa)
    return HttpResponse('hhh')