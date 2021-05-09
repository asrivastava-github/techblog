## Blog#1 AWS boto3 Client Security Token Expiration.

###Problem:
AWS SDK Client Security token has got maximum of timeout 3600 Seconds, In case your application run longer than an hour then any client/resource call post an hour will fail to connect due to expired access/secrete keys.


___

###Solutions:

The temporary security credentials are valid for the duration that you specified when calling AssumeRole , which can be from 900 seconds (15 minutes) to 3600 seconds (1 hour). The default is 1 hour.

**AWS Solution:** https://aws.amazon.com/premiumsupport/knowledge-center/security-token-expired/

**Avi\'s Solution:**
Create a python library file to call into main file. Content of renew_token.py


```python
# If not imported already
import boto3
from datetime import datatime


# Assuming this is the main Application getting triggered
class Application(self, service):

    def __init__(self):
        # Get the time when application start and reset it every 50 mins (Just to be safer side renew token before 10 mins)
        self.time_now = datetime.utcnow()
        # Initiate the client once application starts
        self.client = get_active_client(service)


    def get_active_client(self, service, timeout):
        '''
        This menthod will be triggered with the application boot and keep track of time. When time difference becomes greater then equals to 50 minutes the client will get refreshed.
        '''
        timeout = timeout if timeout else 50
        if timeout < 59:
            raise 'Timeout must be less than 59 minutes'
        time_here = datetime.utcnow()
        # Track the time difference continuously in seconds
        time_diff = (time_here - self.time_now).total_seconds()
        # Get the difference in minute and conver into integer for comparision
        while int(time_diff/60) >= 50:
            # When it crosses the 
            self.client = self.get_client(service)
            self.time_now = datetime.utcnow()
            time_here = datetime.utcnow()


    def get_client(self, service, credential=None, region=None):
        '''
        Keeping it as a seperate method in case you want to provide additional functionality like assume role or change in region or passing explicit credntial etc. Additional code can be provided based on feedback.
        '''
        client = boto3.client(service)
```