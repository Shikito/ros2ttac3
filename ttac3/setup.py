from setuptools import setup
import os
cur_dir_p = os.path.abspath(os.path.dirname(__file__))
inner_dir_path = os.path.join(cur_dir_p, 'png')

package_name = 'ttac3'

data_files = [
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ]

setup(
    name=package_name,
    version='0.0.0',
    package_dir={'utils' : 'ttac3/utils'},
    packages=[package_name, 'utils'],
    data_files=data_files,
    install_requires=[
        'setuptools',
        'pyautogui',
        'opencv-python',
        'python-xlib',
        'PyYAML'],
    zip_safe=True,
    maintainer='shikito',
    maintainer_email='shikito.aos@gmail.com',
    description='Control library for TTA_C3',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'server = ' + package_name + '.ttac3_action_server:main',
            'client = ' + package_name + '.ttac3_action_client:main',
        ],
    },
)
