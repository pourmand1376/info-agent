"""A templated Fixie agent!

Fixie docs:
    https://docs.fixie.ai

Fixie agent example:
    https://github.com/fixie-ai/fixie-examples
"""

import fixieai
import requests


BASE_PROMPT = """This module will receive data from a site and do any query with it. """

FEW_SHOTS = """
Q: How much RAM memory does this product have? https://www.amazon.com/Apple-MacBook-13-inch-256GB-Storage/dp/B08N5KWB9H/ref=sr_1_1?keywords=macbook&qid=1682770022&sr=8-1&th=1
Ask Func[get_info]: https://www.amazon.com/Apple-MacBook-13-inch-256GB-Storage/dp/B08N5KWB9H/ref=sr_1_1?keywords=macbook&qid=1682770022&sr=8-1&th=1
Func[get_info] says: #doc1
A: 8 GB

Q: What is the hard disk space for this product? https://www.amazon.com/Apple-MacBook-13-inch-256GB-Storage/dp/B08N5KWB9H/ref=sr_1_1?keywords=macbook&qid=1682770022&sr=8-1&th=1
Ask Func[get_info]: https://www.amazon.com/Apple-MacBook-13-inch-256GB-Storage/dp/B08N5KWB9H/ref=sr_1_1?keywords=macbook&qid=1682770022&sr=8-1&th=1
Func[get_info] says: #doc1
A: 256 GB
"""
agent = fixieai.CodeShotAgent(BASE_PROMPT, FEW_SHOTS)


@agent.register_func
def get_info(query: fixieai.Message) -> str:
    url = query.text
    response = requests.get(url)
    content_type = response.headers["Content-Type"]
    return fixieai.Message("#doc1", embeds={"doc1": fixieai.Embed(content_type, url)})

