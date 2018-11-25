ttl = 600

def pingsweep(ip_addr):
    print("Performing ping sweep with TTL {}".format(ttl))

def set_ttl(ttl_value):
    global ttl
    ttl = ttl_value