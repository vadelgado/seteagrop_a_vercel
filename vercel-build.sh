#!/bin/bash

# Install required dependencies
apt-get update
apt-get install -y libmysqlclient-dev

# Run the default build command
exec "@vercel/python"
