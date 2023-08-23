# A very important file that sets the environment variable to TEST
# when running tests through pytest.

import os

os.environ["MODE"] = "TEST"