#!/bin/bash
SOCKET=~/.ssh/ssh_auth_sock
ENV=~/.ssh/agent.env
ssh-agent -a $SOCKET > $ENV
source ~/.ssh/agent.env 1>/dev/null
