from pathlib import Path
import pandas as pd
import typer
from loguru import logger
from datetime import datetime
from livestock_project.config import PROCESSED_DATA_DIR, RAW_DATA_DIR

# Define the Typer app for the CLI
app = typer.Typer()

# Reusable functions for data loading, processing, and saving

def load_data(file_name: str) -> pd.DataFrame:
    """Load Excel data from the raw data folder."""
    input_path = RAW_DATA_DIR / file_name
    if not input_path.is_file():
        logger.error(f"File {file_name} not found in RAW_DATA_DIR.")
        raise FileNotFoundError(f"File {file_name} not found.")
    
    logger.info(f"Loading data from {input_path}")
    df = pd.read_excel(input_path)
    return df

def process_data(df: pd.DataFrame) -> pd.DataFrame:
    """Process the dataset (example: drop missing values)."""
    logger.info("Processing data...")
    df = df.dropna(axis=1, how='all')
    logger.info("Data processing complete.")
    return df

def save_data(df: pd.DataFrame, output_path: Path) -> None:
    """Save the processed data to the specified output path."""
    output_path = Path(output_path)  # Convert to Path if it's a string
    output_path.parent.mkdir(parents=True, exist_ok=True)  # Make sure parent directories exist
    df.to_excel(output_path, index=False)  # Save the DataFrame to Excel
    logger.success(f"Processed data saved to {output_path}")

def process_file(file_name: str, output_path: Path = None) -> Path:
    """Load, process, and save the data from an Excel file."""
    # Load data
    df = load_data(file_name)
    
    # Process data (e.g., drop missing values)
    df_processed = process_data(df)
    
    # Default output path: Ensure it is in the `processed` folder inside the `data` directory
    if not output_path:
        output_path = PROCESSED_DATA_DIR / file_name  # Use the same filename, save in `processed`
    else:
        output_path = Path(output_path)  # Convert to Path if it's passed as string
    
    # Ensure the output path is inside the `processed` directory
    if output_path.parent != PROCESSED_DATA_DIR:
        output_path = PROCESSED_DATA_DIR / output_path.name  # Use filename and ensure it's inside the processed folder
    
    # Save processed data to the output path
    save_data(df_processed, output_path)
    
    return output_path


# The main function that will run when the script is executed from the command line
@app.command()
def main(
    file_name: str = typer.Argument(..., help="Name of the input Excel file to process."),
    output_path: Path = typer.Option(None, help="Path to save the processed file. Defaults to processed folder."),
):
    """Command-line interface for processing the dataset."""
    # Process the file and save it
    output_file = process_file(file_name, output_path)
    logger.success(f"Processed file saved to: {output_file}")

# If this script is being run directly, the CLI is executed
if __name__ == "__main__":
    app()