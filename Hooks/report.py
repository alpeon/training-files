#!/bin/python3

import base64
from sys import argv
import xml.etree.ElementTree as ET

data = argv[1]

xml_bytes = base64.b64decode(data)
data_text = xml_bytes.decode("utf8")

def parse(data):

    try:
        root = ET.fromstring(data)
        vmid = root.findtext('ID')
        uname = root.findtext('UNAME')
        name = root.findtext('NAME')
        write_report(vmid=vmid, name=name, uname=uname)

    except ET.ParseError as e:
        print("Failed to parse XML:", e)

def write_report(vmid, name, uname):

    with open('/tmp/report.txt', 'a') as file:
        file.write('New VM data:\n')
        file.write(f'VM Name: {name}\n')
        file.write(f'VM ID: {vmid}\n')
        file.write(f'Owner: {uname}\n')
        file.write('*******************\n')

    print('Reporting: DONE!')

parse(data=data_text)