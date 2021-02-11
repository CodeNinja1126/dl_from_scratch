import numpy as np
import sigmoid

def identity_function(x):
    return x

def softmax_function(x):
    """AI is creating summary for softmax_function

    Args:
        x (np.ndarray): data

    Returns:
        (np.ndarray): softmax value
    """
    exp_x = np.exp(x - x.max())
    exp_sum = exp_x.sum()
    return exp_x / exp_sum
 

def init_network():
    """AI is creating summary for init_network

    Returns:
        dict : neural network
    """
    network = {}
    network['W1'] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    network['b1'] = np.array([0.1, 0.2, 0.3])
    network['W2'] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    network['b2'] = np.array([0.1, 0.2])
    network['W3'] = np.array([[0.1, 0.3], [0.2, 0.4]])
    network['b3'] = np.array([0.1, 0.2])

    return network

def forward(network, x, out_func=softmax_function):
    """AI is creating summary for forward

    Args:
        network (dict): neural network
        x (np.ndarray): data
        out_func (function): output_function

    Returns:
        y (.ndarray): output
    """
    a1 = np.dot(x, network['W1']) + network['b1']
    z1 = sigmoid.sigmoid(a1)

    a2 = np.dot(z1, network['W2']) + network['b2']
    z2 = sigmoid.sigmoid(a2)

    a3 = np.dot(z2 , network['W3']) + network['b3']
    y = out_func(a3)

    return y


if __name__ == '__main__':
    network = init_network()
    x = np.array([1.0, 0.5])
    y = forward(network, x, identity_function)
    print(y)