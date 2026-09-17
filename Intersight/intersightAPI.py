import re
import intersight
from intersight.api import equipment_api
from intersight.api import boot_api

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

api_instance = equipment_api.EquipmentApi(api_client)
devices = api_instance.get_equipment_device_summary_list().results

print('{0:35s}{1:40s}{2:13s}{3:14s}'.format("DN", "MODEL", "SERIAL", "OBJECT TYPE"))
print("-" * 105)

for device in devices:
    print('{0:35s}{1:40s}{2:13s}{3:14s}'.format(
        device.dn,
        device.model,
        device.serial,
        device.source_object_type))
    
boot_api_instance = boot_api.BootApi(api_client)

api_response = boot_api_instance.get_boot_precision_policy_by_moid(moid="6aabe012627572310529a6d4")
print(api_response.name)
print(api_response.description)