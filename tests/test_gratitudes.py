from lib.gratitudes import Gratitudes

def test_show_gratititude():
    gratitiude = Gratitudes()
    gratitiude.add("family")
    assert "family" in gratitiude.gratitudes