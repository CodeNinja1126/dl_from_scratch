# 퍼셉트론

## 퍼셉트론이란 무엇인가?
- 퍼셉트론은 다수의 신호를 입력으로 받아 하나의 신호를 출력한다.
<image src='images/1.png' width='300' height='300'>
  
그림의 원은 노드 혹은 뉴런이라 부른다.

여기서 n개의 w들을 **가중치**라 부르고, b는 **편향**이라 부른다.

## 논리 회로

퍼셉트론으로 다음과 같이 논리 게이트를 구현할 수 있다.

```python3
def AND(x1, x2):
    w = np.array([0.5, 0.5])
    x = np.array([x1, x2])
    b = -0.7

    x = w * x
    if x.sum() + b > 0:
        return 1
    else:
        return 0

def NAND(x1, x2):
    w = np.array([-0.5, -0.5])
    x = np.array([x1, x2])
    b = 0.7

    x = w * x
    if x.sum() + b > 0:
        return 1
    else:
        return 0

def OR(x1, x2):
    w = np.array([0.5, 0.5])
    x = np.array([x1, x2])
    b = -0.3

    x = w * x
    if x.sum() + b > 0:
        return 1
    else:
        return 0
```
각 게이트들을 w와 b 값을 적절히 조절해 주는 것만으로도 구현할 수 있다.

하지만 XOR 게이트의 경우를 생각해 보자.

<image src='images/2.png' width='200' height='200'>

이와 같이 되므로 기존의 방식으로는 구현할 수 없다.

그래서 퍼셉트론을 쌓아 다층 퍼셉트론으로 만들면 XOR 게이트를 구현할 수 있다.

<image src='images/3.jpg' width='400' height='200'>

코드는 다음과 같다.

```python3
def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    return AND(s1, s2)
```

이렇게 퍼셉트론을 쌓으면 비선형 영역을 포함할 수 있으며

퍼셉트론을 통해 다양하고 복잡한 입출력을 해낼 수 있다.
