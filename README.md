This experiment compares the brand registrations of Germany's most active companies in the years 2017 and 2019.

# File naming convention
The file naming convention for data input/output is: `[name]-[DDMMYYYY]`. If the name consists of multiple words they are seperated by `-`.
The file naming convention for Python scripts is: `[name].py`. The name is written in camelcase format.

# Data Sources
- Data from 2017: [GovData Germany](https://www.govdata.de/web/guest/suchen/-/details/markeneintragungen-2017-liste-der-aktivsten-unternehmen-und-institutionen)
- Data from 2019: [GovData Germany](https://www.govdata.de/web/guest/suchen/-/details/markeneintragungen-2019-liste-der-aktivsten-unternehmen-und-institutionen)

# Running the code
To run the code at least Python version 3.8.10 has to be installed. `requirements.txt` contains all needed packages. To install them please run `python -m pip install -r requirements.txt`.

## main.py 
Run this file to conduct the experiment.

## dataPreprocessing.py
It merges the two input datasets into a table containing the company names and their corresponding amount of brand registrations in 2017 and 2019.

## dataVisualization.py
It creates a bar plot, which compares the brand registrations from 2017 and 2019.

# Result
After running the experiment results can be found in the directory `/data/output/`. 

