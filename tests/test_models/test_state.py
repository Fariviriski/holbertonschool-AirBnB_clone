#!/usr/bin/python3

import unittest
from models.state import State

class TestState(unittest.TestCase):

    def test_state_instance(self):
        """test if state is instance and has correct attr"""
        state = State()
        self.assertIsInstance(state, State)
        self.assertTrue(hasattr(state, "name"))
        self.assertEqual(state.name, "")


if __name__ == '__main__':
    unittest.main()
