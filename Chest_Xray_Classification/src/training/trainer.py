import yaml
from src.utils.logger import setup_logger
from src.models.cnn_model import build_cnn_model

logger = setup_logger("trainer", "logs/trainer.log")

class Trainer:
    def __init__(self, config_path="config/config.yaml"):
        with open(config_path, "r") as f:
            self.config = yaml.safe_load(f)

        self.epochs = self.config["model"]["epochs"]
        self.lr = self.config["model"]["learning_rate"]
        self.dropout = self.config["model"]["dropout"]
        self.model = None

    def train(self, train_gen, val_gen):
        logger.info("Initializing CNN model training...")
        self.model = build_cnn_model(
            input_shape=(180, 180, 1),
            dropout=self.dropout,
            lr=self.lr
        )

        history = self.model.fit(
            train_gen,
            epochs=self.epochs,
            validation_data=val_gen
        )

        logger.info("Training completed successfully.")
        return self.model, history
