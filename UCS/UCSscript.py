"""
aaaLogin cookie="" response="yes" outCookie="1789644904/cf780e1b-0bc5-41ac-92f7-2532c3e163ed" outRefreshPeriod="600" outPriv="aaa,admin,ext-lan-config,ext-lan-policy,ext-lan-qos,ext-lan-security,ext-san-config,ext-san-policy,ext-san-security,fault,operations,pod-config,pod-policy,pod-qos,pod-security,read-only" outDomains="org-root" outChannel="noencssl" outEvtChannel="noencssl" outSessionId="" outVersion="4.2(2aS9)" outName="" outPasswdExpiryStatus="" outPasswdExpiryDuration="0"> </aaaLogin>
<configFindDnsByClassId cookie="1789644904/cf780e1b-0bc5-41ac-92f7-2532c3e163ed" response="yes" classId="computeItem"> <outDns> <dn value="sys/chassis-3/blade-3"/> <dn value="sys/chassis-4/blade-2"/> <dn value="sys/chassis-3/blade-2"/> <dn value="sys/chassis-4/blade-1"/> <dn value="sys/chassis-3/blade-1"/> <dn value="sys/rack-unit-9"/> <dn value="sys/rack-unit-8"/> <dn value="sys/rack-unit-7"/> <dn value="sys/rack-unit-6"/> <dn value="sys/rack-unit-5"/> <dn value="sys/rack-unit-4"/> <dn value="sys/rack-unit-3"/> <dn value="sys/rack-unit-2"/> <dn value="sys/rack-unit-1"/> </outDns> </configFindDnsByClassId>
<configResolveDn dn="sys/chassis-4/blade-1" cookie="1789644904/cf780e1b-0bc5-41ac-92f7-2532c3e163ed" response="yes"> <outConfig> <computeBlade adminPower="policy" adminState="in-service" assetTag="" assignedToDn="" association="none" availability="unavailable" availableMemory="49152" chassisId="4" checkPoint="deep-checkpoint" connPath="A" connStatus="A" descr="" discovery="failed" discoveryStatus="" dn="sys/chassis-4/blade-1" fltAggr="281479271677953" fsmDescr="blade discovery 4/1(FSM:sam:dme:ComputeBladeDiscover)" fsmFlags="" fsmPrev="DiscoverFail" fsmProgr="39" fsmRmtInvErrCode="none" fsmRmtInvErrDescr="FSM Retries Exhausted" fsmRmtInvRslt="end-point-unavailable" fsmStageDescr="prepare configuration for preboot environment(FSM-STAGE:sam:dme:ComputeBladeDiscover:BmcPreConfigPnuOSPeer)" fsmStamp="2026-09-17T11:48:13.693" fsmStatus="DiscoverFail" fsmTry="20" intId="74786" kmipFault="no" kmipFaultDescription="" lc="undiscovered" lcTs="1970-01-01T00:00:00.000" localId="" lowVoltageMemory="not-applicable" managingInst="A" memorySpeed="not-applicable" mfgTime="not-applicable" model="UCSB-B200-M6" name="" numOf40GAdaptorsWithOldFw="0" numOf40GAdaptorsWithUnknownFw="0" numOfAdaptors="1" numOfCores="0" numOfCoresEnabled="0" numOfCpus="2" numOfEthHostIfs="0" numOfFcHostIfs="0" numOfThreads="0" operPower="on" operPwrTransSrc="unknown" operQualifier="" operQualifierReason="N/A" operState="discovery-failed" operability="operable" originalUuid="00000000-0000-0000-0000-000000000000" partNumber="" policyLevel="0" policyOwner="local" presence="equipped" revision="0" scaledMode="none" serial="SRV130" serverId="4/1" slotId="1" storageOperQualifier="unknown" totalMemory="49152" usrLbl="" uuid="00000000-0000-0000-0000-000000000000" vendor="Cisco Systems Inc" vid=""/> </outConfig> </configResolveDn>
"""


import requests
import xml.dom.minidom

url = "https://192.168.110.192/nuova"

#payload = "<aaaLogin inName=\"ucspe\" inPassword=\"ucspe\"></aaaLogin>"
#payload = "<configFindDnsByClassId classId='computeItem' cookie = '1789644904/cf780e1b-0bc5-41ac-92f7-2532c3e163ed' />"
payload = "<configResolveDn cookie = '1789644904/cf780e1b-0bc5-41ac-92f7-2532c3e163ed' dn = 'sys/chassis-4/blade-1' />"
headers = {
  'Content-Type': 'application/xml'
}

response = requests.request("POST", url, headers=headers, data=payload, verify=False)
pretty = xml.dom.minidom.parseString(response.text)
print(response.text)
#print(pretty.toprettyxml(indent=" "))
