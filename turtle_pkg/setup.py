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
            "turtle_controller=turtle_pkg.turtle_controller:main",
            "draw_circle=turtle_pkg.draw_circle:main",
            "pose_node=turtle_pkg.pose_node:main",
            "turtle_nav=turtle_pkg.turtle_nav:main",
            "turtle_move=turtle_pkg.turtle_move:main"
        ],
    },
)
