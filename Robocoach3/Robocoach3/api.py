from azure.storage.blob import BlobService
blob_service = BlobService(account_name=settings.AZ_ACCOUNT_NAME, account_key=settings.AZ_ACCOUNT_KEY)

blob_service.get_blob_to_path(‘roboshare’, infile, filename)