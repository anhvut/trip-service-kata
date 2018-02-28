import unittest

from UserSession import UserSession

class UserSessionTest(unittest.TestCase):

  def testUserSessionSingleton(self):
    userSession1 = UserSession()
    userSession2 = UserSession()
    print(userSession1)
    print(userSession2)
    self.assertEqual(str(userSession1), str(userSession2))
    self.assertEqual(userSession1, userSession2)


if __name__ == '__main__':
  unittest.main()
