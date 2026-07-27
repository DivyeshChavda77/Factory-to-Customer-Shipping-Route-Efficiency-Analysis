from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation

if __name__ == "__main__":

    # Data Ingestion
    ingestion = DataIngestion()
    raw_path = ingestion.initiate_data_ingestion()

    print(f"Raw Data Path : {raw_path}")

    # Data Transformation
    transformation = DataTransformation()
    processed_path = transformation.initiate_data_transformation(raw_path)

    print(f"Processed Data Path : {processed_path}")