# -*- coding: utf-8 -*-
"""2_1_pytorch_custom_function.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bLtiX4H4SMTgSNrg1yHwFEkF_TvF87B0
"""

# 새 노트 > 런타임 : GPU 지정
# 세션 새로 시작시(로그아웃 > 로그인), pytorch 새로 설치
!pip3 install torch
!pip3 install torchvision

import torch
import torch.nn as nn
from torch.autograd import Variable, Function

# torch.autograd.Function 클래스가 제공하는 함수 목록 확인
for i in Function.__dict__:
  print(i) # Function.__dict__[i]번째 정보가 출력된다.

# 사용자 정의 클래스 작성 & 메소드 만들기
class Exp(Function):
  @staticmethod
  def forward(ctx, i):
    result = i.exp()
    ctx.save_for_backward(result)
    return result

  @staticmethod
  def backward(ctx, grad_output):
    result, = ctx.saved_variables
    return grad_output * result
# ------------------------------------------------------------

layer = Exp().apply
print(layer)

a = Variable(torch.Tensor([1,2]), requires_grad=True)
output = layer(a)
print(output)

result = torch.sum(output)
print(result)

print(a.grad)
result.backward()
print(a.grad)