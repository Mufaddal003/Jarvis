from utils.logger import setup_logger

logger = setup_logger()

def start_jarvis():
    logger.info("=" * 60)
    logger.info("Starting Jarvis AI OS")
    logger.info("=" * 60)

    from backend.brain import JarvisBrain

    jarvis = JarvisBrain()
    jarvis.start()