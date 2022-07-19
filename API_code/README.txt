# Resume API

Send Response in ranking order of resumes

## Getting Started

These instructions will get you a copy of the project up and running on your local/virtual machine for development and testing purposes. 


### Prerequisites


```
Python version > 3.9

```

### Installing

Clone the repository to your local system.

Run the init script to initialize environment and install project related dependencies. This may take several minutes to complete.

```
pip install -r requirements.txt
```

After successfully installing the dependencies, run the run script.

```
 set Flask_app=file_name.py
 flask run -p portNo{ from properties files}
```

This will setup the basic requirements

## Testing the APIs

Use Postman Collection to test API

```
  For TEsting - [http://127.0.0.1:5050/getdata]
  The above API Input request in the given format
  {"SrfNo":"0048584_23","Skills":"INSURANCE","Job_Description":" see above","SkillWeightage":60,"ExperienceWeightage":0,"LocationWeightage":40,"SkillSearch":"Java","ExperienceSearch":2,"LocationSearch":"Pune"}
  POST Json
  file_name = demo.py

```

  For Fetching data - [http://127.0.0.1:6060/fetchData]
  It is scheduler which requires POST request

## Properties Files for DB Connection
  Need to update the variables as per the System DB

## Issues
```
The Scheduler does not have to the CIO team DB for scheduler
```





