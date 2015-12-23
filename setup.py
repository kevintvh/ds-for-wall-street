from setuptools import setup, find_packages

setup(
    name='tsanalysis',
    version='0.0.1',
    author='Sean Owen, Sandy Ryza, Juliet Hougland',
    author_email='sowen@cloudera.com, sryza@cloudera.com, juliet@cloudera.com',
    packages=find_packages(),
    description='Time series analysis of stock ticker and wikipedia pages view data.',
    long_description='Source code to accompany "Data Science for Wall Street" tutorial at Hadoop World NYC 2015',
    install_requires=[
        'scikit-learn==0.17',
        'scipy==0.16.0',
        'sklearn==0.0',
        'sparkts==0.1.0',
        'numpy==1.9.2',
        'matplotlib==1.4.3',
        'seaborn==0.6.0',
        'py4j==0.9',
    ],
)
