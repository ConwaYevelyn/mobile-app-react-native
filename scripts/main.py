import os
from mobile_app_react_native.config import Config
from mobile_app_react_native.utils import check_environment

def main():
    # Check environment variables
    check_environment()

    # Load configuration
    config = Config()

    # Set up logging
    import logging
    logging.basicConfig(level=config.log_level)
    logger = logging.getLogger(__name__)

    # Start the application
    try:
        from mobile_app_react_native.app import App
        app = App(config)
        app.run()
    except Exception as e:
        logger.error(f"Error starting application: {e}")
        raise

if __name__ == "__main__":
    main()