# Momentum Stock Analysis Tool

## Instructions 

After Setup is complete, the program project.py can be executed. When the program is executed, the user will input a stock ticker. The available stock choices are AAPL (Apple), GOOG (Google), NFLX (Netflix), or Facebook (FB).

Once the user input is complete, the program will run and output a stock report indicating the gold cross and death cross events, and provide a chart showing the 50-day and 200-day moving averages.

## Setup

### Repo Setup 

Use the GitHub.com online interface to create a new remote project repository called something like "groceries-exercise". When prompted by the GitHub.com online interface, let's get in the habit of adding a "README.md" file and a Python-flavored ".gitignore" file (and also optionally a "LICENSE") during the repo creation process. 

After creating the remote repo, use GitHub Desktop software or the command-line to download or "clone" it onto your computer. Choose a familiar download location like the Desktop.

After cloning the repo, navigate there from the command-line:

```sh
cd ~/Desktop/project2
```

### Environment Setup


Use Anaconda to create and activate a new virtual environment, perhaps called "game-env":

```sh
conda create -n project-env python=3.7 # (first time only)
conda activate project-env
```

From inside the virtual environment, install package dependencies:

```sh
pip install pandas
pip install matplotlib
```

## Usage

Run the project script:

```sh
python project.py
```

There will be a prompt for user input:

```sh
Please select one of the following Stocks - AAPL, GOOG, NFLX, FB:
```

Note: You can only specify one of the four stocks in the prompt.
