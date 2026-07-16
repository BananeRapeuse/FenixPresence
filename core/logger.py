from pathlib import Path
import logging


LOG_DIR.mkdir(
    exist_ok=True
)



LOG_FILE = LOG_DIR / "fenixpresence.log"



logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    encoding="utf-8"
)



logger = logging.getLogger(
    "FenixPresence"
)