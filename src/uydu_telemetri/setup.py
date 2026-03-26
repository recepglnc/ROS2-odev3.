from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'uydu_telemetri'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # include launch files, otherwise they won't be found
        (os.path.join('share', package_name, 'launch'),
            glob('launch/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Student',
    maintainer_email='student@mail.com',
    description='Satellite telemetry simulation package',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [
            'publisher_node = uydu_telemetri.publisher_node:main',
            'subscriber_node = uydu_telemetri.subscriber_node:main',
        ],
    },
)