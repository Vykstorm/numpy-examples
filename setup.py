
'''
Installation script
'''

from setuptools import setup



if __name__ == '__main__':
    setup(
        name = 'Numpy examples',
        version = '1.0.0',
        description = 'Usage examples of numpy library',
        author = 'Vykstorm',
        author_email = 'victorruizgomezdev@gmail.com',
        python_requires = '>=2.7',
        install_requires = ['numpy'],
        dependency_links = [],
        keywords = ['numpy', 'examples']
    )
