#!/usr/bin/env python

def setup_rstudio():
    return {
        "command": [
            "/usr/lib/rstudio-server/bin/rsession", 
            "-u", "waldronlab",
            "--session-root-path", "/home/waldronlab",
            "---www-port=", "{port}"
        ],
        "launcher_entry": {
            "title": "RStudio"
        },
        "absolute_url": False,
        "port": "8787"
    }
