# Job Description Preprocessing Tool

This script is a utility for generating job descriptions from markdown templates using [General Defitions](../../../GeneralDefinitions.md) to make editing easier and promote consistency.

## Requirements

- Python 3.x
- Access to the terminal or command line interface
- Definitions of the Job (Salary, Requierments, etc) with this format:
```
{Def Title}
{Def Salary}
{Def Equity}
{Def Role}
{Def Responsibilities}
{Def Requirements}
```
Example: [Defition for Data Scientist](specs_ds.md)

## Setup

No additional libraries are required to run this script as it only uses the standard library provided by Python.

## Usage

To use this script, follow these steps:

1. Prepare your Job Definitions in a markdown file.

2. Place your template markdown file in the directory of the script or provide the path to it. 

3. Run the script from the terminal with the following command structure:

```bash
python generatejob.py [specs_ds.md] [DataScientist.md]
````