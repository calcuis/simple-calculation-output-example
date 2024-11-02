### simple calculation and output example
try it out by:
```
py calculator.py
```
### code explanation
- Reading the csv: The `input.csv` file is loaded into a `DataFrame`.
- Grouping and Summing: The `DataFrame` is grouped by `id` and `group`, summing the `min` column.
- Exporting to csv: The grouped data is saved in `output.csv`.
- Exporting to json: The grouped data is restructured into a json format, nested under each id, and saved to `output.json`.

it will produce two files (`output.csv` and `output.json`) as a result; enjoy!
