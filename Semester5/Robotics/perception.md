making sense of the unstructured real world

**Perception**: information input  
**Cognition**: (rational) information processing  
**Motorics**: information output  

**components:**
- sensors: camera, IR sensors, micorphones, touch sensors, ...  
- data representation: eg semantic maps  

Robot recognition:  
- enable robots to observe and interact with the environment  
- guides physical robot in real world environments for pickup etc  

Computer vision:  
- various fields beyond robotics  
- extracting information from images  
- object detection, facial recognition, image segmentation, ...

Typical Tasks:  
- object detection  
- environment mapping  
- human detection  
- gesture, voice recognition  
- obstacle detection  

Preprocessing:  
Downsampling: reduce data size and search space  
Random Sample Concensus (RANSAC): find and remove dominant planes  
Smoothing: softens corners and edges  

Registration:  
Photogrammetry: generate 2.5/3D data from 2d sequences -> multiple pictures from different angles result in a 3d model  
Meshing: create a manifold from a point cloud  
Optical Flow: tracking objects/people in images  
Feature extraction: detect objects/places..  

Tools: OpenCV, Point Cloud Library (PCL)


