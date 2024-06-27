# Graph
Non-linear data structure

Nodes and edges - no rules


## Types of “graphs”
### Undirected graphs
> Facebook Network | G = {V, E}
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/290ca436-9b2c-4597-b44e-0ed37f7297ca" width="460">

### Directed graphs
> Google Webs | G = (V, E)
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/9071661c-7c2d-484d-bff0-97df650912e0" width="460">

### Weighted graphs
> Road map network (weight = distances)
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/32e6a102-1577-493c-9035-88829b986e3e" width="460">


## Properties of Graph
<img src="https://github.com/MaryamZahiri/LC-Algorithms/assets/52676399/289568f3-0c49-4315-8124-c69c0952a3cf" width="460">


## Graph implementation/representation
1. Edge List
> Edge -> [node, neighber]

```python
edges = [[0,1],[1,2],[2,0]]
```

2. Adjancy Matrix
3. Adjancy List
> index -> [neighbor 1, neighbor 2]

```python 
adjacency_list = [[1,2], [0,2], [0,1]]
```


## Graph Algorithm
### 1. [Traversing all Vertices](https://github.com/MaryamZahiri/LC-Algorithms/blob/master/Data_Structure/graph/Examples/Example%201%20-%20DFS%20vs%20BFS%20-%20Traversing%20all%20Vertices%20Example%201.md)

### 2. [Traversing all paths between two vertices vs Shortest Path Between Two Vertices](https://github.com/MaryamZahiri/LC-Algorithms/blob/master/Data_Structure/graph/Examples/Example%202%20-%20DFS%20vs%20BFS%20-%20Traversing%20all%20paths%20between%20two%20vertices.md)


## Sources
[Explore Graph from Leedcode](https://leetcode.com/explore/learn/card/graph/)

[Data Structure](https://www.youtube.com/watch?v=ZdY1Fp9dKzs&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P&index=40)

[Neetcode](https://www.youtube.com/@NeetCode)

[Lintcode](https://www.lintcode.com/)