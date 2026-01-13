import os
import logging
from typing import Dict, List, Tuple

def get_environment_variables() -> Dict[str, str]:
    return dict(os.environ)

def setup_logging(log_level: int = logging.INFO) -> None:
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=log_level
    )

def parse_query_params(query_string: str) -> Dict[str, List[str]]:
    params = {}
    for param in query_string.split('&'):
        key, value = param.split('=')
        if key in params:
            params[key].append(value)
        else:
            params[key] = [value]
    return params

def validate_api_response(response: Dict[str, any]) -> Tuple[bool, str]:
    if 'error' in response:
        return False, response['error']
    return True, ''

# setup_logging()
# logging.info('Logging setup complete')