import setuptools

setuptools.setup(
    name="jupyter-rstudio-proxy",
    version="1.0",
    url="https://github.com/jwokaty/jupyter-rstudio-proxy",
    author="J Wokaty",
    description="Jupyter extension to proxy Rstudio",
    packages=setuptools.find_packages(),
        keywords=["Jupyter"],
        classifiers=["Framework :: Jupyter"],
    install_requires=[
        "jupyter-server-proxy"
    ],
    entry_points={
        "jupyter_serverproxy_servers": [
            "rstudio = jupyter_rstudio_proxy:setup_rstudio",
        ]
    },
)
