from google.cloud import bigquery
from litreview.params import PROJECT_ID, LOCATION, DATA_SET


i = 0
#for index in range(100000,2000000,100000):
upload = True
while upload == True:
    data_set = DATA_SET
    #Index(['id', 'authors', 'title', 'doi', 'category', 'abstract', 'versions',
    #'clean_abstract', 'clean_abstract_text', 'count_words'],
    client = bigquery.Client(project=PROJECT_ID, location=LOCATION)
    schemafield_col1 = bigquery.schema.SchemaField("index", "INTEGER")
    schemafield_col2 = bigquery.schema.SchemaField("id", "STRING")
    schemafield_col3 = bigquery.schema.SchemaField("authors", "STRING")
    schemafield_col4 = bigquery.schema.SchemaField("title", "STRING")
    schemafield_col5 = bigquery.schema.SchemaField("doi", "STRING")
    schemafield_col6 = bigquery.schema.SchemaField("cat", "STRING")
    schemafield_col7 = bigquery.schema.SchemaField("abstract", "STRING")
    schemafield_col8 = bigquery.schema.SchemaField("versions", "INTEGER")
    schemafield_col9 = bigquery.schema.SchemaField("cleanabstract", "STRING")
    schemafield_col10 = bigquery.schema.SchemaField("cleanabstracttext","STRING")
    schemafield_col11 = bigquery.schema.SchemaField("countwords", "STRING")
    #filename = f'/Users/viana.abreu/Downloads/data/bigquery/arxiv-metadata_final_{start}_{end}.csv ' # this is the file path to your csv
    #dataset_id = 'new_dataset'
    table_id = f'{PROJECT_ID}.{data_set}.arxiv_complete'
    #dataset_ref = client.dataset(data_set)
    #table_ref = dataset_ref.table(new_table)
    #job_config = bigquery.LoadJobConfig()
    job_config = bigquery.LoadJobConfig(
        schema=[
            schemafield_col1, schemafield_col2, schemafield_col3, schemafield_col4,
            schemafield_col5, schemafield_col6, schemafield_col7, schemafield_col8
        ],
        source_format=bigquery.SourceFormat.CSV,
        allow_quoted_newlines=True,
        skip_leading_rows=1,
    )
    #uri = f'gs://wagon-data-735-vianadeabreu/data/arxiv-metadata_final_{i}_{index}.csv'
    uri = 'gs://wagon-data-735-vianadeabreu/data/final_dataframe_01_dec.csv'
    load_job = client.load_table_from_uri(
        uri,
        table_id,
        location=LOCATION,  # Must match the destination dataset location.
        job_config=job_config,
        )  # Make an API request.

    load_job.result()  # Waits for the job to complete.

    destination_table = client.get_table(table_id)
    print(f"Loaded {table_id}")
    #i = index
    break
