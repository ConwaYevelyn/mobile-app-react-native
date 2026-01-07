import os
from mobile_app_react_native.config import Config
from mobile_app_react_native.utils import logger

class MobileAppReactNative:
    def __init__(self):
        self.config = Config()
        self.logger = logger.get_logger(__name__)

    def run(self):
        try:
            self.logger.info("Mobile App React Native started")
            self.config.load_config()
            self.logger.info("Config loaded successfully")
        except Exception as e:
            self.logger.error(f"Error occurred: {str(e)}")
            raise

if __name__ == "__main__":
    app = MobileAppReactNative()
    app.run()