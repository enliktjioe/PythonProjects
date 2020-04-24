# Suggested setup

## Software

### Core
Download and install Anaconda Python distribution: https://www.anaconda.com/download/.
Installing Anaconda will also install the Jupyter Notebook executable and most of the necessary libraries.
I strongly suggest to add Anaconda executables to the system path when asked at the end of the installation.

All examples in the course demos use Jupyter Notebook. To launch it in the right directory run the following command in your terminal:
`jupyter notebook --notebook-dir=<PATH_TO_DEMOS_FOLDER>`

Core software versions used (higher should be fine too):
* Python 3.6.8 
* Pandas 0.24.2
* Dask 1.2.2
* NumPy 1.16.3

### Not critical (but suggested)
* Last module uses Docker and docker-compose. Please follow the installation instruction to install it on your machine - i stronly suggest following the examples
* Visualizing task graphs will require Graphviz installation and Graphviz command to be available on your system PATH - this is optional as this functionality is not used heavily, and the most relevant output of commands that use graphviz will be shown on the demos.

## Data
As this course focuses on big data processing, and the datasets are quite big, each of them is packed separately with 7z so you don't need to unpack everything upfront to start the course.
Below is the list of datasets required for individual modules:

* Module 3
  - Clip 2 - osm/NewYork.osm.7z - 1,21 GB unpacked
  - Clip 4 - osm/southamerica.7z - 33,3 GB unpacked

* Module 4 (keep previous ones)
  - osm/ny.7z - 3,64 GB unpacked 
  After M4 osm datasets can be removed.

* Modules 5 & 6 - telco.7z - 19,2 GB unpacked 

After unpacking, that directory with the data should be in the same place a the 7z file. For example, the files for South America should be located as follows:

demos -> data -> osm -> southamerica -> *.txt

All datasets used in this course, contained inside the `data` folder provided here are licensed under the Open Database License:

*This data is made available under the Open Database License: http://opendatacommons.org/licenses/odbl/1.0/. Any rights in individual contents of the database are licensed under the Database Contents License: http://opendatacommons.org/licenses/dbcl/1.0/*

Original data comes from:
* OpenStreetMap - https://download.geofabrik.de/ and https://download.bbbike.org/osm/ 
* SpazioDati - https://dandelion.eu/datamine/open-big-data/

In case of any question or doubts contact the course author - pawel.kordek@gmail.com