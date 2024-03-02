# Configure the logging module
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(funcName)s:  %(lineno)d - %(message)s  : %(name)s",
    handlers=[
        logging.StreamHandler()
        # Add other handlers as needed, e.g., logging.FileHandler("logfile.log")
    ],
)
