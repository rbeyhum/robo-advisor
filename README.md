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

## Fetching Data from API 

As mentioned, the API used here is ALPHAVANTAGE. In order to use this API, the user needs to create an account which then gives them an API key to use later on. This key is stored in the *.env* file for security reasons and therefore the user must store their own API value in a variable called ALPHAVANTAGE_API_KEY. After that, the user is able to use the API and gather the necessary data. 

### Further Explorations

The basic requirement and the further explorations here follow the same parsed version. However, the further exploration data requests more data than that of the basic requirement. The chart generated is a result of the basic requirement data that only gives 100 data points. In order to calculate the 52 week high and low (assuming the average market days a year is 252), more data was needed and therefore another url was used. 