from sklearn.metrics import classification_report, confusion_matrix
import numpy as np
from src.utils.logger import setup_logger

logger = setup_logger("evaluator", "logs/evaluator.log")

class Evaluator:
    def __init__(self, model):
        self.model = model

    def evaluate(self, test_gen):
        logger.info("Evaluating model on test data...")
        predictions = self.model.predict(test_gen)
        preds = (predictions > 0.5).astype("int32")

        y_true = test_gen.classes
        report = classification_report(y_true, preds, target_names=list(test_gen.class_indices.keys()))
        matrix = confusion_matrix(y_true, preds)

        logger.info("Evaluation completed.")
        return report, matrix
