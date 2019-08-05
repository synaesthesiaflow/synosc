"""
utility functions for OSC

MIDI is passed within OSC: http://opensoundcontrol.org/wrapping-other-protocols-inside-osc
  - python_osc docs: https://python-osc.readthedocs.io/en/latest/dispatcher.html
  - OSC spec: http://opensoundcontrol.org/spec-1_0
  - intro to osc: https://www.linuxjournal.com/content/introduction-osc
Notes
  - OSC Address Space: list of all the messages a server understands
  - OSC Schema: OSC Address Space plus the semantics of all the messages
      - Expected argument type(s) for each message
      - Units and allowable ranges for each parameter
      - The effect of each message (with respect to some model of the behavior of the OSC server as a whole)
      - If and how the effects of multiple messages interact

"""

DEFAULT_ADDRESS = "127.0.0.1"
# DEFAULT_PORT = 5005
DEFAULT_PORT = 8000


class OscObject:
    """
  contains an OSC Client, Server, or both
  TODO: not functional, needs work
  """

    SPS = 44100  # Samples per second

    def __init__(self, addr, port):
        self.addr = addr
        self.port = port
