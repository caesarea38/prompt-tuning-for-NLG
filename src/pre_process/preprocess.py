from datasets import load_dataset, Dataset


def serialize_dataset(dataset: Dataset):
    return dataset.flatten()


def pre_process_dataset(path: str, name: str = None, split_names=("train", "validation", "test")):
    dataset_union = load_dataset(path, name)
    container = DatasetContainer(dataset_union, split_names)
    return container


class DatasetContainer:

    def __init__(self, dataset, split_names):
        if split_names[0] in dataset:
            self.train_data = dataset[split_names[0]]
        else:
            self.train_data = None

        if split_names[1] in dataset:
            self.validation_data = dataset[split_names[1]]
        else:
            self.validation_data = None

        if split_names[2] in dataset:
            self.test_data = dataset[split_names[2]]
        else:
            self.test_data = None

    def get_train_data(self):
        return self.train_data.data

    def get_validation_data(self):
        return self.validation_data

    def get_test_data(self):
        return self.test_data
