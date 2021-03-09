# Robo-Advisor Project

This README.md file explains what the program does and how it should be run from the user's end. 

## Program Functionality 
A robo-advisor here is a program run using Python code in order to advise a user on whether a specific stock. The program is designed to fetch data from an API called ALPHAVANTAGE (more explanation on that later) and then provides the user with the latest stock price high, low, closing price, etc. Moreover, the user can then opt to view a visual representation of the stock price's performance over the years shown in a lineplot. Finally, if the user wants further detail about the stock price and fetching data that dates back to one year (52 weeks) then this option is also available only if the user desires so. 

## Setup 

### Repository Setup 

After cloning the repository onto Github Desktop, and choosing the Desktop as a download location, the user can now navigate from the command-line: 

``` sh
cd ~/Desktop/robo-advisor
```
For more information, the repo already includes a file called *robo_advisor.py* which is located withon a subdirectory called *data*.

### Environment Setup

The user must create and activate a new Anaconda virtual environemnt in order to install third party packages. The user should type the following inside their command-line:

```sh
conda create -n stocks-env python=3.8 # (first time only)
conda activate stocks-env
```
#### Installing Packages 

From within the virtual environment, install the third party packages necessary for the program to run. The third party packages used are already stored, therefore, the user must type the following line of code: 

```sh 
pip install -r requirements.txt
```

#### Running the code

Once evrything is set up, the user can now run the code from the command-line by typing the following:

```sh
python app/robo_advisor.py
```
