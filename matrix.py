def matrix_is(matrix, n: int, m: int):#格式判断
    if(len(matrix) != n):
        return False
    for i in range(n):
        if(len(matrix[i]) != m):
            return False
        for j in range(len(matrix[i])):
             if(type(matrix[i][j]) != int):
                 return False
    return True

class Matrix(object):# 矩阵类
    
    def __init__(self, n: int, m: int, matrix = None):#n行m列
        if(matrix):
            if(matrix_is(matrix, n, m)):
                self.n = n
                self.m = m
                self.matrix = matrix
                return
        self.n = n
        self.m = m
        self.matrix = [[0 for i in range(m)] for j in range(n)]#不传入默认为0


    def get_size(self):
        return self.n, self.m
    

    def add(self, other: "Matrix"):#加法
        if(self.get_size() != other.get_size()):
            print("矩阵大小不匹配")
            return
        new = Matrix(self.n,self.m)
        for i in range(self.n):
            for j in range(self.m):
                new.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return new
    

    def sub(self, other:"Matrix"):#减法
        if(self.get_size() != other.get_size()):
            print("矩阵大小不匹配")
            return
        new = Matrix(self.n,self.m)
        for i in range(self.n):
            for j in range(self.m):
                new.matrix[i][j] = self.matrix[i][j] - other.matrix[i][j]
        return new
    

    def mul(self, other: int):#数乘
        new = Matrix(self.n,self.m)
        for i in range(self.n):
            for j in range(self.m):
                new.matrix[i][j] = self.matrix[i][j] * other 
        return new
    
    
    def dot(self, other: "Matrix"):#乘法
        if(self.m != other.n):
            print("矩阵大小不匹配")
            return
        new = Matrix(self.n,other.m)
        for i in range(self.n):
            for j in range(other.m):
                sum = 0
                for k in range(self.m):
                    sum += self.matrix[i][k] * other.matrix[k][j]
                new.matrix[i][j] = sum
        return new
    

    def trun(self):#转置
        new = Matrix(self.m,self.n)
        for i in range(self.n):
            for j in range(self.m):
                new.matrix[j][i] = self.matrix[i][j]
        return new


    def inv(self):#逆
        if(self.n != self.m):
            print("矩阵不可逆")
            return
        new = Matrix(self.n,self.m)
        for i in range(self.n):#生成单位阵
            new.matrix[i][i] = 1
        for i in range(self.n):#高斯消元
            k = i
            for j in range(i + 1,self.n):#找到每一列绝对值最大的那一行（为了防止是0）
                if(abs(self.matrix[j][i]) > abs(self.matrix[k][i])):
                    k = j
            self.matrix[i], self.matrix[k] = self.matrix[k], self.matrix[i]#行交换
            new.matrix[i], new.matrix[k] = new.matrix[k], new.matrix[i]
            if(self.matrix[i][i] == 0):#不满秩则不可逆（维度退化了）
                print("矩阵不可逆")
                return
            for j in range(self.n):#每行都减一遍
                if(j != i):
                    temp = self.matrix[j][i] / self.matrix[i][i]
                    for t in range(self.n):
                        self.matrix[j][t] -= self.matrix[i][t] * temp
                        new.matrix[j][t] -= new.matrix[i][t] * temp
        for i in range(self.n):
            for j in range(self.n):
                new.matrix[i][j] = new.matrix[i][j] / self.matrix[i][i]
        return new


    def rank(self):#秩
        if(self.n>self.m):
            self = self.trun()
        row = 0
        for i in range(self.n):
            k = row
            for j in range(row + 1,self.n):
                if(abs(self.matrix[j][i]) > abs(self.matrix[k][i])):
                    k = j
            self.matrix[row], self.matrix[k] = self.matrix[k], self.matrix[row]
            if(self.matrix[row][i] == 0):
                continue
            else:
                for j in range(row + 1,self.n):
                    temp = self.matrix[j][i] / self.matrix[row][i]
                    for t in range(i,self.n):
                        self.matrix[j][t] -= self.matrix[row][t] * temp
                row += 1
                if(row == self.n):
                    return row
        return row


    def print_m(self):#打印矩阵
        for i in range(self.n):
            print(self.matrix[i])


mat = Matrix(3,2,[[1,2],[3,4],[2,4]])#请输入一个矩阵
mat.print_m()
print(mat.rank())
tam = mat.trun()
tam.print_m()
print(tam.rank())