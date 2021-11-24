from google.cloud import storage
client = storage.Client()
new_bucket = client.create_bucket('new-bucket-id')
new_blob = new_bucket.blob('remote/path/storage.txt')
new_blob.upload_from_filename(filename='/local/path.txt')

# Retrieve an existing bucket
# https://console.cloud.google.com/storage/browser/[bucket-id]/
bucket = client.get_bucket('litreview-bucket')
# Then do other things...
blob = bucket.get_blob('remote/path/to/file.txt')
print(blob.download_as_bytes())
blob.upload_from_string('New contents!')