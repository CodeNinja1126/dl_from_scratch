# 신경망 학습하기
## 데이터에서 학습한다.
신경망의 특징은 데이터에서 학습한다는 것이다.

신경망의 파라미터들은 그 수가 너무 많아 사람이 하나 하나 설정할 수 있는 수준이 아니다.

기계학습에서는 문제 데이터를 **훈련 데이터**와 **시험 데이터**로 나눠 학습과 실험을 수행한다.

이는 모델의 **범용 능력**을 제대로 평가하기 위함이다.

지나치게 하나의 데이터셋에 최적화된 형태를 **오버피팅**이라고 한다.

## 손실 함수
신경망이 학습할 때 하나의 지표를 기준으로 매개 변수를 탐색한다.

이 지표를 **손실 함수**라고한다.

일반적으로는 오차 제곱합과 교차 엔트로피 오차를 사용한다.

### 오차 제곱합

![](https://cdn.corporatefinanceinstitute.com/assets/sum-of-squares3-300x120.png)
  
### 교차 엔트로피

![2](https://user-images.githubusercontent.com/56903243/116270163-d2103d00-a7b9-11eb-844f-c6a551e7e2d8.png)
  
### 미니 배치 학습
모든 데이터셋에 대해 하나하나 손실 함수를 구해 평균을 하는 것은 효율적이지 않다.

그래서 데이터 몇 개를 골라 손실 함수를 구하고 학습을 수행 한다.

이를 **미니배치 학습**이라고 한다.

### 왜 손실함수를 설정하는가?
정확도라는 지표를 두고 왜 손실 함수라는 지표를 사용할까?

그 이유는 정확도는 미분 가능한 함수가 아니기 때문이다.

딥러닝에서는 미분을 통해 학습을 수행하는데 그러지 못하면 학습을 제대로 수행할 수가 없다.

그렇기 때문에 미분 가능한 지표인 손실 함수를 설정해 학습을 수행하는 것이다.

## 수치 미분
경사법에서는 기울기 값을 기준으로 나아갈 방향을 정한다.

### 미분
미분 수식은 다음과 같다.

![](https://wikimedia.org/api/rest_v1/media/math/render/svg/88349812ad8e22727ed7e2f3280a5b6b8e970ef6)

따라서 x값을 한없이 작은 값으로 설정하면 미분값에 근사한 값을 얻을 수 있다.

이를 **수치 미분**이라고 한다.

보통은 다음과 같은 중앙 차분을 이용해 미분 값을 계산한다.

### 편미분
다음과 같은 다변수 함수를 생각해보자.

![](https://wikimedia.org/api/rest_v1/media/math/render/svg/028579be25b95d7ea02beb6d3e0cec42ea600358)

이 경우에는 미분을 할 때 어떤 변수에 대한 미분인지를 구별해야 한다.

그래서 변수가 여럿인 함수에 대한 미분을 **편미분**이라 한다.

![](https://wikimedia.org/api/rest_v1/media/math/render/svg/592f7c49852acb0db33f15b42b050e4415749e62)

## 그래디언트
모든 변수의 편미분을 벡터로 정의한 것을 **그래디언트**라고 한다.

그래디언트는 현재 위치에서 가장 낮은 곳을 가르킨다.

### 경사하강법
변수에 그래디언트를 빼면 점점 최소위치로 이동하게 된다.

이를 **경사하강법**이라 한다.

![](https://wikimedia.org/api/rest_v1/media/math/render/svg/dda3670f8a8996a0d3bf80856bb4a166cc8db6d4)

이때 적절한 **학습률**값을 줘 학습이 얼마나 수행될지를 결정해 준다.

학습률 값이 너무 크면 최소점을 지나칠 수 있고 너무 작으면 학습이 더디게 된다.

학습률 같이 학습을 통해 학습되지 않고 개발자가 미리 지정해 주어야 하는 파라미터를 **하이퍼 파라미터**라고 한다.

대부분의 경우 데이터를 무작위로 배치로 골라 학습을 시킨다.

하나만 무작위로 고를 경우 **확률적 경사하강법(Stochastic Gradient Descent, SGD)**,

무작위로 배치를 고를 경우 **미니배치 경사하강법(Mini-batch Gradient Descent, MGD)** 라고 한다.

