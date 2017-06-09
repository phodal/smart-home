import broadlink

devices = broadlink.discover(timeout=50)

print devices
