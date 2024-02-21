import json

file_path = "/Users/zere/Desktop/python/sample-data.json"  # Update the file path with the correct file name and extension

with open(file_path, "r") as my_file:
    json_string = my_file.read()

data = json.loads(json_string)

interfaces = data.get('imdata', [])
print("Interface Status")
print("=" * 80)
print("{:<50} {:<20} {:<8} {:<6}".format("DN", "Description", "Speed", "MTU"))
print("-" * 50, "-" * 20, "-" * 8, "-" * 6)

for i in interfaces:
    l1physif = i.get('l1PhysIf', {})
    att = l1physif.get('attributes', {})
    
    dn = att.get('dn', '')
    descr = att.get('descr', '')
    speed = att.get('speed', 'inherit')
    mtu = att.get('mtu', '')
    
    print("{:<50} {:<20} {:<8} {:<6}".format(dn, descr, speed, mtu))
