from setuptools import find_packages, setup

setup(
    name='simfy_health',
    version='0.0.1',
    description='Simfy Africa Health',
    url='https://github.com/simfy-africa/health.git',
    author='Simfy Africa',
    author_email='info@simfyafrica.com',
    packages=find_packages(),
    install_requires=['flask'],
    zip_safe=False
)
