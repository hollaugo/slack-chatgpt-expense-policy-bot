# Slack ChatGPT Chatbot For PDF Files
A Slack bot that makes it possible for users to chat with documents. 

## Quick Setup

1. Create the required Slack Application:
  
   a. Setup the following bot token scopes:
   
       app_mentions:read
       chat:write
       chat:write.customize
       chat:write.public
       im:history
       im:read
       im:write
       incoming-webhook

   
   b. Retrieve the OAuth Token
   
   c. Enable Socket Mode and enable the following features:

![image](https://github.com/dfcantor/slack-chatgpt-qa-bot/assets/88911560/62910386-aa10-4ef9-b4cd-e870759d1e75)

  d. Generate an App-Level Token, enable the following scopes: 

    connections:write, authorizations:read,app_configurations:write; retrieve the token.

2. Get your OpenAI API token and retrieve it.
3. In the command line, run:

       $ cd <YOUR_PROJECT_PATH>

       $ python -m venv venv

  For Windows systems: 

       $ ./venv/Scripts/activate

  For Unix-based systems:

       $ source venv/bin/activate

  Then install requirements:

       $ pip install -r requirements.txt

4. Replace ABS_Prof_Full.pdf to the PDF of your preference (remember to update the path in both app.py and load_vector.py).
5. Change the path/name of the index in               

       index.storage_context.persist(persist_dir = <YOUR_INDEX_FILE_PATH>
6. Create a file named config.py, where you will load the API keys:

    a. App_Level_Token_Slack

    b. OAuth_Slack_Key1
  
    c. OPENAI_API_KEY

7. Run the scripts

       $ python load_vector.py
       $ python app.py
9. Wait some seconds until the app is initialized
10. Start querying in Slack!
  




## Libraies
- slack_bolt 
- llama_index
- openai
- pypdf2


## Environment variables required 


