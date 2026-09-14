from ydk.services import CRUDService
from ydk.providers import NetconfServiceProvider
from ydk.models.cisco_ios_xe import Cisco_IOS_XE_native as xe_native

provider = NetconfServiceProvider(address="10.10.20.175", port=830, username="cisco", password="cisco", protocol="ssh")
crud = CRUDService()

native = xe_native.Native()
interface = native.interface.GigabitEthernet()
interface.name = "1"
interface.description = "configured via YDK"
native.interface.gigabit_ethernet.append(interface)

crud.create(provider, native)