# Quickstart

Hyenas is a curde Hy handle written on top of Pandas API to allow for more elegant access to data-scientist's powerhouse that is Pandas.

## Installation

To quickstart with Hyenas you will need to:

1. Install [Hy](https://docs.hylang.org/en/alpha/)
2. Download Hyenas by pulling this repository and executing the following commands:
```
cd ./hyenas
pip install -r requirements.txt
python -m build
pip install ./dist/hyenas-0.0.1-py3-none-any.whl
```
## Usage

Hy - while very humble in its Pandas API coverage as of now - currently boasts an SQL like interface to access dataframe structures.
```
(import [hyenas[*]])
(import [pandas [read_csv]])

(
    select  :cols [(count_agg "long_name") (mean_agg "weight_kg")] 
            :from_df (read_csv "/some/data/players_21.csv") 
            :group_by ["height_cm"]
)
```

# Project Status
Hyenas is currently in its infancy. Collaboratos, Pull Requests and Issues are welcome.
