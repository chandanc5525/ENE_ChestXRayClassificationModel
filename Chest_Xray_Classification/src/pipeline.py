from src.data.data_ingestion import DataIngestion
from src.data.data_preprocessing import DataPreprocessor
from src.training.trainer import Trainer
from src.evaluation.evaluator import Evaluator
from src.utils.logger import setup_logger

logger = setup_logger("pipeline", "logs/pipeline.log")

def run_pipeline():
    logger.info("Pipeline started...")

    # Step 1: Data Ingestion
    ingestion = DataIngestion()
    ingestion.run()

    # Step 2: Preprocessing
    preprocessor = DataPreprocessor()
    train_gen, val_gen, test_gen = preprocessor.create_generators()

    # Step 3: Training
    trainer = Trainer()
    model, history = trainer.train(train_gen, val_gen)

    # Step 4: Evaluation
    evaluator = Evaluator(model)
    report, matrix = evaluator.evaluate(test_gen)

    print("\nClassification Report:\n", report)
    print("\nConfusion Matrix:\n", matrix)

    logger.info("Pipeline completed successfully.")

if __name__ == "__main__":
    run_pipeline()
