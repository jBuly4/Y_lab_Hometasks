import ipaddress


def int32_to_ip(int32: int) -> str:
    return ipaddress.ip_address(int32).__str__()


assert int32_to_ip(2154959208) == "128.114.17.104"
assert int32_to_ip(0) == "0.0.0.0"
assert int32_to_ip(2149583361) == "128.32.10.1"
assert int32_to_ip(3222733570) == "192.23.3.2"
