import pytest

from trabalho2.dataset import Dataset, join_datasets


def test_features(example):
    instances = example['dataset']
    dataset = Dataset(instances)
    assert dataset.features.tolist() == [i[0] for i in instances]


def test_expectations(example):
    instances = example['dataset']
    dataset = Dataset(instances)
    assert dataset.expectations.tolist() == [i[1] for i in instances]


def test_normalize():
    features = [
        [0.0, -1.0],
        [1.0,  1.0],
        [4.0,  0.0],
    ]
    normalized_features = [
        [0.00, 0.0],
        [0.25, 1.0],
        [1.00, 0.5],
    ]
    instances = [(xs, [0.]) for xs in features]
    dataset = Dataset(instances, normalize=True)
    assert dataset.features.tolist() == normalized_features


def test_random_folds():
    dataset = Dataset([
        ([0.], [1., 0.]),
        ([1.], [1., 0.]),
        ([2.], [1., 0.]),
        ([3.], [1., 0.]),
        ([4.], [0., 1.]),
        ([5.], [0., 1.]),
        ([6.], [0., 1.]),
        ([7.], [0., 1.]),
    ])
    folds = dataset.random_folds(4)

    assert len(folds) == 4
    for fold in folds:
        assert isinstance(fold, Dataset)
        assert len(fold) == 2

        # cada fold deve ter uma instância de cada classe
        assert fold.expectations[0].tolist() != fold.expectations[1].tolist()


def test_join_datasets():
    d1 = Dataset([
        ([0.], [0.]),
        ([1.], [1.]),
    ])
    d2 = Dataset([
        ([2.], [2.]),
        ([3.], [3.]),
    ])
    combined = join_datasets([d1, d2])

    assert combined.features.tolist() == [[0.], [1.], [2.], [3.]]
    assert combined.expectations.tolist() == [[0.], [1.], [2.], [3.]]
