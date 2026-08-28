# Alternate file for logger_rate_limiter.py

from logger_rate_limiter import Logger as _BaseLogger

class LoggerAlternate(_BaseLogger):
    """Alternate file for the same problem.

    This keeps the same public API while providing a dedicated
    alternate-file entry for the topic folder.
    """

    pass
