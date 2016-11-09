from setuptools import setup

setup(
    name='facenet',
    version='1.0',
    packages=['facenet', 'mtcnn_align'],
    package_data={'mtcnn_align': ['../data/*.npy']},
    url='git@github.com:alfiya400/facenet.git',
    license='',
    author='alfiya400',
    author_email='',
    description='FaceNet implementation in Tensorflow'
)
