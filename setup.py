import setuptools
import os.path

import add

app_path = os.path.dirname(add.__file__)

with open(os.path.join(app_path, 'resources', 'README.md')) as f:
      long_description = f.read()

with open(os.path.join(app_path, 'resources', 'requirements.txt')) as f:
      install_requires = map(lambda s: s.strip(), f)

setuptools.setup(
      name='awsdyndns',
      version=add.__version__,
      description="An AWS (Route53)-based dynamic DNS client.",
      long_description=long_description,
      classifiers=[],
      keywords='aws r53 route53 boto dyndns dns client',
      author='Dustin Oprea',
      author_email='myselfasunder@gmail.com',
      url='https://github.com/dsoprea/AwsDynDns',
      license='GPL 2',
      packages=setuptools.find_packages(exclude=[]),
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      package_data={
            'add': ['resources/scripts/*', 
                    'resources/README.md',
                    'resources/requirements.txt'],
      },
      scripts=[
            'rpipe/resources/scripts/add_update',
      ],
)