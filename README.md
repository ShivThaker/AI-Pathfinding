# Implementing Pathfinding Algorithms

## Proposed Methodology
Pygame is a cross-platform set of Python modules which is used to create video games, 
consisting of computer graphics and sound libraries designed to be used with the 
Python programming language, and will be used here for the graphical representation 
for the project.

Class “Node” will include all the essentials

For informed search, we need a heuristic function f(n) = g(n) + h(n), which is a way to 
inform the search about the direction to a goal. It provides an informed way to guess 
which neighbour of a node will lead to a goal. First, the nodes and the grid should be 
created to provide a platform for the search. 

After that, we have to create a mechanism to detect wherever the user clicks and 
generate the starting/ending node or the barrier/wall nodes there. Then comes the 
algorithm itself, which will run on the grid when the user hits SPACEBAR. The user will have an option to choose from different algorithms (options will be displayed on the right). 

**GRID** (on a small scale)

S – Start node E – Target/End node

Black nodes will be the barriers and the line highlighted will be the path, if there is one.
The path will be different for different algorithms.

![1](https://user-images.githubusercontent.com/68414803/183497348-5ec2ceb5-181c-47a7-9aad-a0cc96f4c710.png)

A maze can also be generated on the grid, like using Recursive Back tracking algorithm, 
as it is fast, easy to understand, and straightforward to implement. The algo will follow a process to remove barriers from a pre-defined grid instead of waiting for the user to create them.

![2](https://user-images.githubusercontent.com/68414803/183497355-c9fc2348-78f7-4ae1-afa0-6163f4150e25.png)

The user can now create START and END node and run the algorithm like before.
Essential Pseudo-Code of this and all the pathfinding algorithms are discussed in 
subsequent sections.

The gird structure is shown below. All the child nodes are referred to as neighbors in 
the project. 

R – Right node

D – Down node

L – Left node

U – Up node

The following structure will continue, barrier nodes (black nodes) will be excluded from 
the tree itself. All this information is stored in a 2-D array “grid”. Discussed further in the implementation section. All the algorithms will follow simple steps until they reach the end node (if there is one). Then it will call a simple back tracer function to trace its path back to the starting node.

### BFS with a dynamic maze made by user
![5](https://user-images.githubusercontent.com/68414803/183497043-6ffacacf-4027-45ad-9b42-d4729cd06d4e.png)

### DFS in the recursive maze generation algorithm
![6](https://user-images.githubusercontent.com/68414803/183497049-1ac71e56-abd7-4127-8f82-153098f7ffca.png)

### A* in the predefined maze
![7](https://user-images.githubusercontent.com/68414803/183498994-bf6461c1-5568-4956-8c0d-3b79ff6cdb99.png)

## Results and Observations

All the algorithms are run in all three different situations. Given that the maze 
generation will give out a different maze each time its run, we can’t use it to compare 
the performance. So, using predefined maze and making our own, the observations 
were made.

DFS will miss the node even if it is adjacent to the start node. Given the nature 
of the algorithm, it will find longer path if it doesn’t hit the end node on time.

![8](https://user-images.githubusercontent.com/68414803/183497056-1c8afe77-cc07-4f93-a66a-c948a84e7ee7.png)

BFS is in general a better algorithm as it will traverse in level order, unlike DFS, 
it won’t miss the node even if its adjacent to the Start node. To find the path but the 
algo will have to traverse through a large number of nodes to get to the end node, 
which is a disadvantage.

![9](https://user-images.githubusercontent.com/68414803/183499182-a58feb13-e7a4-4963-a875-a1de9b0342e8.png)

To counter this, we use A* algorithm. From the below figure, it is obvious that 
the number of nodes it needs to traverse through is a lot less compared to other BFS 
and DFS algorithms.

![10](https://user-images.githubusercontent.com/68414803/183497071-f8f1783a-1f6f-40c4-b07a-f7671887a868.png)

As A* uses a heuristic approach, it uses on an average fewer resource than BFS and 
DFS. Admissible heuristic guaranteed it will find the most optimal path.


