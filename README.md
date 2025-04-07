# pyarrow-orc-failure
Demonstrating how pyarrow cannot write ORC files with time zone data if the virtual environment is created using UV on Windows

Steps to recreate the problem.
1. Clone the repo
2. Run `uv sync` to install polars and pyarrow using pyproject.toml
3. Run `uv run main.py`

The error message is 

```
Traceback (most recent call last):
  File "W:\code\test_pyarrow\main.py", line 21, in <module>
    main()
  File "W:\code\test_pyarrow\main.py", line 17, in main
    writer.write(df.to_arrow().cast(table_schema))
  File "W:\code\test_pyarrow\.venv\Lib\site-packages\pyarrow\orc.py", line 289, in write
    self.writer.write(table)
  File "pyarrow\\_orc.pyx", line 439, in pyarrow._orc.ORCWriter.write
  File "pyarrow\\error.pxi", line 92, in pyarrow.lib.check_status
pyarrow.lib.ArrowException: Unknown error: Time zone file /usr/share/zoneinfo/GMT does not exist. Please install IANA time zone database and set TZDIR env.
```
