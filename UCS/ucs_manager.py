#!/usr/bin/env python
"""
CCNA_AUTO project - UCS Manager connection example
Demonstrates correct UcsHandle instantiation and login/logout.

Common mistake: passing port as a string (port="443") instead of an
integer (port=443). ucsmsdk validates parameter types and will raise
a UcsValidationException if port is not an int.
"""

from ucsmsdk.ucshandle import UcsHandle
from ucsmsdk.ucsexception import UcsException, UcsValidationException

# Connection details
UCS_IP = "10.1.14.32"
UCS_USER = "boson"
UCS_PASSWORD = "exsim"
UCS_PORT = 443          # int, NOT "443" (string) - this is what breaks the original code
UCS_SECURE = False       # False = plain HTTP, True = HTTPS


def main():
    handle = UcsHandle(UCS_IP, UCS_USER, UCS_PASSWORD, port=UCS_PORT, secure=UCS_SECURE)

    try:
        # Establish the session
        handle.login()
        print(f"Connected to UCS Manager at {UCS_IP}")

        # Example: pull basic system info
        managed_objects = handle.query_classid("computeRackUnit")
        for mo in managed_objects:
            print(f"Rack Unit: {mo.dn} | Model: {mo.model} | Serial: {mo.serial}")

    except UcsValidationException as ve:
        print(f"Validation error (likely a type/argument issue): {ve}")
    except UcsException as e:
        print(f"UCS API error: {e}")
    finally:
        # Always log out to release the session/token
        if handle:
            handle.logout()
            print("Session closed.")


if __name__ == "__main__":
    main()