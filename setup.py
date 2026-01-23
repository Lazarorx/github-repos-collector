"""Setup configuration for GitHub Repos Collector."""
from setuptools import setup, find_packages
from pathlib import Path

# Read the contents of README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf-8')

setup(
    name='github-repos-collector',
    version='2.4.0',
    author='GitHub Repos Collector Contributors',
    author_email='',
    description='A powerful tool to collect, filter, and export GitHub repository information',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/github-repos-collector',
    py_modules=['app'],
    python_requires='>=3.7',
    install_requires=[
        'requests>=2.31.0',
        'click>=8.1.7',
        'tqdm>=4.66.0',
        'rich>=13.7.0',
    ],
    extras_require={
        'dev': [
            'pytest>=7.4.0',
            'pytest-cov>=4.1.0',
            'black>=23.0.0',
            'flake8>=6.0.0',
            'isort>=5.12.0',
        ],
    },
    entry_points={
        'console_scripts': [
            'github-repos-collector=app:main',
            'grc=app:main',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Operating System :: OS Independent',
        'Environment :: Console',
        'Natural Language :: English',
    ],
    keywords='github api repository search filter export csv json cli',
    project_urls={
        'Bug Reports': 'https://github.com/yourusername/github-repos-collector/issues',
        'Source': 'https://github.com/yourusername/github-repos-collector',
        'Documentation': 'https://github.com/yourusername/github-repos-collector/tree/main/docs',
    },
)
