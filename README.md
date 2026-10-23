# Healthcare Accessibility Analysis in Sierra Leone

## Student Information

| Detail | Information |
| **Student Name** | Alhaji Abubakarr Jalloh |
| **Student ID** | 905005263 |
| **Class** | DIT2101 |


## Project Overview

This project was developed as part of the Data Science Fundamentals (COMM104) assignment at Limkokwing University of Creative Technology, Sierra Leone.

The project examines healthcare facility distribution across Sierra Leone using a real-world dataset. Python is used for data exploration, cleaning, validation, analysis, and visualization.

The project supports **Sustainable Development Goal 3 (SDG 3): Good Health and Well-being**, particularly Target 3.8 concerning universal health coverage.

## Project Objectives

- Examine healthcare facility distribution across Sierra Leone's districts.
- Analyze facility types, ownership, and functional status.
- Identify missing values, duplicate records, and invalid coordinates.
- Clean and prepare healthcare data using Python.
- Generate visualizations to support data interpretation.

## Dataset

**Source:** Sierra Leone National Health Facilities Dataset Version 01 (2023), Ministry of Health and GRID3.

- **Records:** 1,616 healthcare facilities
- **Districts:** 16
- **Columns:** 15
- **Formats:** GeoJSON and CSV

[View Original Dataset](https://services3.arcgis.com/BU6Aadhn6tbBEdyk/ArcGIS/rest/services/sle_htlfac_grid3_v01/FeatureServer/0)

## Technologies Used

Python, Pandas, Matplotlib, Seaborn, Visual Studio Code, Git, and GitHub.

## Project Files

| File | Description |
|---|---|
| `main.py` | Dataset loading and exploration |
| `clean_data.py` | Data cleaning and preparation |
| `visualize_data.py` | Data visualization |
| `analysis.py` | Healthcare facility analysis |
| `verify_data.py` | Final data-quality verification |
| `data/` | Original dataset |
| `outputs/` | Cleaned dataset, charts, and results |

## Data Cleaning Procedures

The project examines missing values, checks duplicate records, standardizes text formatting, validates geographical coordinates, investigates repeated facility identifiers, and exports the prepared dataset.

## How to Run

Install the required libraries:

`python -m pip install pandas matplotlib seaborn`

Run the scripts in sequence:

1. `python main.py`
2. `python clean_data.py`
3. `python visualize_data.py`
4. `python analysis.py`
5. `python verify_data.py`

## Limitations

The dataset represents facilities recorded in 2023. Facility counts alone cannot establish healthcare accessibility without considering population, travel distances, staffing, and service availability.

## Conclusion

This project demonstrates how data science techniques can support the understanding of healthcare facility distribution in Sierra Leone. The findings provide a foundation for further research into healthcare accessibility and development planning.

## Academic Information

Institution: Limkokwing University of Creative Technology, Sierra Leone

Module: COMM104 — Data Science Fundamentals

Assignment: Identifying and Preparing Data for a Sierra Leone Development Problem

Project Type: Academic Data Science Project