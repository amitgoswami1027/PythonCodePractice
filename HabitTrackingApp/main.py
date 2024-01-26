import requests
from datetime import datetime

USERNAME = "amitgoswami"
TOKEN = "kwjbfjbu89hweubfjwbe"
GRAPH_ID = "graph1"

# HTTP GET 
# HTTP POST
# HTTP PUT
# HTTP DELETE

# https://pixe.la/
# Pixela Info : https://docs.pixe.la/entry/post-graph
# Step-01
# Create your user account
# Call /v1/users API by HTTP POST.
# $ curl -X POST https://pixe.la/v1/users -d '{"token":"thisissecret", "username":"a-know", "agreeTermsOfService":"yes", "notMinor":"yes"}'
# {"message":"Success.","isSuccess":true}

pixela_endpoint ="https://pixe.la/v1/users"

user_params = {

    "token": USERNAME,
    "username" : TOKEN,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes",

}

#response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)

# Step-02
# Create a graph definition
# Call /v1/users/<username>/graphs by HTTP POST.
# $ curl -X POST https://pixe.la/v1/users/a-know/graphs -H 'X-USER-TOKEN:thisissecret' -d '{"id":"test-graph","name":"graph-name","unit":"commit","type":"int","color":"shibafu"}'
# {"message":"Success.","isSuccess":true}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    
    "id" : GRAPH_ID,
    "name": "Cycling Graph",
    "unit" : "Km",
    "type" : "float",
    "color" : "ajisai"
}

headers = {

    "X-USER-TOKEN" : TOKEN
}

#response = requests.post(url=graph_endpoint,json=graph_config, headers=headers)
#print(response.text)

#Step-03
#Get the graph!
#Browse https://pixe.la/v1/users/a-know/graphs/test-graph ! This is also /v1/users/<username>/graphs/<graphID> API.
# https://pixe.la/v1/users/amitgoswami/graphs/graph1

#Step-04
#Post value to the graph
#Call /v1/users/<username>/graphs/<graphID> by HTTP POST.
#$ curl -X POST https://pixe.la/v1/users/a-know/graphs/test-graph -H 'X-USER-TOKEN:thisissecret' -d '{"date":"20180915","quantity":"5"}'
#{"message":"Success.","isSuccess":true}

#pixela_creation_endpoint = "/v1/users/<username>/graphs/<graphID>"
pixela_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
print(today.strftime("%Y%m%d"))

pixela_data ={

    "date" : today.strftime("%Y%m%d"),
    "quantity" : "9.75"
}

response = requests.post(url=pixela_creation_endpoint,json=pixela_data,headers=headers)
print(response.text)

