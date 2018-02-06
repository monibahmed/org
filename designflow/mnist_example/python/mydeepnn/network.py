class Network():
    '''sizes: contains the number of neurons in respective layers

    example : net = Network([2,3,1])
    gives 2 neurons in first layer, 3 in teh next and 1 in the last layer

    The network then initializes the biases and weights to be random.

    '''

    def __init__(self, sizes):
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x)
                        for x, y in zip(sizes[:-1], sizes[1:])]


def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))
