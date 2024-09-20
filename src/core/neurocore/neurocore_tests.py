import unittest
import numpy as np
from neurocore import NeuroCore
from neurocore import NeuroCoreConfig
from neurocore import AdvancedFeatureExtractor
from neurocore import CustomFeatureExtractor
from neurocore import DataPreprocessor
from neurocore import ModelEvaluator

class TestNeuroCore(unittest.TestCase):
    def test_init(self):
        config = NeuroCore Config(num_nodes=10, num_layers=2, learning_rate=0.01, batch_size=32, advanced_features=["correlation"], custom_features=["custom_feature_1"], hyperparameters={"hidden_layer_sizes": [(10, 10), (20, 20)]})
        neuro_core = NeuroCore(config)
        self.assertIsInstance(neuro_core, NeuroCore)

    def test_train(self):
        config = NeuroCoreConfig(num_nodes=10, num_layers=2, learning_rate=0.01, batch_size=32, advanced_features=["correlation"], custom_features=["custom_feature_1"], hyperparameters={"hidden_layer_sizes": [(10, 10), (20, 20)]})
        neuro_core = NeuroCore(config)
        X = np.random.rand(100, 10)
        y = np.random.rand(100, 1)
        neuro_core.train(X, y)
        self.assertTrue(True)

    def test_predict(self):
        config = NeuroCoreConfig(num_nodes=10, num_layers=2, learning_rate=0.01, batch_size=32, advanced_features=["correlation"], custom_features=["custom_feature_1"], hyperparameters={"hidden_layer_sizes": [(10, 10), (20, 20)]})
        neuro_core = NeuroCore(config)
        X = np.random.rand(100, 10)
        y_pred = neuro_core.predict(X)
        self.assertIsInstance(y_pred, np.ndarray)

    def test_evaluate(self):
        config = NeuroCoreConfig(num_nodes=10, num_layers=2, learning_rate=0.01, batch_size=32, advanced_features=["correlation"], custom_features=["custom_feature_1"], hyperparameters={"hidden_layer_sizes": [(10, 10), (20, 20)]})
        neuro_core = NeuroCore(config)
        X = np.random.rand(100, 10)
        y = np.random.rand(100, 1)
        accuracy, precision, recall, f1 = neuro_core.evaluate(X, y)
        self.assertIsInstance(accuracy, float)
        self.assertIsInstance(precision, float)
        self.assertIsInstance(recall, float)
        self.assertIsInstance(f1, float)

if __name__ == "__main__":
    unittest.main()
