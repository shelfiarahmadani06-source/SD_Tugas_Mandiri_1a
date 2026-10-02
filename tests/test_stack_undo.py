import unittest

from structures.stack_undo import StackUndo


class TestStackUndo(unittest.TestCase):

    def setUp(self):
        self.stack = StackUndo()

    def test_stack_awalnya_kosong(self):
        self.assertTrue(self.stack.is_empty())

    def test_push(self):
        self.stack.push("Aktivitas A")

        self.assertFalse(self.stack.is_empty())
        self.assertEqual(self.stack.peek(), "Aktivitas A")

    def test_pop(self):
        self.stack.push("Aktivitas A")
        self.stack.push("Aktivitas B")

        hasil = self.stack.pop()

        self.assertEqual(hasil, "Aktivitas B")

    def test_lifo(self):
        self.stack.push("Aktivitas A")
        self.stack.push("Aktivitas B")
        self.stack.push("Aktivitas C")

        self.assertEqual(self.stack.pop(), "Aktivitas C")
        self.assertEqual(self.stack.pop(), "Aktivitas B")
        self.assertEqual(self.stack.pop(), "Aktivitas A")


if __name__ == "__main__":
    unittest.main()