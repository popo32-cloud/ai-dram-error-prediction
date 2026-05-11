# AI-Based DRAM Error Prediction System

This project aims to predict memory error occurrence under different operating conditions such as temperature, voltage, refresh interval, timing margin, and noise level.

The system uses a DRAM-like simulation model to generate memory error data and trains machine learning models to predict error probability.

## Project Goal

To implement an AI-based memory error prediction system that estimates the probability of memory errors caused by environmental and timing-related factors.

## Main Features

- DRAM-like memory error data generation
- Error probability modeling
- Machine learning-based prediction
- Feature importance analysis
- Adaptive refresh decision concept

## Input Variables

- Temperature
- Voltage
- Refresh interval
- Timing margin
- Noise level
- Leakage factor

## Output

- Error label: 0 or 1
- Error probability: 0.0 to 1.0

## Tech Stack

- Python
- pandas
- numpy
- scikit-learn
- matplotlib
- joblib

## Project Structure

```text
ai-dram-error-prediction/
├─ README.md
├─ PROJECT_SPEC.md
├─ requirements.txt
├─ data/
├─ src/
├─ notebooks/
└─ results/
