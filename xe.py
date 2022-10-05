#!/usr/bin/env python
#
# Copyright (c) 2018 Cisco and/or its affiliates
#
from ncclient import manager

m = manager.connect(host="8000v",
                     port=830,
                     username="cisco",
                     password="cisco",
                     allow_agent=False,
                     look_for_keys=False,
                     hostkey_verify=False,
                     device_params={'name':'iosxe'})

m.create_subscription()

while True:
    n = m.take_notification()
    print(n.notification_xml)
