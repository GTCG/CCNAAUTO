"""
UCS Manager VM required. Set Network adapters to bridge to fetch a valid IP address in your network."""

from ucsmsdk.ucshandle import UcsHandle

Handle = UcsHandle("192.168.110.192", "ucspe", "ucspe")

Handle.login()
BLADES = Handle.query_classid("ComputeBlade")

print ("{0:23s}{1:8s}{2:12s}{3:14s}{4:6s}".format(
    "DN",
    "SERIAL",
    "ADMIN STATE",
    "MODEL",
    "TOTAL MEMORY"))
print ("-"*70)

for BLADE in BLADES:
    print ("{0:23s}{1:8s}{2:12s}{3:14s}{4:6s}".format(
        BLADE.dn,
        BLADE.serial,
        BLADE.admin_state,
        BLADE.model,
        BLADE.total_memory))

    Handle.logout()