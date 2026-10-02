import unittest

from models import Mahasiswa
from structures.queue_processing import QueueProcessing


class TestQueueProcessing(unittest.TestCase):

    def setUp(self):
        self.queue = QueueProcessing()

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

    def test_queue_awalnya_kosong(self):
        self.assertTrue(self.queue.is_empty())

    def test_enqueue(self):
        self.queue.enqueue(self.mahasiswa_a)

        self.assertFalse(self.queue.is_empty())
        self.assertEqual(self.queue.size(), 1)

    def test_dequeue(self):
        self.queue.enqueue(self.mahasiswa_a)

        hasil = self.queue.dequeue()

        self.assertEqual(hasil.nim, "230001")

    def test_fifo(self):
        self.queue.enqueue(self.mahasiswa_a)
        self.queue.enqueue(self.mahasiswa_b)

        hasil_pertama = self.queue.dequeue()
        hasil_kedua = self.queue.dequeue()

        self.assertEqual(hasil_pertama.nim, "230001")
        self.assertEqual(hasil_kedua.nim, "230002")


if __name__ == "__main__":
    unittest.main()