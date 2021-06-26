import os

def setup_rstudio():
    return {
        "command": ["rstudio-server", "start", "8787"],
        "launcher_entry": {
            "title": "RStudio"
        },
        "absolute_url": False
    }
