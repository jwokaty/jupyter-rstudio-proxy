import os

def setup_rstudio():
    return {
        "command": ["/usr/lib/rstudio-server/bin/rstudio-server", "start"],
        "launcher_entry": {
            "title": "RStudio"
        },
        "absolute_url": False,
        "port": "8787"

    }
