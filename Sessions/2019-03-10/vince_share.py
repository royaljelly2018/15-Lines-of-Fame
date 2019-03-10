#!/usr/bin/env python

import sys

# run with: "cat test-var-lib-mesos-attributes.py | ssh mesos@<hostname> python -"

# Search values
mesos_attribute1="capabilities_class"
mesos_attribute2="agent_location"

# Open file and present contents as variable.
with file("/var/lib/dcos/mesos-slave-common") as f:
    attributes_file = f.read()

# Check for search values.
if str(mesos_attribute1) not in attributes_file:
    mesos_attribute1_state=False
    print("\tAgent misconfigured: capabilities_class not defined.")
else:
    mesos_attribute1_state=True

if str(mesos_attribute2) not in attributes_file:
    mesos_attribute2_state=False
    print("\tAgent misconfigured: agent_location not defined.")
else:
    mesos_attribute2_state=True

# Error detection and handling.
if mesos_attribute1_state == True and mesos_attribute2_state == True:
   sys.exit(0)
else:
   sys.exit(1)
