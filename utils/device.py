import logging

import torch

logger = logging.getLogger(__name__)


def get_device(preference: str = "auto") -> torch.device:
    """Return a torch device based on *preference* ('auto', 'cpu', 'cuda')."""
    if preference == "auto":
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    elif preference == "cuda":
        if torch.cuda.is_available():
            device = torch.device("cuda")
        else:
            logger.warning("CUDA requested but not available — falling back to CPU")
            device = torch.device("cpu")
    else:
        device = torch.device("cpu")

    logger.info("Using device: %s", device)
    return device
