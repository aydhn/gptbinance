from app.core.bootstrap import bootstrap
from app.telegram.notifier import get_notifier

def main():
    config, ctx = bootstrap()

    # Initialize core components here in the future
    notifier = get_notifier(config)
    notifier.send_message(f"Application started in {ctx.profile.value} mode. Run ID: {ctx.run_id}")

    import logging
    logger = logging.getLogger(__name__)
    logger.info("Main execution block reached. Exiting gracefully.")

if __name__ == "__main__":
    main()
