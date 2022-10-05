#!/usr/bin/env python
#
# Copyright (c) 2018 Cisco and/or its affiliates
#
from ncclient import manager
from ncclient.xml_ import to_ele
from lxml import etree

fltr = etree.fromstring(b'''<System xmlns="http://cisco.com/ns/yang/cisco-nx-os-device">
            <intf-items>
                <phys-items>
                    <PhysIf-list>
                        <phys-items>
                          <operSt/>
                        </phys-items>
                    </PhysIf-list>
                </phys-items>
            </intf-items>
        </System>''')

m = manager.connect(host="nx",
                     port=830,
                     username="cisco",
                     password="cisco",
                     allow_agent=False,
                     look_for_keys=False,
                     hostkey_verify=False,
                     device_params={'name':'nexus'})

m.create_subscription(filter=("subtree", fltr))

while True:
    n = m.take_notification()
    print(n.notification_xml)
