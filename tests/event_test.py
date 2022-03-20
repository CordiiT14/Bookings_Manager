import unittest

from models.event import Event

class TestEvent(unittest.TestCase):

    def setUp(self):
        self.event_1 = Event("Loud Poets", "11 April 2022", "18:30", "Spoken Word", "Showcasing the top spoken word talent from Scotland and the UK! From laugh-out-loud funny, through the wonderfully surreal, to the thoughtful and emotional. Loud Poets continue to prove that Spoken Word has something for everyone.")

    # def test_event_name(self):
    #     self.assertEqual("Loud Poets", self.event_1.event_title)