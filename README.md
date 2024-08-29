# Eagy Broker: Real-Time Stock Simulation

Eagy Broker is a Python-based simulation tool that models real-time stock price movements for two companies, Amazon (AMZN) and Apple (AAPLE). The simulation includes dynamic price updates and provides visual indicators for buy and sell signals based on price fluctuations.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Simulation](#running-the-simulation)
- [Understanding the Simulation](#understanding-the-simulation)
- [Error Handling](#error-handling)
- [Creating and Using a Virtual Environment](#creating-and-using-a-virtual-environment)

## Features

- **Real-Time Simulation**: Visualizes stock price changes in real-time for AMZN and AAPLE.
- **Buy/Sell Signals**: Automatically detects and marks buy (green dots) and sell (red dots) signals based on price changes.
- **Probability-Based Price Movement**: Prices are updated based on the probability of share purchases and sales.
- **User-Friendly Visualization**: Includes legends and clear titles for each stock.

## Prerequisites

To run the simulation, you need:

- **Python 3.x**: Download and install Python from [python.org](https://www.python.org/downloads/).
- **pip**: Ensure `pip` is installed to manage Python packages (comes with Python).

## Installation

1. **Clone the Repository**:
   Clone this repository to your local machine:
   ```bash
   git clone https://github.com/herhu/COMMONSHARE-TECH-.git
   cd COMMONSHARE-TECH-
   ```

2. **Create and Activate a Virtual Environment**:
   It is recommended to create a virtual environment to manage dependencies.
   ```bash
   python -m venv venv
   ```
   - **Activate the Virtual Environment**:
     - On **Windows**:
       ```bash
       venv\Scripts\activate
       ```
     - On **macOS/Linux**:
       ```bash
       source venv/bin/activate
       ```

3. **Install Required Libraries**:
   Use `pip` to install the necessary Python packages:
   ```bash
   pip install matplotlib
   ```

## Running the Simulation

1. **Run the Script**:
   Execute the simulation by running the Python script:
   ```bash
   python eagy_broker.py
   ```

2. **View the Simulation**:
   - A window will appear with two plots: one for AMZN and another for AAPLE.
   - The plots update in real-time, showing price changes and marking buy (green) and sell (red) signals.

3. **Stop the Simulation**:
   - To stop the simulation, close the plot window or press `Ctrl + C` in the terminal.

## Understanding the Simulation

- **Price Updates**: 
  - The simulation calculates the probability of price increases or decreases based on the number of shares bought and sold.
  - Prices are updated every second, and a new price is generated every time the total shares traded exceed 2000.

- **Buy/Sell Signals**:
  - A **buy signal** is triggered when the price decreases by 10% or more from the initial price.
  - A **sell signal** is triggered when the price increases by 10% or more from the initial price.

- **Visualization**:
  - The blue line represents AMZN's stock price, and the orange line represents AAPLE's stock price.
  - Green dots indicate buy signals, and red dots indicate sell signals.

## Error Handling

- The code includes error handling to manage unexpected issues during simulation and evaluation.
- The program exits cleanly if interrupted by the user (e.g., pressing `Ctrl + C`).

## Creating and Using a Virtual Environment

Using a virtual environment is a good practice to manage project dependencies and avoid conflicts with other Python packages on your system.

### Steps to Create a Virtual Environment:

1. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   ```
   This command creates a new directory called `venv` that contains a standalone Python environment.

2. **Activate the Virtual Environment**:
   - On **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - On **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

   Once activated, your terminal prompt will change to indicate that you are now working within the virtual environment.

3. **Deactivate the Virtual Environment**:
   When you're done working, you can deactivate the virtual environment by running:
   ```bash
   deactivate
   ```
