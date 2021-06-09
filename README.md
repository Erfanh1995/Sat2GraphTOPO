# TOPO Usage

"Here, the graph files gt.p and prop.p are all in the same format as what we used in Sat2Graph - a python dictionary where each key is the coordinate of a vertex (denoted by x) and the corresponding value is a list of x's neighboring vertices."  

All rights for the topo algorithm and its documentations go to the authors and creators of Sat2Graph ([Songtao He](https://github.com/songtaohe/) and his collaborators). [Link](https://github.com/songtaohe/Sat2Graph) to the main repo.

txt2RoadGraph is a tool I have created for conversions from text-based graphs to a pickle file containing a RoadGraph object, suitable for this TOPO evaluation.
Simply put your vertices.txt and edges.txt in the same directory and convert them to a pickle file:
```bash
python3 txt2RoadGraph.py
```

 Then you are all set to start the evaluation:
```bash
python3 main.py -graph_gt data/chicago_osm -graph_prop data/chicago_james -output toporesult.txt
```


# TOPO Parameters
Parameters | Note
--------------------- | -------------
Propagation Distance  | 300 meters for large tiles and 150 meters for small tiles (see line 127-130 in main.py)
Propagation Interval  | Default is 5 meters. Config with -interval flag.
Matching Distance Threshold | Default is 10 meters. Config with -matching_threshold flag.
Matching Angle Threshold | 30 degrees
One-to-One Matching | True


# Dependency
* hopcroftkarp
* rtree
* pyproj (for txt2RoadGraph)
