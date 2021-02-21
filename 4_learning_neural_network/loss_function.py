import numpy as np

def sum_square_error(y, t):
    return 0.5 * np.sum((y-t)**2)


def cross_entropy_error(y, t, one_hot=True):
    delta = 1e-7  # log 0이 나오지 않도록 미세한 값을 더해줌
    if y.ndim == 1:
        return -np.sum(t*np.log(y + delta))

    batch_size = y.shape[0]
    if one_hot:
        return -np.sum(t*np.log(y + delta)) / batch_size
    else:
        return -np.sum(np.log(y[np.arange(batch_size), t] + delta)) / batch_size


if __name__ == '__main__':
    y = np.array([[0, 0.1, 0.2, 0.7],[0, 0.3, 0.2, 0.5]])
    t = np.array([[0, 0, 0, 1],[0, 0, 0, ]])

    print(sum_square_error(y, t))
    print(cross_entropy_error(y, t))