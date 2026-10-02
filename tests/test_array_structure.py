import unittest

from models import Mahasiswa
from structures.array_structure import ArrayMahasiswa


class TestArrayMahasiswa(unittest.TestCase):

    def setUp(self):
        self.array = ArrayMahasiswa()

        self.mahasiswa_a = Mahasiswa(
            "230001",
            "Andi",
            "Teknik Informatika"
        )

        self.mahasiswa_b = Mahasiswa(
            "230002",
            "Budi",
            "Sistem Informasi"
        )

    def test_array_awalnya_kosong(self):
        self.assertTrue(self.array.is_empty())

    def test_tambah(self):
        self.array.tambah(self.mahasiswa_a)

        self.assertFalse(self.array.is_empty())
        self.assertEqual(self.array.size(), 1)

    def test_cari(self):
        self.array.tambah(self.mahasiswa_a)
        self.array.tambah(self.mahasiswa_b)

        hasil = self.array.cari("230002")

        self.assertIsNotNone(hasil)
        self.assertEqual(hasil.nama, "Budi")

    def test_hapus(self):
        self.array.tambah(self.mahasiswa_a)
        self.array.tambah(self.mahasiswa_b)

        hasil = self.array.hapus("230001")

        self.assertEqual(hasil.nim, "230001")
        self.assertEqual(self.array.size(), 1)


if __name__ == "__main__":
    unittest.main()