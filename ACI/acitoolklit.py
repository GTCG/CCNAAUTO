from acitoolkit.acitoolkit import Tenant, AppProfile, EPG, Session

# 1. Establish a session with APIC
session = Session('https://10.10.20.185', 'admin', 'Cisco1234!')
session.login()

# 2. Create the TENANT first — it's the top of the object hierarchy
tenant = Tenant('tutorial')

# 3. Create the AppProfile, passing the parent (tenant) into the constructor
app = AppProfile('myapp', tenant)

# 4. (Optional) Create an EPG under the AppProfile, same pattern
epg = EPG('myepg', app)

# 5. Push ONLY the top-level parent object — ACI Toolkit walks the
#    object tree and pushes all children (app, epg, etc.) automatically
resp = tenant.push_to_apic(session)