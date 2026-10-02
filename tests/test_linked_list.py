import unittest
from models import Mahasiswa
from structures.linked_list import LinkedListMahasiswa


class TestLinkedListMahasiswa(unittest.TestCase):

    def setUp(self):
        self.linked_list = LinkedListMahasiswa()

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

    def test_linked_list_awalnya_kosong(self):
        self.assertTrue(self.linked_list.is_empty())

    def test_tambah(self):
        self.linked_list.tambah(self.mahasiswa_a)

        self.assertFalse(self.linked_list.is_empty())
        self.assertEqual(self.linked_list.size(), 1)

    def test_cari(self):
        self.linked_list.tambah(self.mahasiswa_a)
        self.linked_list.tambah(self.mahasiswa_b)

        hasil = self.linked_list.cari("230002")

        self.assertIsNotNone(hasil)
        self.assertEqual(hasil.nama, "Budi")

    def test_hapus(self):
        self.linked_list.tambah(self.mahasiswa_a)
        self.linked_list.tambah(self.mahasiswa_b)

        hasil = self.linked_list.hapus("230001")

        self.assertEqual(hasil.nim, "230001")
        self.assertEqual(self.linked_list.size(), 1)


if __name__ == "__main__":
    unittest.main()