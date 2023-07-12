# Libary Modules needed for this script: slack_bolt, os, json, llama_index, openai
import json
import os

import config
import openai
from llama_index import (
    LLMPredictor,
    ServiceContext,
    SimpleDirectoryReader,
    StorageContext,
    VectorStoreIndex,
    load_index_from_storage,
)
from llama_index.llms import OpenAI
from llama_index.prompts import Prompt
from llama_index.query_engine import CitationQueryEngine
from llama_index.retrievers import VectorIndexRetriever
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# Define OpenAI API key
openai.api_key = config.OPENAI_KEY

# Initialize Slack App with the provided bot token
app = App(token=config.OAuth_Slack_Key1)


# Load the GPT index from disk

from llama_index import StorageContext, load_index_from_storage

# rebuild storage context
storage_context = StorageContext.from_defaults(
    persist_dir=r"C:\Users\DanielCantorBaez\Documents\SyncierGPT\slack-chatgpt-qa-bot\abs-prof-index"
)


# Create a service context for the OpenAI model
service_context = ServiceContext.from_defaults(
    llm=OpenAI(model="gpt-3.5-turbo", temperature=0)
)

# load index
index = load_index_from_storage(
    StorageContext.from_defaults(
        persist_dir=r"C:\Users\DanielCantorBaez\Documents\SyncierGPT\slack-chatgpt-qa-bot\abs-prof-index"
    ),
    service_context=service_context,
)


# Listens to any incoming messages
@app.message("")
def message_all(message, say):
    # Print the incoming message text
    print(message["text"])

    # Query the index with the message text and get a response
    text = message["text"]
    query_engine = CitationQueryEngine.from_args(
        index,
        similarity_top_k=3,
        citation_chunk_size=1024,
    )

    response = query_engine.query(text)

    # Extract the desired message and sources from the response object
    message = str(response)  # Convert the 'Response' object to a string
    # sources = json.dumps(response.get_formatted_sources(length=100))

    # Print the message and sources and send them as a message back to the user
    print(message)
    # print(sources)
    say(message)

    print(response.source_nodes[0].node.get_text())


# Responds to mentions


@app.event("app_mention")
def event_test(body):
    event = body.get(
        "event", {}
    )  ## Gets the dictionary with the event variables via a GET API request

    print(event)

    # Get and Print the incoming message text

    text = get_text(event)
    print(text)

    user_id = event.get("user")  ## Gets user id from current event
    channel_id = event.get("channel")  ## Gets current event channel
    ts = event.get("ts")  ## Gets the timestamp from the event

    # Query the index with the message text and get a response
    query_engine = index.as_query_engine()
    response = query_engine.query(text)

    # Extract the desired message and sources from the response object
    message = (
        f"<@{user_id}>: \n {str(response)}"  # Convert the 'Response' object to a string
    )

    app.client.chat_postMessage(channel=channel_id, thread_ts=ts, text=message)


def get_text(data: dict) -> str:
    for block in data["blocks"]:
        if block["type"] == "rich_text":
            for element in block["elements"]:
                if element["type"] == "rich_text_section":
                    for sub_element in element["elements"]:
                        if sub_element["type"] == "text":
                            return sub_element["text"]

    text = get_text(data)
    return text


# Start the Socket Mode handler
if __name__ == "__main__":
    SocketModeHandler(app, config.App_Level_Token_Slack).start()
