"""
Setup configuration for 1TamilMV Telegram Bot
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text(encoding="utf-8") if readme_file.exists() else ""

# Read requirements
requirements_file = Path(__file__).parent / "requirements.txt"
requirements = []
if requirements_file.exists():
    with open(requirements_file) as f:
        requirements = [
            line.strip() for line in f 
            if line.strip() and not line.startswith("#")
        ]

setup(
    name="1tamilmv-bot",
    version="3.0.0",
    author="1TamilMV Development Team",
    author_email="dev@1tamilmv.dev",
    description="The #1 Telegram Bot for Tamil Movies, OTT Updates & Movie Information",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/YourUsername/1TamilMV",
    project_urls={
        "Bug Tracker": "https://github.com/YourUsername/1TamilMV/issues",
        "Documentation": "https://github.com/YourUsername/1TamilMV/docs",
        "Source Code": "https://github.com/YourUsername/1TamilMV",
        "Telegram Channel": "https://t.me/1TamilMV",
        "Telegram Bot": "https://t.me/1TamilMVBot",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Communications :: Chat",
        "Topic :: Multimedia :: Video",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "1tamilmv=main:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
