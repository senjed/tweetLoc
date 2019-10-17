from setuptools import setup , find_packages 
#setup(name = "tweetLoc", version = "1.0", packages = ["tweetLoc", "tweetLoc.data", "tweetLoc.cooc" ], packages_dir = {'tweetLoc':"tweetLoc", 'tweetLoc.data':"tweetLoc/data"})
setup(name = "tweetLoc", version = "1.0", packages = find_packages())
