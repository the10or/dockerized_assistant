from setuptools import setup, find_namespace_packages

setup(name='personal assistant',
      version='1',
      description='Program includes features: address book; notes; sorting files',
      url='https://github.com/Baskina/personal_assistant',
      author='Group',
      author_email='baskina.development@gmail.com',
      license='MIT',
      packages=find_namespace_packages(),
      entry_points={'console_scripts': ['start-bot = src.main:main']},
      )