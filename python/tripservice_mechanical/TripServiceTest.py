import unittest

from TripService import TripService
from User import User

class TripServiceTest(unittest.TestCase):

  def testTripServiceWithDefaultUser(self):
    user = User()
    tripService = TripService()
    result = tripService.getTripsByUser(user)
    print(result)
    self.assertIsNotNone(result)

if __name__ == '__main__':
  unittest.main()
