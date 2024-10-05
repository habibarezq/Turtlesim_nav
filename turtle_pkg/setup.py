from setuptools import find_packages, setup

package_name = 'turtle_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='habiba-rezq',
    maintainer_email='habibarezq30@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [ 
            "turtle_controller=pkg_py.turtle_controller:main",
            "draw_circle=pkg_py.draw_circle:main",
            "pose_node=pkg_py.pose_node:main",
            "turtle_nav=pkg_py.turtle_nav:main",
            "turtle_move=pkg_py.turtle_move:main"
        ],
    },
)
