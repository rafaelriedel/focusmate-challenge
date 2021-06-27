#!/usr/bin/env python

import os

from app import create_app

config_name = os.getenv('APP_SETTINGS')  # config_name = "development"
a = create_app(config_name)

if __name__ == '__main__':
    a.run(host='0.0.0.0', debug=1)
