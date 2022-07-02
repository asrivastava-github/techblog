# token_refresh.py
import boto3
from botocore.config import Config
from datetime import datetime


# Assuming this is the main Application getting triggered
class Application:

    def __init__(self, service:str, client_timeout:int=None):
        """
        :param service: AWS Service name for which client needs to be created as a String
        :param client_timeout: timeout as an integer within which you are looking to refresh the token, by default it
        will be set to 3580
        """
        # Get the time when application start and reset it every 3580 seconds (Just to be safer side renew token 20
        # seconds early)
        self.service = service
        self.timeout = int(client_timeout) if client_timeout else 3580
        if self.timeout > 3580:
            raise Exception('Timeout must be less than 3580 Seconds')

        self.init_time = datetime.utcnow()
        self.client_config = Config(retries={'max_attempts': 1})

        # Instantiate the client once application starts. It could be one or many
        self.client = self.get_client()
        # Below function will make sure it's active post the defined timeout
        self.get_active_client()

    def get_active_client(self):

        """
        This method will be triggered with the application init and keep track of time. When time difference becomes
        greater than to 3580 seconds (by default) or timeout value you will pass, client will get refreshed.
        """
        # get the current time
        time_now = datetime.utcnow()

        # get the time difference between current and when app was started
        time_diff = (time_now - self.init_time).seconds

        while self.timeout > int(time_diff):
            # keep track of current time
            time_now = datetime.utcnow()
            # Track the time difference continuously in seconds
            time_diff = (time_now - self.init_time).seconds
        else:
            print('Refreshing client after {} seconds'.format(time_diff))
            self.init_time = datetime.utcnow()
            self.client = self.get_client()
            self.get_active_client()

    def get_client(self):

        """
        Keeping it as a separate method in case you want to provide additional functionality like assume role or change
        in region or passing explicit credential etc. Additional code can be provided based on feedback.
        """

        return boto3.client(self.service, config=self.client_config)


if __name__ == '__main__':
    # I am taking an example of s3 client
    app_instance = Application(service='s3')
