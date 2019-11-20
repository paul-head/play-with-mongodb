import mongoengine


def global_init():
    mongoengine.register_connection(alias='core', name='demo_dealership')

#  init for dealership db
def dealership_init():
    mongoengine.register_connection(alias='dealership', name='dealership')