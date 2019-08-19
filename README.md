# Predictive model on wine Phenological Cycle
This repository include the work for a predictive model on wine  phenological cycle. All the data are in the `data` folder, all the notebooks are found in the jupyter note book within the `jupyternotebook` folder. The interaction with the data for feature extraction is shown 
on the `Interaction with the dataset.ipynb` file.

## Required packages ( recommedation )

It is recommended to using anaconda to install all the required packages. I have included a file that incldue all the pacakges. You can download `env.yaml`

The packages required to run the notebooks and every application on this project are specified in the `env.yaml`.
You can install conda on your machine and clone the repo. You can create conda environment including all the package require for the project using 
 the code below:

```
$ conda env create -f env.yaml
```
those should create an environment with the necessary dependencies to run the application. Then, activate your conda env by
```
activate <env>
```
and finally you can launce jupyter notebook
```
jupyter notebok
```
Now, you you should have a local server created just clikc on the link to open the project on the browser.

## Features
Below are the list of features the data contains
- **minTemp:** The minimum temprature during the day. 
- **maxTempe:** The maxmum temprature during the day.
- **Eto_values:** Evapotranspiration of the plant during the day. 
- **DayPrecip:** Day precipitation 
- **DaySolRad:** Day Solar Radiation 
- **WindSpd:** Wind speed, respectively
- **rain:** Avarage rain collected in the day
- **stages:** incldue the 4 phenological stages (Bud, Bloom, Veraison, and Harvest)

## Regression
## Classification
<!--[![Dashboard using Bokeh](https://img.youtube.com/vi/eGM2O1w6aUk/0.jpg)](https://youtu.be/eGM2O1w6aUk) -->
### Results 
- CNN model ( simple structure mentioned on the paper attached )
    - Trained without normalization (53 percent accuracy)
    - Trained with normalization (61.33 percent accuracy)
    - Trained on AWS using the g3s.xlarge instance (75 percent accuracy)

<!---
OLS stands for Ordinary Least Squares and the method “Least Squares” means that we’re trying to fit a regression line that would minimize the square of distance from the regression line

Using this model for the **First Byte:** being Y, p1 =**Speed Index**, p2 = **Load time**, p3 = **Start render**, p4 = **DOM elements**
the coefficent for each parameters will be as follows:
```
Y = -0.7179*p1 + 0.5839*p2 +0.7944*p3 +-1.3634*p4
```



 login twitter https://en.wikipedia.org/wiki/Annual_growth_cycle_of_grapevines 
# Takes to do
- look for dataset that have growing date information upto harvest date
- create a SVM or any machine learning model
- work on your thesis (was it was been mentioned)

# Resource 

- data.world
below is a good source to use the world production of graph per hactar 
https://public.opendatasoft.com/explore/dataset/wine-area-cepages-france/table/?sort=-year


Setup Process:
ssh -i KirubelAWS.pem ubuntu@<addresse to dns>

Todo:
______________________________
YouTube Video: 30 
Classification:
Self:
Outline Draft:
  # preliminary


# Some idea of changing the structure of the Neural Network.

* using PCA to reduce the feature
* using fine tuning 
* using pretrained VGG network


# I can use the functional API to create the DD and use the as a column and feed it to the neural network.

# multinomial Logistic Classification
___________________________________________

# trying to formate the output layer to an actual date (52 weeks)





# Book

``` A simple way to initialize Recurrent Networks of Rectified Linear Units ``` Basically you can initialize the hidden layer with 
identity metrixs and get result comparable to LSTM





Note book setup

Create a password for jupyter notebook
ipython

from IPython.lib import passwd

passwd()

Enter password: [Create password and press enter] Verify password: [Press enter]

'sha1:98ff0e580111:12798c72623a6eecd54b51c006b1050f0ac1a62d'

exit

Create config profile
jupyter notebook --generate-config

Create certificates for https
mkdir certs

cd certs

sudo openssl req -x509 -nodes -days 365 -newkey rsa:1024 -keyout mycert.pem -out mycert.pem

Answer questions

Configure jupyter
cd ~/.jupyter/

vi jupyter_notebook_config.py


c = get_config()

# Kernel config
c.IPKernelApp.pylab = 'inline'  # if you want plotting support always in your notebook

# Notebook config
c.NotebookApp.certfile = u'/home/ubuntu/certs/mycert.pem' #location of your certificate file
c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.open_browser = False  #so that the ipython notebook does not opens up a browser by default
c.NotebookApp.password = u'sha1:98ff0e580111:12798c72623a6eecd54b51c006b1050f0ac1a62d'  #the encrypted password we generated above
# Set the port to 8888, the port we set up in the AWS EC2 set-up
c.NotebookApp.port = 8888
-->