from groq import Groq
from settings import GROQ_API_KEY
from settings import PINECONE_API_KEY
import sys
from vector import search_similar

client = Groq(api_key=GROQ_API_KEY)

class ChatSession:
  def __init__(self, client, model="meta-llama/llama-4-scout-17b-16e-instruct"):
    self.client = client
    self.model = model
    self.messages = []

  def add_user_message(self, content):
    self.messages.append({"role": "user", "content": content})

  def add_assistant_message(self, content):
    self.messages.append({"role": "assistant", "content": content})

  def chat(self, msg, temperature=1, max_completion_tokens=1024, top_p=1, stream=True, stop=None):
    context = search_similar(msg, top_k=3, debug=False)
    self.add_user_message(msg + 'Context: ' + ' '.join(context))
    
    completion = self.client.chat.completions.create(
      model=self.model,
      messages=self.messages,
      temperature=temperature,
      max_completion_tokens=max_completion_tokens,
      top_p=top_p,
      stream=stream,
      stop=stop
    )
    response = ""
    for chunk in completion:
      delta = chunk.choices[0].delta.content or ""
      print(delta, end="")
      response += delta
    self.add_assistant_message(response)
    print()  # For newline after response


if __name__ == "__main__":
    session = ChatSession(client)
    try:
        while True:
            msg = input("You: ")
            if msg.lower() in ["exit", "quit"]:
                break
            session.chat(msg)
            print()  # For better readability
    except KeyboardInterrupt:
        print("\nNos vemos la proxima.")
        sys.exit(0)
