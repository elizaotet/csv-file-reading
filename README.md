# CSV Training Run Analyzer

A Python command-line script that calculates the average duration and number of successful training runs for each model. It reads `logs.csv` with Python's standard `csv` module and includes runs whose status is `OK`.

## Run locally

Keep `main.py` and `logs.csv` in the same folder. Open a terminal in that folder and run the script with Python 3.

```powershell
python main.py
```

## Example input

`logs.csv` uses the following columns. Durations are whole seconds.

```csv
run_id,model,status,duration_seconds
run-01,bert,OK,12
run-02,gpt,FAILED,8
run-03,bert,OK,15
```

## Example report

```text
bert: 13.5 seconds average (2 successful runs)
```

The report includes models with at least one successful run.
