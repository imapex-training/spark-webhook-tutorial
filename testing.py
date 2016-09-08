import os
import app
import unittest
import tempfile

SAMPLE_REQUEST = {
  "filter": "roomId=Y2lzY29zcGFabcdeL3VzL1JPT00vNzYyZmMzOTAtNzA1ZC0xMWU2LTllZDItZDVmNDNhNDI2ZmFi",
  "actorId": "Y2lzY29zcGFabcdeL3VzL1BFT1BMRS82Njk3ZDE1ZC1hYTA0LTQ3ZmMtYWU5Mi1hZWQ0NWRlYjc5N2U",
  "resource": "messages",
  "name": "webhook",
  "created": "2016-09-01T16:05:15.158Z",
  "targetUrl": "http://54.152.28.194/api/spark",
  "data": {
    "roomType": "group",
    "created": "2016-09-01T17:57:26.111Z",
    "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS82Njk3ZDE1ZC1hYTA0LTQ3ZmMtYWU5Mi1hZWQ0NWRlYjc5N2U",
    "personEmail": "someone@cisco.com",
    "roomId": "Y2lzY29zcGFabcdeL3VzL1JPT00vNzYyZmMzOTAtNzA1ZC0xMWU2LTllZDItZDVmNDNhNDI2ZmFi",
    "id": "Y2lzY29zcGFabcdeL3VzL01FU1NBR0UvOGFhM2I2ZjAtNzA2ZC0xMWU2LTk3YTMtM2IwZmE1NDcxNTEx"
  },
  "id": "Y2lzY29zcGFyadafsdfL3VzL1dFQkhPT0svNWIxNTU2MTMtNTJiMS00M2YxLWIxNjUtOGM0OTgzMjZhZTcx",
  "event": "created"
}


class APITestCases(unittest.TestCase):

    def setUp(self):
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()


    def test_post(self):
        rv = self.app.post('/api/spark', data=SAMPLE_REQUEST)
        print rv
        #assert b'No entries here so far' in rv.data


    def tearDown(self):
        pass
        #os.close(self.db_fd)
        #os.unlink(flaskr.app.config['DATABASE'])

if __name__ == '__main__':
    unittest.main()
