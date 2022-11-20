from mipaquete.string import minusculas, mayusculas

def test_minusculas():
    assert minusculas("AaáÁäÄàÀâÂ") == "aaááääààââ"

def test_mayusculas():
    assert mayusculas("AaáÁäÄàÀâÂ") == "AAÁÁÄÄÀÀÂÂ"