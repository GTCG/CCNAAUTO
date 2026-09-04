from meraki_sdk.meraki_sdk_client import MeraikiSdkClient
Bearer = "X"
Meraki = MeraikiSdkClient(Bearer)
orgs = Meraki.organizations.get_organizations()
for org in orgs:
    print ("ORG ID: {} and ORG name: {}".format(org["id"], org["name"]))
PARAMS= {}
PARAMS["organization_id"] = "x"


