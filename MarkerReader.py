import xml.etree.ElementTree as ET

#def markerReader(xmlFile):
    #Create marker dictionary
markers = {}
    #Parse through XMl file
tree = ET.parse(r"C:\Cheese Project\test.xml")
root = tree.getroot()
    #Get to video tag
video = root.find(".library/event/project/sequence/spine/video")
vidStart = int(video.attrib["start"][:-1])

    #Iterate through marker tags
for child in video:
        #Check to make sure tag is a marker tag
    if child.tag == "marker":
        markerStart = round(eval(child.attrib["start"][:-1]) - vidStart)
        name = child.attrib["value"]
        markers[name] = markerStart
print(markers)