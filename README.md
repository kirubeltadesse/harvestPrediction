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