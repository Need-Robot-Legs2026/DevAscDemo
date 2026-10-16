import xmltodict

with open('r1.xml') as file:
    xml_data = file.read()

data = xmltodict.parse(xml_data)

# print(data) # Prints all data
# print(data['router']['interfaces']['interface'][0]['ip']) # 192.168.1.254