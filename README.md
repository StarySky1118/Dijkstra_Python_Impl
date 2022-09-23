## Dijkstra 算法

### 一、算法背景

解决带权有向图单源最短路径问题。特殊条件：权值不能为负。

>带权图：图的边带有权值。

###  二、算法思想

Dijkstra 算法基于贪心算法，每次迭代都会获得一个局部最优解，并且这个局部最优解将作为全局最优解的一部分。

贪心算法具体到本算法中：如果源点到达**某个结点**的**最短路径**找到了，那么如果到达**另一个结点**也需要经过该结点，到达该结点的最短路径将作为到达另一结点最短路径的一部分。

### 三、算法描述

记图为 G = <V, E>。

使用集合 S 保存已经找到最短路径的结点，显然，初始情况下，集合 S 中只包含源点 s，即 S = {s}。

使用 dist[] 向量保存算法进行过程中源点 s 到每个结点的最短路径距离，显然，初始情况下，只有源点 s 直达的结点才有合法值。

遍历集合 V - S 中的结点（即未找到最短路径的结点）,记为 i：

​		遍历图中其他所有结点，记为 j：如果出现 G.arcs[i] [j] + dist[i] < dist[j]，则更新 dist[j]。即：如果以 i 为中间结点，到达 j 路径更      		短，则更新到达 j 的最短路径。

​		将 i 添加到 S 中。

当 S = V 时，算法结束。

### 四、算法的具体实现

#### 1、图的存储结构

使用邻接矩阵存储图。结构体内包括结点个数、顶点集、边集和不可到达距离。

```python
class MGraph:
    vex_num = 0  # 结点个数
    nodes = []  # 顶点集
    edges = []  # 边集
    infinity = 1000  # 不可到达距离
```

#### 2、测试用案例的加载

```python
    def load_example(self):
        self.edges[0][1] = 1
        self.edges[0][3] = 4
        self.edges[0][2] = 2
        self.edges[1][3] = 2
        self.edges[2][4] = 1
        self.edges[3][4] = 2
```

案例即为下图。

![图](Z:\研究生学习\算法研究\图.png)

#### 3、Dijkstra 算法具体代码

##### (1) 辅助数据结构

向量  `final[]` 指示结点是否已经找到最短路径。如：`final[1] = True` 表示已经找到到达结点 1 的最短路径。

距离向量 `dist[]` 表示源点到各个结点的最短路径。如：`dist[1] = 1` 表示源点到 1 的最短距离为 1。

路径矩阵 `path[v][w]` 表示源点到结点 v 是否经过结点 w。如：`path[1][2]` 表示源点到结点 1 经过结点 2。

辅助数据结构定义如下：

```python
final = [True]  # 已经考虑源点作为中间结点
dist = [self.infinity]  # 距离向量
path = []  # 路径矩阵
```

辅助数据结构初始化如下：

```python
# 初始化路径矩阵
for i in range(self.vex_num):
	temp = []
	for j in range(self.vex_num):
		temp.append(False)
	path.append(temp)

# 初始化 final 、距离向量和路径矩阵
for i in range(1, self.vex_num):
	distance = self.edges[0][i]
	if distance != self.infinity:  # 可以直达
		path[i][i] = True
	final.append(False)
	dist.append(distance)  # 距离为直达距离
```

##### (2) 更新距离向量

可以想象为，将每个结点作为中间结点进行探测：遍历距离向量找到最短距离和中间结点 `min_path_vex` ，使用该中间结点更新距离向量。代码如下：

```python
for i in range(1, self.vex_num):  # 最多需要考虑 vex_num-1 次新加入结点
	min_distance = self.infinity
    min_path_vex = 0
    
    # 找出最短距离另一端的结点下标
    for j in range(1, self.vex_num):
    	if dist[j] < min_distance and not final[j]:  # 最小且未找到最短路径
        	min_distance = dist[j]
            min_path_vex = j

	# 该结点找到了最短距离
    final[min_path_vex] = True

    # 更新距离向量
    for j in range(1, self.vex_num):
        if dist[min_path_vex] + self.edges[min_path_vex][j] < dist[j]:  # 将 min_path_vex 作为中间结点距离更短
            dist[j] = dist[min_path_vex] + self.edges[min_path_vex][j]
            path[j] = path[min_path_vex]  # 复制源点到达 min_path_vex 的路径
            path[j][min_path_vex] = True  # 到达结点 j 需要经过结点 min_path_vex
```

### 五、代码的时间复杂度分析

#### 1、空间复杂度

使用路径矩阵 `path[][]` 进行辅助，因此空间复杂度为 O(n^2^)。

#### 2、时间复杂度

使用循环嵌套，时间复杂度为 O(n^2^)。
