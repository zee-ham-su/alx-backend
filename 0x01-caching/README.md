# 0x01 Caching

This directory contains code and documentation related to caching in software development.

## Table of Contents

- [Introduction](#introduction)
- [Resources](#Resources)
- [Learning Objectives](#Learning Objectives)
- [Requirements](#Requirements)


## Introduction

In this directory, you will find examples and explanations of caching techniques and their importance in software development. Caching can greatly improve the performance and efficiency of applications by storing frequently accessed data in a faster and more accessible location.

## Resources
- Read or watch:
- [Cache replacement policies - FIFO] https://intranet.alxswe.com/rltoken/fjhr6EvFeF3mWwsPQXUKdQ
- [Cache replacement policies - LIFO] https://intranet.alxswe.com/rltoken/U44RQjXp8xBtsbNIyhHIyw
- [Cache replacement policies - LRU] https://intranet.alxswe.com/rltoken/gKerxvR4dnXQYkBX2ujZiQ
- [Cache replacement policies - MRU] https://intranet.alxswe.com/rltoken/Tmk4qEBZ7QTknvbpKabWfQ
- [Cache replacement policies - LFU] https://intranet.alxswe.com/rltoken/8PEJ8L34bxhL2y--BW5zGQ


## Learning Objectives

- At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
- General
    - What a caching system is
    - What FIFO means
    - What LIFO means
    - What LRU means
    - What MRU means
    - What LFU means
    - What the purpose of a caching system
    - What limits a caching system have

## Requirements

- Python Scripts
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/env python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle style (version 2.5)
- All your files must be executable
- The length of your files will be tested using wc
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

## More Info
## Parent class BaseCaching
- All your classes must inherit from BaseCaching defined below:
- $ cat base_caching.py

#!/usr/bin/python3


""" BaseCaching module
"""

class BaseCaching():
    
    
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    
    MAX_ITEMS = 4

    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError("get must be implemented in your cache class")