from setuptools import setup


readme = open('README.rst').read()

setup(name='drf-related-object-field',
      version='0.0.1',
      description='Customizable primary key related field which allows for id integer input and serializer based rendering.',
      author='Linnify',
      author_email='vlad.rusu@linnify.com',
      url='https://github.com/linnify/drf-related-object-field',
      packages=['drf_related_object_fields'],
      zip_safe=True,
      include_package_date=True,
      license='MIT',
      keywords='drf restframework rest_framework django_rest_framework primary key related field serializers',
      long_description=readme,
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'Topic :: Software Development :: Build Tools',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3.6',
          'Framework :: Django :: 3.1',
      ],
      )
