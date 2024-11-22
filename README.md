# Project03_A*
## FRC
FRC stands for First Robotics Competition. I am really passionate about FRC and wanted to make a path planner for the differing positions on the field.
## A* Pathfinding
### Algorithm
I implemented a basic, common A* Pathfinding algorithm. I began by initializing an openlist and a closedlist and gave the algorithm a starting node. The algorithm then searches every node that is walkable adjacent to the starting node, then calculates an F score for those nodes and add them to the openlist. The F score is calculated by calculating the distance to the starting node(G score) and the distance to the end node(H score or heuristic). Then, I find the node in the openlist with the smallest F score(using a heapqueue). I add it to the closedlist and look at all of those neighbors and repeat the process. 
### Heuristic Optimization
I used 3 different heuristics in my algorithm, Euclidean Distance, Diagonal Distance(Chebyshev), and Diagonal Distance(Octile). I found that Diagonal Distance(Octile) or Euclidean Distance worked the best. The Euclidean Distance is just the pythagorean theorem. The Octile Diagonal Distance is more complex, here is my function that calculated it:
```
dx = abs(child.position[0] - end[0])
    dy = abs(child.position[1]-end[1])
    #d = 1, d2 = 1 (d,d2,d)
    return int((1 * (dx + dy) + (math.sqrt(2) - 2 * 1) * min(dx, dy))*10)
```
## Optimization
### Smoothing
I did some research into smoothing paths after going through the A* algorithm. This would make the path more realistic for the robot. However, this requires a walkable function(to see if a line is obstructed), which I found difficult to implement in pygame.
### Heirarchical
Originally, my grid for the a* was every single pixle, which made the a* incredibly slow. Therefore, I researched Heirarchical Pathfinding. Hierarchical Pathfinding divides up the grid into larger chunks, calculates the path using larger chunks, then calculates the smaller path through gates in the larger path.


## Sources
- https://webdocs.cs.ualberta.ca/%7Emmueller/ps/hpastar.pdf
- https://gamedev.stackexchange.com/questions/192183/how-does-hpahierarchical-pathfinding-a-really-work
- https://web.archive.org/web/20170518005643/http://www.gamasutra.com/view/feature/131505/toward_more_realistic_pathfinding.php?page=2
- https://web.archive.org/web/20171022224528/http://www.policyalmanac.org:80/games/aStarTutorial.htm
