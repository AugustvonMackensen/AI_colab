# -*- coding: utf-8 -*-
"""1_2_pytorch_basic.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cDLf7pppaMVrXbGf-3a1UlWFl3Ke6_tv

# **PyTorch Tensor Basic Usage**
- Create Tensor
- Indexing, Joining, Slicing
- Initialization
- Math Operations

# **1. Create Tensor**
1) random numbers
"""

# 새 노트에서 런타임 > GPU 로 다시 지정함
import torch

# torch.rand(sizes) --> 0에서 1 사이의 실수값을 랜덤하게 발생함
# sizes : 1차원 개수 or 2차원 행렬 갯수 등으로 지정
# 0과 1 사이의 실수형 숫자를 균등하게 생성
x = torch.rand(2, 3)
x

# torch.randn(sizes) --> Z(0, 1)
# 평균이 0이고, 표준편차가 1인 가우시안 정규분포를 이용해서 생성
x = torch.randn(2, 3)
x

# torch.randperm(n) --> permutation of 0 ~ n
x = torch.randperm(5)
x

"""**랜덤한 값을 가지는 텐서 생성시키는 함수들**
1. torch.rand() : 0과 1사이의 숫자를 균등하게 생성
2. torch.rand_like() : 사이즈를 튜플로 입력하지 않고, 기존의 텐서와 같은 구조를 만들때 사용
3. torch.randn() : 평균이 0이고 표준편차가 1인 가우시안 정규분포를 이용해 값 생성
4. torch.randn_like() : 사이즈를 튜플로 지정하지 않고 기존의 텐서를 이용
5. torch.randint() : 주어진 범위 내의 정수를 균등하게 생성. 자료형은 torch.float32
6. torch.randint_like()
7. torch.randperm() : 주어진 범위 내의 정수를 랜덤하게 생성

# **2) zeros, ones, arange**
"""

# torch.zeros(2, 3) --> [[0,0,0], [0,0,0]]
x = torch.zeros(2, 3)
x

# torch.ones(2, 3) --> [[1,1,1], [1,1,1]]
x = torch.ones(2, 3)
x

# torch.arange(start, end, strp=1)
x = torch.arange(0, 3, step=0.5)
x

"""# **3) Tensor Data Type**"""

# torch.FloatTensor(size | list)
x = torch.FloatTensor(2, 3)
x

x = torch.FloatTensor([12, 35])
x

# tensor.type_as(tensor_type)
# 기존 텐서의 값의 자료형을 바꿀 때 사용
x = x.type_as(torch.IntTensor())
x

"""# **4) Numpy to Tensor, Tensor to Numpy**"""

import numpy as np

# torch.from_numpy(ndarray) --> tensor
x1 = np.ndarray(shape=(2, 3), dtype=int, buffer=np.array([1,2,3,4,5,6]))
x1
x2 = torch.from_numpy(x1)
x2

# torch.numpy() --> ndarray
x3 = x2.numpy()
x3

"""# **5) Tensor on CPU & GPU**"""

x = torch.FloatTensor(([1,2,3],[4,5,6]))
x
x_gpu = x.cuda()
x_gpu

x_cpu = x_gpu.cpu()
x_cpu

"""6) Tensor Size"""

# tensor객체.size() --> 인덱스값
x = torch.FloatTensor(10, 12, 3, 3) # start, end-1, row, col
x
x.size() # torch.size([10, 12, 3, 3])
x.size()[:] # torch.size([10, 12, 3, 3])

"""# **2. Indexing, Slicing, Joining**
**1) Indexing**
"""

# torch.index_select(input, dim, index)
# dim == 행값, index == 열에 대한 인덱싱
x = torch.rand(4, 3)
out = torch.index_select(x, 0, torch.LongTensor([0, 3]))

x, out

# python indexing 사용 가능
x[:, 0] # 모든 행의 0열 값들
x[0, :] # 0행의 모든값들
x[0:2, 0:2] # 0~1행, 0~1열까지의 값들

# torch.masked_select(input, mask)
x = torch.randn(2, 3)
x
mask = torch.ByteTensor([[0, 0, 1], [0, 1, 0]])
out = torch.masked_select(x, mask)
x, mask, out

"""**2) Joining**"""

# torch.cat(seq, dim=0)

x = torch.FloatTensor([[1,2,3],[4,5,6]])
y = torch.FloatTensor([[-1,-2,-3],[-4,-5,-6]])

z1 = torch.cat([x,y], dim=0) # dim=0, 아래에 합쳐짐
z2 = torch.cat([x,y], dim=1) # dim=1, 오른쪽에 합쳐짐

x, y, z1, z2 # z1, z2 확인해보려면 print로 보시오.

# torch.stack(sequence, dim=0) --> 새로운 차원으로 추가
x_stack = torch.stack([x, x, x, x], dim=0) # (4,2,3) 모양

x_stack

"""**3) Slicing**"""

# torch.chunk(tensor, chunks, dim=0)
x_1, x_2 = torch.chunk(z1, 2, dim=0) # dim 이 0이면 행을 2개로 분할
y_1, y_2, y_3 = torch.chunk(z1, 3, dim=1) #dim 이 1이면 열을 3개로 분할

z1, x_1, x_2, y_1, y_2, y_3

# torch.split(tensor, split_size, dim=0)
x1, x2 = torch.split(z1, 2, dim=0)
_, y1 = torch.split(z1, 2, dim=1) # 3개 열을 2개로 분할

z1, x1, x2, y1

"""**4) Squeezing**"""

# torch.squeeze(input, dim=None) --> 숫자가 1인 차원을 제거
x1 = torch.FloatTensor(10, 1, 3, 14)
# 차원(dimension)의 개념
# 10 : batch size (데이터 한 묶음당 들어있는 데이터(x,y)쌍 갯수)
# 1 : channel size
# 3 : width image size
# 14 : height image size

x2 = torch.squeeze(x1)

x1.size(), x2.size()

# torch.unsqueeze(input, dim=None) --> 숫자가 1인 차원을 추가
x1 = torch.FloatTensor(10, 3, 4)
x2 = torch.unsqueeze(x1, dim=0) # dim이 0이면, 첫번째 위치에 추가

x1.size(), x2.size()

"""# **3. Initialization**"""

import torch.nn.init as init

x1 = init.uniform(torch.FloatTensor(3, 4), a=0, b=9) # a에서 b까지의 값으로 초기화
x2 = init.normal(torch.FloatTensor(3, 4), std=0.2) # 표준편차 0.2를 적용 초기화
x3 = init.constant(torch.FloatTensor(3, 4), 3.145) # 지정된 상수 값으로 초기화

x1, x2, x3

"""# **4. Math Operations**

**1) arithmetic operations**
"""

# torch.add()
x1 = torch.FloatTensor([[1,2,3], [4,5,6]])
x2 = torch.FloatTensor([[1,2,3], [4,5,6]])
x_add = torch.add(x1, x2)
x1, x2, x_add, x1 + x2, x1 - x2

# torch.add() : broadcastion (숫자와의 연산)
x3 = torch.add(x1, 10)

x3, x1 + 10, x2 - 10

# torch.mul() 곱하기
x3 = torch.mul(x1, x2)

x3, x1 * x2

x3 = torch.mul(x1, 10)

x3, x1 * 10

# torch.div() 나누기한 몫
x3 = torch.div(x1, 5)

x1, x3, x1 / 5

"""**2) Other Math Operations**"""

# torch.pow(input, exponent)
x1 = torch.FloatTensor(3,4)

x1, torch.pow(x1, 2), x1 ** 2

# torch.exp(tensor, out=None) : exponential 연산
# y = e의 x제곱 구하기
x1 = torch.FloatTensor(3,4)
out = torch.exp(x1)

x1, out

# torch.log(input, out=None) : 자연로그
out = torch.log(x)
x1, out

"""**3) Matrix operations**"""

# torch.mm(mat1, mat2) -> Matrix multiplication (행렬곱)
x1 = torch.FloatTensor(3,4)
x2 = torch.FloatTensor(4,5)
out = torch.mm(x1, x2)
x1, x2, out

# torch.bmm(batch1, batch2) --> batch 행렬 연산
# 맨 앞의 batch는 차원을 유지하면서 뒤 요소들의 행렬곱 연산함
x1 = torch.FloatTensor(10, 3, 4)
x2 = torch.FloatTensor(10, 4, 5)
out = torch.bmm(x1, x2)
out.size()

# torch.dot(tensor1, tensor2) : 벡터의 내적을 구함
x1 = torch.FloatTensor([1,2,3,4])
x2 = torch.FloatTensor([2,3,4,5])

torch.dot(x1,x2)

# torch.t(matrix) : transposed matrix(텐서의 전치연산)
# 행과 열 서로 바꿈

x1 = torch.FloatTensor(3,4)

x1, x1.t()

# torch.transpose(input, dim_0, dim_1)
# 바꿀 차원을 2개 지정함
# 텐서의 내부 차원간 바꾸기
x1 = torch.FloatTensor(10, 3, 4)

# 1차원과 2차원을 서로 바꿈
x1.size(), torch.transpose(x1, 1, 2).size(), x1.transpose(1, 2).size()

# torch.eig(input, eigenvectors=False)
# 고유값(eigen_value), 고유벡터(eigen_vector) 반환
x1 = torch.FloatTensor(4,4)

x1, torch.eig(x1, True)