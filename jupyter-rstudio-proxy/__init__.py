#!/usr/bin/env python

def setup_rstudio():
    return {
        "command": [
            "rstudio-server", "start", "---www-port=", "{port}"
        ],
        "launcher_entry": {
            "title": "RStudio"
        },
        "absolute_url": False,
        "port": "8787"
    }
