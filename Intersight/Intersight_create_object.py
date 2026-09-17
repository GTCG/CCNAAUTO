from intersight.api import boot_api
from intersight.model.boot_precision_policy import BootPrecisionPolicy
from intersight.model.boot_device_base import BootDeviceBase
import re
import intersight
from intersight.api import equipment_api

def get_api_client(api_key_id, api_secret_file, endpoint="https://eu-central-1.intersight.com"):
    with open(api_secret_file, 'r') as f:
        api_key = f.read()

    if re.search('BEGIN RSA PRIVATE KEY', api_key):
        signing_algorithm = intersight.signing.ALGORITHM_RSASSA_PKCS1v15
    elif re.search('BEGIN EC PRIVATE KEY', api_key):
        signing_algorithm = intersight.signing.ALGORITHM_ECDSA_MODE_DETERMINISTIC_RFC6979

    configuration = intersight.Configuration(
        host=endpoint,
        signing_info=intersight.signing.HttpSigningConfiguration(
            key_id=api_key_id,
            private_key_string=api_key,
            signing_scheme=intersight.signing.SCHEME_HS2019,
            signing_algorithm=signing_algorithm,
            hash_algorithm=intersight.signing.HASH_SHA256,
            signed_headers=[
                intersight.signing.HEADER_REQUEST_TARGET,
                intersight.signing.HEADER_HOST,
                intersight.signing.HEADER_DATE,
                intersight.signing.HEADER_DIGEST,
            ]
        )
    )
    return intersight.ApiClient(configuration)



api_client = get_api_client(
    api_key_id="6aabd833756461330526b92e/6aabd833756461330526b936/6aabd9a47564613105396ded",
    api_secret_file="API1-SecretKey.txt"
)

api_instance = boot_api.BootApi(api_client)

boot_local_disk = BootDeviceBase(
    class_id="boot.LocalDisk",
    object_type="boot.LocalDisk",
    name="local_disk1",
    enabled=True
)

boot_precision_policy = BootPrecisionPolicy()
boot_precision_policy.name = "sample_boot_policy1"
boot_precision_policy.description = "test policy"
boot_precision_policy.boot_devices = [boot_local_disk]



api_response = api_instance.create_boot_precision_policy(boot_precision_policy)
print(api_response.moid)