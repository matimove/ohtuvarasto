"""Auttaa unittestien tekemisessä"""
import unittest
from varasto import Varasto
class TestVarasto(unittest.TestCase):
    """Toteuttaa testit varastoluokalle"""
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        """Testaa konstruktoria"""
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        """Testaa tilavuuden toiminnan"""
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        """Testaa lisäyksen"""
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        """Testaa lisäystä"""
        self.varasto.lisaa_varastoon(8)
        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        """Testaa ottamista ja määrää"""
        self.varasto.lisaa_varastoon(8)
        saatu_maara = self.varasto.ota_varastosta(2)
        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        """Testaa ottamista"""
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(2)
        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_virheellinen_tilavuus_nollataan(self):
        """Testaa virheellistä tilavuutta"""
        self.varasto = Varasto(-2,-2)
        self.assertEqual(self.varasto.paljonko_mahtuu(), 0.0)

    def test_konstruktori_hukkaa_ylimaaraisen_saldon(self):
        """Testaa ylimääräistä saldoa"""
        self.varasto = Varasto(2,4)
        self.assertEqual(self.varasto.paljonko_mahtuu(), 0.0)

    def test_negatiivinen_lisays_ei_vaikuta(self):
        """Testaa negatiivista lisäystä"""
        self.varasto.lisaa_varastoon(-8)
        self.assertEqual(self.varasto.paljonko_mahtuu(), 10)

    def test_ylimaarainen_saldo_lisays_hukkaan(self):
        """Testaa ylimääräistä saldoa"""
        self.varasto.lisaa_varastoon(12)
        self.assertEqual(self.varasto.paljonko_mahtuu(), 0)

    def test_otetaan_negatiivinen_luku_saldosta(self):
        """Testaa negatiivisen luvun ottamista"""
        self.varasto.lisaa_varastoon(6)
        self.varasto.ota_varastosta(-2)
        self.assertEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_otetaan_kaikki_mita_voidaan_saldosta(self):
        """Testataan kaiken ottamista"""
        self.varasto.lisaa_varastoon(6)
        self.varasto.ota_varastosta(7)
        self.assertEqual(self.varasto.paljonko_mahtuu(), 10)

    def test_tulostus_nakyy_oikein(self):
        """Testataan tulostusta"""
        self.varasto.lisaa_varastoon(6)
        self.assertEqual(str(self.varasto), "saldo = 6, vielä tilaa 4")
