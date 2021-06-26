import setuptools

setuptools.setup(
    name="jupyter-rstudio-proxy",
    version="1.0dev",
    url="https://github.com/jwokaty/jupyter-rstudio-proxy",
    author="J Wokaty",
    description="jwokaty@users.noreply.github.com",
    packages=["jupyter-rstudio-proxy"],
    install_requires=[
        "jupyter-server-proxy"
    ],
    entry_points={
        "jupyter_serverproxy_servers": [
            "rstudio = jupyter_rstudio_proxy:setup_rstudio",
        ]
    },
)
