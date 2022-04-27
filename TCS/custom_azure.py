from storages.backends.azure_storage import AzureStorage


class AzureMediaStorage(AzureStorage):
    account_name = 'thalosqa'  # Must be replaced by your <storage_account_name>
    account_key = 'LtydyCKpgsEsbKTWjPuHr6/eQI6lHP7WZcpsJRW74Mrg7V2nPdFfFhkwz6nznXnM4jFaUSbH8V1/qByXEDm3XQ=='  # Must be replaced by your <storage_account_key>
    azure_container = 'media'
    expiration_secs = None


class AzureStaticStorage(AzureStorage):
    account_name = 'thalosqa'  # Must be replaced by your storage_account_name
    account_key = 'LtydyCKpgsEsbKTWjPuHr6/eQI6lHP7WZcpsJRW74Mrg7V2nPdFfFhkwz6nznXnM4jFaUSbH8V1/qByXEDm3XQ=='  # Must be replaced by your <storage_account_key>
    azure_container = 'static'
    expiration_secs = None
