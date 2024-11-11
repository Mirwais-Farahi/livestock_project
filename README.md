# Livestock  Third Party Monitoring Service for Emergency & Resilience Project

This project is led by **Adroit Associates** as part of the Third Party Monitoring Service for Emergency \& Resilience Project. The Livestock UN-FAO project is designed to apply data science methodologies to analyze livestock-related data, providing valuable insights to the United Nations Food and Agriculture Organization (UN-FAO).

## Project Intro/Objective
The purpose of this project is to analyze livestock-related data in order to provide valuable insights for the United Nations Food and Agriculture Organization (UN-FAO). This project involves data cleaning, analysis, and reporting. The goal is to create actionable results for stakeholders by providing a better understanding of the current livestock situation in Afghanistan.

### Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         livestock_project and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── livestock_project   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes livestock_project a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    ├── modeling                
    │   ├── __init__.py 
    │   ├── predict.py          <- Code to run model inference with trained models          
    │   └── train.py            <- Code to train models
    │
    └── plots.py                <- Code to create visualizations
```

--------

### Partner
* **United Nations Food and Agriculture Organization (UN-FAO)**
* [FAO Website](https://www.fao.org)
* Partner contact: [Adroit Associates](https://adroitassociates.org)

### Methods Used
* Data Cleaning
* Data Analysis
* Reporting

### Technologies
* Python
* Pandas
* NumPy
* Typer
* Loguru
* Openpyxl
* TQDM

## Project Description
The Livestock UN-FAO project involves working with data related to livestock outcomes. The data is cleaned, analyzed, and used to generate reports that provide insights on livestock management practices and trends globally. Key tasks include:

1. **Data Processing**: Handling missing values, dropping irrelevant columns, and ensuring the dataset is in a usable format.
2. **Data Analysis**: Performing statistical analyses to uncover trends and patterns in the livestock data.
3. **Reporting**: Preparing clean, actionable reports that highlight key findings for UN-FAO stakeholders.

The challenges of the project include handling large datasets, ensuring the accuracy of the analysis, and presenting the findings in an easily digestible format for non-technical stakeholders.

## Needs of this project

- Data exploration and descriptive statistics
- Data processing and cleaning
- Reporting and visualization of results
- Model development (optional)

## Contributing Members

**Team Leads (Contacts) : [Mirwais Farahi](https://linkedin.com/in/mfarahi/)**

#### Other Members:

|Name     |  Linkedin   | 
|---------|-----------------|
|[Divya Narang](https://github.com/[github handle])| @johnDoe |
|[Mohammad Omid Ahmadi](https://github.com/[github handle]) |     @janeDoe    |

## Contact
* Feel free to contact team leads with any questions or if you are interested in contributing!

## Getting Started

1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/livestock_project.git
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. The raw data can be found [here](data/raw/).

4. Data processing and transformation scripts are located [here](scripts/).

5. To process a dataset, use the following command:
    ```bash
    python dataset.py main <file_name> --output-path <output_file_name>
    ```

### Example Usage

```python
# Specify the file name and optional output path
file_name = "129_ASB_Livestock_Outcome.xlsx"  # Define dataset name
output_path = "processed/129_ASB_Livestock_Outcome_processed.xlsx"  # Optional, can be None

# Process the file
output_file = process_file(file_name, output_path)
print(f"Processed file saved to: {output_file}")

# Get the processed dataset
df = pd.read_excel(output_file)  # Use the output_file Path object directly

