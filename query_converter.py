from openai import OpenAI
import json

client = OpenAI()


#can force user to click on a button like perplexity.... makes sense
#that's an option

glossary = """

SG means Singapore
CS means Cold Storage

"""

#for each collection

intention = """

The user who asks this question is interested in understanding cold storage market.  They are an investor who will need to collect data to understand whether a market is attractive.  They are interested in cap rates, pallet rates, new supply, demand, investments.  Considering their intention, improve their prompt"

"""

def humanize_prompt(user_input, chat_id):
    print(f"This is the initial prompt: {user_input}")
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role": "system", "content": f"You are an assistant that helps improve user queries. Users are occasionally lazy and do not write a detailed prompt.  Your job is to take their prompt, which could be written with bad grammer or with wrong wording, and convert it into something coherent and that makes sense.  To help you, you can find glossary of words here, which can help you associate abbreviations with the right words {glossary}. Do not ask back the user if it's not clear what they really ask, in next steps we'll figure it out.  Your only job is to take the current input and make sense out of it as best as you can, and write it in a more structured, clean and logical way"},
            {"role": "user", "content": user_input}
        ]
    )
    improved_query = response.choices[0].message.content.strip()
    print(improved_query)
    return improved_query



#maybe it needs to know the documents, and their one sentence summary or keywords
#to be able to improve the query.......
#it's not mixing the document sources.



def improve_prompt(user_input, chat_id):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role": "system", "content": "You are an assistant that helps improve user queries. Take the user's input and convert it into a more refined and effective query that can help you reach to a larger set of vector embeddings, thus improving the answer. Ensure that the new query requies use of data, sources, examples and real world developments.  Ensure that query prompts LLM to give source for the information, e.g. the name of the source document"},
            {"role": "user", "content": f"This is the user input: {user_input}.  This is the intention of the user: {intention}"}
        ]
    )
    improved_query = response.choices[0].message.content.strip()
    print(improved_query)
    return improved_query



#maybe it needs to know the documents, and their one sentence summary or keywords
#to be able to improve the query.......
#it's not mixing the document sources.


with open('sample_query.json', 'r') as file:
    sample_json = json.load(file)


def expand_and_improve_prompt(user_input, chat_id):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        response_format={ "type": "json_object" },
        messages=[
            {"role": "system", "content": f"You are an assistant that helps improve user queries. Take the user's input and convert it into five more refined and effective queries that can help you reach a larger set of vector embeddings. When we say refine and improved, what we mean is you figure out an idea in the existing prompt, pick that, and rewrite that as an individual prompt but in a more comprehensive and expanded way.  Remember goal is to make sure that we take 1 query, and turn that into more extensive 5 queries so taht we reach to higher quality information Realize that the prompt user puts will go to a single document most likely, our goal is to go to more varied sources so that we combine information from multiple sources. This is the JSON structure I want from you: {sample_json}. So write 5 prompts as questions and their focuses (you can write multiple focuses, these are keywords that you want to look at in the vector database) such that they do not overlap and they do not bring the same chunks from the vector database, but they are still relevant to each other. Ensure the JSON structure is clean."},
            {"role": "user", "content": user_input}
        ]
    )
    improved_queries = response.choices[0].message.content.strip()
    print(improved_queries)
    
    # Save the improved queries to a JSON file
    with open('query_expansion.json', 'w') as file:
        json.dump(improved_queries, file, indent=4)
    
    return improved_queries



with open('query_expansion.json', 'r') as file:
        queries_data = json.load(file)
  




#burada kodu duzgun yazacagiz yani tum pdf'leri falan process edip atomice ekleyecegiz
#sonra 5 tane prompt yollayacagiz.  chunklar gelecek.  En son onu llama indexteki ayni sisteme koyacagiz


def query_expansion(user_input, chat_id):
        # Loop through each query and focus, and send it to the OpenAI API
    for query_info in queries_data['queries']:
        for query, focus in query_info.items():
            print(f"Sending query: {query} with focus: {focus}")
            response = client.chat.completions.create(
                model="gpt-3.5-turbo-0125",
                messages=[
                    {"role": "system", "content": "You are a senior associate at an investment bank who is responsible for doing market research and sending detailed, succinct and professional memos on various investment topics.  Your output is a well organized and structured memo that is clear and concise.  You do not need to write this is a memo or a title at the top of your writing, just start with a short note as you would in an email memo and go onto your bulelt point note"},
                    {"role": "user", "content": query}
                ]
            )
            detailed_response = response.choices[0].message.content.strip()
            print(f"Response for {query}: {detailed_response}")
    
    return improved_queries



step1 = humanize_prompt("Summarize SG CS market", "1234")
step2 = improve_prompt(step1, "1234")
step3 = expand_and_improve_prompt(step2, "1234")