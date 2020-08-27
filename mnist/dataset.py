from ml.colearn.mnist.data import split_to_folders, prepare_single_client
from ml.colearn.mnist.config import load_config
from ml.colearn.plot import display_statistics, plot_results, plot_votes
from ml.colearn.model import KerasLearner


class Mnist:
    split_to_folders = split_to_folders
    prepare_single_client = prepare_single_client
    load_config = load_config
    display_statistics = display_statistics
    plot_results = plot_results
    plot_votes = plot_votes
    Model = KerasLearner