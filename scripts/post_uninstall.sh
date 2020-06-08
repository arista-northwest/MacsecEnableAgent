#!/bin/sh
AGENT=MacsecEnableAgent
DEST=/usr/lib/SysdbMountProfiles/$AGENT
[ -e $DEST ] && rm -f $DEST
