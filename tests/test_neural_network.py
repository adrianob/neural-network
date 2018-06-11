import numpy as np
import pytest

from trabalho2.dataset import Dataset
from trabalho2.neural_network import NeuralNetwork


def test_lambda_(example):
    lambda_, structure = example['network']
    network = NeuralNetwork(lambda_, structure)
    assert network.lambda_ == lambda_


def test_structure(example):
    lambda_, structure = example['network']
    network = NeuralNetwork(lambda_, structure)
    assert list(network.structure) == structure


def test_set_weights(example):
    network = NeuralNetwork(*example['network'])
    network.set_weights(example['weights'])

    weights = [theta.tolist() for theta in network.weights]
    assert weights == example['weights']


def test_propagate(example):
    network = NeuralNetwork(*example['network'])
    network.set_weights(example['weights'])

    dataset = Dataset(example['dataset'])
    activations = network.propagate(dataset.features)

    activations = [np.round_(a, decimals=5) for a in activations]
    activations = [a.T.tolist() for a in activations]
    assert activations == example['activations']


def test_backpropagate(example):
    network = NeuralNetwork(*example['network'])
    network.set_weights(example['weights'])

    dataset = Dataset(example['dataset'])
    activations = network.propagate(dataset.features)
    gradients = network.backpropagate(dataset.expectations, activations)

    gradients = [np.round_(g, decimals=5) for g in gradients]
    gradients = [g.tolist() for g in gradients]
    assert gradients == example['gradients']


def test_total_error(example):
    network = NeuralNetwork(*example['network'])
    network.set_weights(example['weights'])

    dataset = Dataset(example['dataset'])
    activations = network.propagate(dataset.features)
    total_error = network.total_error(dataset.expectations, activations[-1])

    assert round(total_error, 5) == example['total_error']
