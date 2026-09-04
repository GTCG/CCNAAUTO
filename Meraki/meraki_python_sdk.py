import meraki
from API_KEY import APIKEY
#APIKEY="067f5faf02686f39c30af8172eaa72f33801dd83"

def main():
    try:
        dashboard = meraki.DashboardAPI(APIKEY, suppress_logging=True)
        print("\n===MERAKI ORGANIZATIONS & NETWORKS===\n")
        organizations = dashboard.organizations.getOrganizations()
        if not organizations:
            print ("no organizations found.")
            return
        for org in organizations:
            org_id = org["id"]
            org_name= org["name"]
            print (f"Organization: {org_name}")
            print (f"id: {org_id}")
            print ("-" * 50)
            networks = dashboard.organizations.getOrganizationNetworks(org_id)
            if networks:
                for net in networks:
                    print (f"   network name : {net["name"]}")
                    print (f"   network id : {net["id"]}")
                    print (f"   product type : {',  '.join(net.get('productTypes', []))}")
                    print()
            else:
                print ("no networks found.\n")
        devs = dashboard.organizations.getOrganizationDevices(org_id, total_pages="all")
        for dev in devs:
            print (f"  device name: {dev.get("name", "N/A")}")
            print (f"  model: {dev.get("model", "N/A")}")
            print (f"  serial: {dev.get("serial", "N/A")}")
            print (f"  MAC address: {dev.get("mac","N/A")}")
            print (f"  LAN IP: {dev.get("lanIp", "N/A")}")

           
            print ("=" *50 + "\n")
    except Exception as e:
        print ("\n an error occured")
        print (e)
if __name__ == "__main__":
    main()
                           
