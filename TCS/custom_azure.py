from storages.backends.azure_storage import AzureStorage
import os

try:
    os.environ["IS_PRODUCTION"]
except KeyError:
    pass
else:
    from TCS.settings import AZURE_ACCOUNT_NAME

    ACCOUNT_KEY = os.environ["STORAGE_ACCOUNT_KEY"]


    class AzureMediaStorage(AzureStorage):
        account_name = AZURE_ACCOUNT_NAME  # Must be replaced by your <storage_account_name>
        account_key = ACCOUNT_KEY  # Must be replaced by your <storage_account_key>
        azure_container = 'media'
        expiration_secs = None


    class AzureStaticStorage(AzureStorage):
        account_name = AZURE_ACCOUNT_NAME  # Must be replaced by your storage_account_name
        account_key = ACCOUNT_KEY  # Must be replaced by your <storage_account_key>
        azure_container = 'static'
        expiration_secs = None
