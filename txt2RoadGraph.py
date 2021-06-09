import graph as RG
from pyproj import Transformer
import pickle


epsg = input("EPSG code of the input projection:")
inProj = 'epsg:'+epsg
outProj = 'epsg:4326'
transformer = Transformer.from_crs(inProj, outProj)

graph = RG.RoadGraph()

max_lon = -1000000
max_lat = -1000000
min_lon = 1000000
min_lat = 1000000

vertices = {}
with open("vertices.txt", 'r') as f1:
	for line in f1:
		temp = line.strip('\n').split(',')
		lat, lon = transformer.transform(float(temp[1]), float(temp[2]))
		vertices[temp[0]] = (lat, lon)
		if lon > max_lon:
			max_lon = lon
		if lon < min_lon:
			min_lon = lon
		if lat > max_lat:
			max_lat = lat
		if lat < min_lat:
			min_lat = lat

graph.region = [min_lat, min_lon, max_lat, max_lon]
print([min_lat, min_lon, max_lat, max_lon])

# Reading edges
edges = []
with open("edges.txt", 'r') as f2:
	for line in f2:
		temp = line.strip('\n').split(',')
		edges.append([vertices[temp[1]], vertices[temp[2]]])
		graph.addEdge(str(temp[1]), vertices[temp[1]][0], vertices[temp[1]][1], str(temp[2]), vertices[temp[2]][0], vertices[temp[2]][1])


graph.ReverseDirectionLink()

print("Done.")
filename = input("choose a filename:")

pickle.dump(graph, open(filename,"wb"))

