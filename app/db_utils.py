from sqlalchemy import Table, Column, Integer, String, MetaData, Float

def create_table_from_df(df, engine, table_name):
    """
    Creates a table in the specified database based on the schema of a pandas DataFrame.

    :param df: pandas DataFrame from which the schema is derived.
    :param engine: SQLAlchemy engine object connected to the database.
    :param table_name: Name of the table to be created in the database.
    """
    metadata = MetaData()
    columns = []

    for col_name, col_type in df.dtypes.items():
        if "int" in str(col_type):
            dtype = Integer
        elif "float" in str(col_type):
            dtype = Float
        else:
            dtype = String(255)

        columns.append(Column(col_name, dtype))

    table = Table(table_name, metadata, *columns)

    metadata.create_all(engine, tables=[table])
