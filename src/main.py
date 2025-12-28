import os
from mobile_app_react_native import app_config, services

def main():
    # Initialize application configuration
    config = app_config.init_config()
    
    # Set up logging
    logging_config = config['logging']
    logging.basicConfig(level=logging_config['level'], format=logging_config['format'])
    
    # Initialize services
    services.init_services(config)
    
    # Start the application
    from mobile_app_react_native.app import App
    app = App(config)
    app.run()

if __name__ == '__main__':
    main()