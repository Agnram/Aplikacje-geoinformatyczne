from ..utils.get_logger import get_logger

logger = get_logger(__name__)


def example_for_logging():
    logger.warning("To jest treść warning")
    logger.error("To jest error")
    logger.debug("To jest tylko informacja dla debugowania")

    logger.error("WHAAAAAAAAAAAAAAT222222222222222222")