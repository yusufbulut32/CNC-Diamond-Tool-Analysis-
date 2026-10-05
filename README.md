# CNC Tool Wear Analysis & Decision Support

## Project Overview

This project focuses on monitoring CNC cutting tool wear
and supporting tool replacement decisions using a data-driven approach.

The project was inspired by an observation made during an
industrial internship, where tool replacement decisions were
largely based on operator experience and visual inspection.

## Objective

The objective of the project is to analyze cutting tool wear
and develop a decision support prototype for tool replacement.

## Data

The dataset used in this project is synthetic and does not
represent real production measurements.

## Technologies

- Python
- Pandas
- PostgreSQL
- SQL
- SQLAlchemy
- Matplotlib
- Streamlit

## Project Workflow

Production Problem
→ Synthetic Data
→ PostgreSQL
→ SQL Analysis
→ Python / Pandas
→ Wear Classification
→ Decision Support
→ Streamlit Dashboard

## Decision Support

Tool wear is classified into three levels based on predefined wear thresholds:

- Normal: wear < 0.10 mm
- Monitor: 0.10 mm ≤ wear < 0.20 mm
- Replacement Recommend: wear ≥ 0.20 mm

These thresholds are project-defined and are not intended to represent industry-standard limits.

## Limitations

The dataset is synthetic because numerical tool wear measurements
were not available from the internship environment.

Therefore, the results should not be interpreted as actual
production performance or cost savings.

 