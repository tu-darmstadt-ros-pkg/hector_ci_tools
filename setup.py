from distutils.core import setup

setup(
    version='0.0.0',
    scripts=['bin/hector_ci_node'],
    packages=['hector_ci_tools'],
    package_dir={'': 'src'}
)