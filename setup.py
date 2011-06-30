from setuptools import setup, find_packages

setup(
    name='nous.testbrowser',
    version='0.1.0',
    description='Nous testbrowser goodies.',
    author='Ignas Mikalajunas',
    author_email='ignas@nous.lt',
    url='http://github.com/Ignas/nous.testbrowser/',
    classifiers=["Development Status :: 3 - Alpha",
                 "Environment :: Web Environment",
                 "Intended Audience :: Developers",
                 "License :: OSI Approved :: GNU General Public License (GPL)",
                 "Programming Language :: Python"],
    install_requires=[
        'setuptools',
        'lxml',
        'webtest',
        'zope.testbrowser'],
    package_dir={'': 'src'},
    packages=find_packages('src'),
    namespace_packages=['nous'],
    include_package_data=True,
    zip_safe=False,
    license="GPL"
)
