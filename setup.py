from setuptools import setup
setup(
   name='dis3',
   version='2.0',
   description='tools for disassembling and reassembling python code',
   author='kapten-kaizo',
   author_email='cyber2687@gmail.com',
   packages=['dis3'],
   entry_points={"console_scripts": ["dis3=dis3:main"]}
)
