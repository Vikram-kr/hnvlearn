from setuptools import setup, find_packages

setup(
    name='hnvlearn',
    version='0.0.1',
    description='hnvlearn Python library',
    author='hnvlearn',
    author_email='hnv@hnv.com',
    url='https://github.com/Vikram-kr/hnvlearn',
    packages=find_packages(),
    install_requires=[
        'numpy>=1.22.4',
        'pandas>=1.4.4',
        'matplotlib>=3.7.1',
        'scikit-learn>=1.2.2',
        'scipy>=1.10.1',
        'ipython>=7.34.0'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
    ],
)
