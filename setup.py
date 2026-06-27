from setuptools import setup, find_packages

setup(
    name="veil",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "typer>=0.9.0",
        "rich>=13.7.0",
        "pyyaml>=6.0",
        "python-dotenv>=1.0.0",
        "stem>=1.8.0",
        "netifaces>=0.11.0",
        "psutil>=5.9.0",
        "playwright>=1.40.0",
        "playwright-stealth>=1.0.0",
        "PyQt6>=6.5.0",
    ],
    entry_points={
        "console_scripts": [
            "veil=veil.main:app",
        ],
    },
    python_requires=">=3.10",
)
