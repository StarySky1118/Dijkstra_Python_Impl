# -*- coding:utf-8 -*-
# 图的邻接矩阵存储结构
class MGraph:
    vex_num = 0  # 结点个数
    nodes = []  # 顶点集
    edges = []  # 边集
    infinity = 1000  # 不可到达距离

    # 构造方法
    def __init__(self, vex_num):
        self.vex_num = vex_num
        # 初始化顶点集
        for i in range(vex_num):
            self.nodes.append(i)
        # 初始化边集
        for i in range(vex_num):
            temp = []
            for j in range(vex_num):
                temp.append(self.infinity)
            self.edges.append(temp)

    # 格式化输出邻接矩阵
    def print_matrix(self):
        print("   ", end="")  # 格式化空格
        # 横向序号
        for i in range(self.vex_num):
            print("{}  ".format(i), end="")
        print()
        for i in range(self.vex_num):
            print("{} ".format(i), end="")
            print(self.edges[i])

    # 测试用，载入 5*5 案例矩阵
    def load_example(self):
        self.edges[0][1] = 1
        self.edges[0][3] = 4
        self.edges[0][2] = 2
        self.edges[1][3] = 2
        self.edges[2][4] = 1
        self.edges[3][4] = 2

    # 迪杰斯特拉算法
    def shortest_path_dij(self):
        final = [True]  # 已经考虑源点作为中间结点
        dist = [self.infinity]  # 距离向量
        path = []  # 路径矩阵

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
            dist.append(distance)

        for i in range(1, self.vex_num):  # 最多需要考虑 vex_num-1 次新加入结点
            min_distance = self.infinity
            min_path_vex = 0
            # 找出最短距离另一端的结点下标
            for j in range(1, self.vex_num):
                if dist[j] < min_distance and not final[j]:
                    min_distance = dist[j]
                    min_path_vex = j

            # 将该最短距离结点置为 True
            final[min_path_vex] = True

            # 更新距离向量
            for j in range(1, self.vex_num):
                if dist[min_path_vex] + self.edges[min_path_vex][j] < dist[j]:  # 将 min_path_vex 作为中间结点距离更短
                    dist[j] = dist[min_path_vex] + self.edges[min_path_vex][j]
                    path[j] = path[min_path_vex]
                    path[j][min_path_vex] = True

        return path










