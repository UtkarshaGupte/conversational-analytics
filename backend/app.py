from langchain_community.document_loaders import DuckDBLoader

from langchain_community.llms import Ollama
from langchain_community.embeddings import OllamaEmbeddings
import ollama
from fastapi import FastAPI, Request


import duckdb

MODEL = "llama2"
model = Ollama(model=MODEL)
embeddings = OllamaEmbeddings(model=MODEL)

# from ..scripts import sample-data.csv




app = FastAPI()
@app.post("/chatbot")
async def chatbot_endpoint(request: Request):
    data = await request.json()
    message =  data["message"]
        
    csv_file_path = '/Users/utkarshagupte/Documents/GitHub/conversational-analytics/scripts/sample-data.csv'

    # %%file example.csv
    # Define the query to read and select data from the CSV file
    query =f"SELECT * FROM read_csv_auto('{csv_file_path}')"

    # Create a connection to DuckDB and load the CSV as a virtual table
    con = duckdb.connect(database=':memory:')  # Using an in-memory database
    con.execute(f"CREATE VIEW dataset AS SELECT * FROM read_csv_auto('{csv_file_path}')")

    # Test to see if the data loads correctly
    data = con.execute("SELECT * FROM dataset").fetchdf()
    # print("actual")
    # print(data.head())

    # Get the schema of the dataset
    schema = con.execute("DESCRIBE dataset").fetchdf()
    schema_str = "\n".join([f"CREATE TABLE dataset ({' '.join([f'{col} {dtype}' for col, dtype in row.items()])});" for _, row in schema.iterrows()])

    # Use ollama to generate SQL query
    # prompt = "get all columns ending with _amount from dataset table"

    prompt = message
    r = ollama.generate(
        model='duckdb-nsql:7b-q4_0',
        system=schema_str,
        prompt=prompt,
    )

    # Execute the generated SQL query
    try:
        result = con.execute(r['response']).fetchdf()
        
        # Summarize the result using ollama
        summarize_prompt = f"Summarize the following SQL query result: \n\n{result.to_string()}"
        summary = ollama.generate(
            model='llama2',
            prompt=summarize_prompt,
        )
        # Return the bot's response
        return {"response": summary['response']}
    except Exception as e:
        print(f"Error executing the query: {e}")

    


# ========= Testing =============
# query1 = "show me the scheduled events"
# res1 = llm_with_tools.invoke(query1).tool_calls
# print(res1)

# query2 = "cancel my event at 3pm today"
# res2 = llm_with_tools.invoke(query2).tool_calls
# print(res2)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8888)

