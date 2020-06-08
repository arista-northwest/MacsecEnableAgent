#!/usr/bin/env python

from __future__ import print_function
import os
import sh
import sys
import re
import eapi

agent = "MacsecEnableAgent"

_, local, host = sys.argv[:3]

rpm = os.path.basename(local)

_match = re.search(r"(?:https?\:\/\/)?(?P<hostaddr>.*)", host)

ssh_host = _match.group("hostaddr")
sh.scp(local, "admin@{}:/tmp/{}".format(ssh_host, rpm))

#package = os.path.basename(local)
print(host, rpm)



r = eapi.execute(host, [
    "configure",
    "no extension %s" % rpm,
    "end"
], auth=("admin", ""), verify=False)
print(r)


r = eapi.execute(host, [
    "copy file:/tmp/%s extension:" % rpm,
    "configure",
    "extension %s" % rpm,
    "end"
], auth=("admin", ""), verify=False)
print(r)

r = eapi.execute(host, [
    "configure",
    "trace %s-%s setting %s/*" % (agent, agent, agent),
    "daemon %s" % agent,
    "shutdown",
    "exec /usr/bin/%s" % agent,
    "no shutdown",
], auth=("admin", ""), verify=False)
print(r)
