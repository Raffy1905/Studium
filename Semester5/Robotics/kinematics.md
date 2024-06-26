Link: rigid body  
Joint:  
 - prismatic - entlang des joint  
 - revolute - rotierend  

Configuration: positions of all points of the robot  

Degree of Freedom: 1..n per joint (equal to amount of joints) - eg 7 for sawyer  
Task Space: Space the task takes place in. (eg plane for a chalkboard)  
Joint/configuration Space: space with all configurations. Each configuration is represented as a Point  
End Effector: Effector sitting at the end of the robot arm. eg gripper, drill, etc...  

Forward/Direct Kinematics: Joint -> Task Space  
"Where is the end-effector located in space given the joint configurations?"  
Backward/Inverse Kinematics: Task -> Joint Space  
"What does the Configuration have to be for the end-effector the be at a specific position?"  
Kinematic Chain: links+joints: base -> end effector  

3D-Space: 6 Parameters:  
(x, y, z, yaw, pitch, roll)  

Denavit-Hartenberg (DH) Convention:  
only 4 parameters, because joints can only rotate in one direction.

