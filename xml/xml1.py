import xml.etree.ElementTree as ET

with open('xml1.xml') as f:
    tree = ET.parse(f)
    root = tree.getroot()

print('-------------------------------')  
for child in root.iter():
    print(child.tag , " : ", child.text.strip())
    
print('-------------------------------')   

xml_content = ET.tostring(root).decode('utf-8')
print(xml_content)
print('-------------------------------') 

new_data = ET.SubElement(root,'person3')

name = ET.SubElement(new_data, 'name')
name.text = 'C'
age = ET.SubElement(new_data, 'age')
age.text = '30'
cmd = ET.SubElement(new_data, 'cmd')
cmd.text = 'happy'
value = ET.SubElement(new_data, 'value')
value.text = '300'

tree.write('xml1_new.xml')  



