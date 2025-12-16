import twttr

def test_twttr_little_a():
    assert twttr.shorten("cat") == "ct"

def test_twttr_big_a():
    assert twttr.shorten("CAT") == "CT"

def test_twttr_little_e():
    assert twttr.shorten("egg") == "gg"

def test_twttr_big_e():
    assert twttr.shorten("EGG") == "GG"

def test_twttr_little_i():
    assert twttr.shorten("rip") == "rp"

def test_twttr_big_i():
    assert twttr.shorten("RIP") == "RP"

def test_twttr_little_O():
    assert twttr.shorten("cop") == "cp"

def test_twttr_big_o():
    assert twttr.shorten("COP") == "CP"

def test_twttr_little_u():
    assert twttr.shorten("cup") == "cp"

def test_twttr_big_u():
    assert twttr.shorten("CUP") == "CP"

def test_twttr_no_v():
    assert twttr.shorten("RTLP") == "RTLP"

def test_twttr_num():
    assert twttr.shorten("1one") == "1n"

def test_twttr_punct():
    assert twttr.shorten("Hello!") == "Hll!"
