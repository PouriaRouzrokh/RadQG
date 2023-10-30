##########################################################################################
# Description: High-level project configurations.
##########################################################################################

from radqg.utils import redirect_path
from radqg.apis import POURIA_OPENAI_API_KEY

# ----------------------------------------------------------------------------------------
# API and token configs
# ----------------------------------------------------------------------------------------

OPENAI_API_KEY = POURIA_OPENAI_API_KEY  # Enter your OpenAI API key here

# ----------------------------------------------------------------------------------------
# Logging configs
# ----------------------------------------------------------------------------------------

VERBOSE = True

# ----------------------------------------------------------------------------------------
# Path configs
# ----------------------------------------------------------------------------------------

TOY_DATA_DIR = redirect_path("data/html_articles")
VECTOR_DB_DIR = redirect_path("data/vector_db")

# ----------------------------------------------------------------------------------------
# LLM arguments
# ----------------------------------------------------------------------------------------

OPENAI_EMBEDDING_MODEL = "text-embedding-ada-002"
OPENAI_QA_GEN_MODEL = "gpt-4"
OPENAI_QA_EDIT_MODEL = "gpt-4"
OPENAI_FORMATTING_MODEL = "gpt-3.5-turbo"

# ----------------------------------------------------------------------------------------
# Retrieval arguments
# ----------------------------------------------------------------------------------------

NUM_RETRIEVED_CHUNKS = 3
CHUNK_SIZE = 4000
CHUNK_OVERLAP = 1000

# ----------------------------------------------------------------------------------------
# GradIO arguments
# ----------------------------------------------------------------------------------------

GR_PORT_NUMBER = 1901
GR_SERVER_NAME = "0.0.0.0"
GR_PUBLIC_SHARE = True
GR_CONCURRENCY_COUNT = 30