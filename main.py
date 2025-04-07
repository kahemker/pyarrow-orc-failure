import pyarrow as pa
import pyarrow.orc as orc
import datetime
import polars as pl

table_schema = pa.schema([('REGION', pa.string()),
                          ('USER', pa.string()),
                          ('CREATED_ON', pa.timestamp(unit='us', tz=None))]
                          )

def main():
    example_data = {'REGION': ['Other'],
                    'USER': ['test'],
                    'CREATED_ON': [datetime.datetime(2024, 11, 7, 10, 26, 16, 606509)]}
    df = pl.DataFrame(example_data)
    with orc.ORCWriter('test.orc.snappy', compression='SNAPPY') as writer:
        writer.write(df.to_arrow().cast(table_schema))


if __name__ == "__main__":
    main()
