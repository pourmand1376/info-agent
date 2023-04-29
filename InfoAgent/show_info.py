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
Q: What are top asked questions for this product? https://www.amazon.com/Apple-MacBook-13-inch-256GB-Storage/dp/B08N5KWB9H/ref=sr_1_1?keywords=macbook&qid=1682770022&sr=8-1&th=1
Ask Func[get_info]: https://www.amazon.com/Apple-MacBook-13-inch-256GB-Storage/dp/B08N5KWB9H/ref=sr_1_1?keywords=macbook&qid=1682770022&sr=8-1&th=1
Func[get_info] says: #doc1
A: How do I get this in 16gb ram, can a wireless mouse be used with this mac?, Can you use it with a 4K external monitor?

Q: What are the top 5 reviews for this product? https://www.amazon.com/dp/B08N5KWB9H?ref=ods_ucc_kindle_B08N5KWB9H_rc_nd_ucc
Ask Func[get_info]:https://www.amazon.com/dp/B08N5KWB9H?ref=ods_ucc_kindle_B08N5KWB9H_rc_nd_ucc
Func[get_info] says: #doc1
A: "The King. M2 Max vs M1 Max 14" vs 16" which one?", " Great for DJ Using Serato", "It is what I expected"

Q: What are 2 most recent comments on this product? https://www.amazon.com/dp/B08N5KWB9H?ref=ods_ucc_kindle_B08N5KWB9H_rc_nd_ucc&th=1
Ask Func[get_info]: https://www.amazon.com/dp/B08N5KWB9H?ref=ods_ucc_kindle_B08N5KWB9H_rc_nd_ucc&th=1
Func[get_info] says: #doc1
A: "Received it as advertised", "Fast, lightweight beauty"

Q: What are some comments for this product?  https://www.amazon.com/Google-Pixel-Pro-Smartphone-Telephoto/dp/B0BCQVHYQY/ref=sr_1_4?keywords=android&qid=1682772142&sr=8-4&th=1
Ask Func[get_info]: https://www.amazon.com/Google-Pixel-Pro-Smartphone-Telephoto/dp/B0BCQVHYQY/ref=sr_1_4?keywords=android&qid=1682772142&sr=8-4&th=1
Func[get_info] says: #doc1
A: "Bought with confidence... now I regret buying off of false hype.", "Nice (Big) phone"
"""
agent = fixieai.CodeShotAgent(BASE_PROMPT, FEW_SHOTS)


@agent.register_func
def get_info(query: fixieai.Message) -> str:
    url = query.text
    response = requests.get(url)
    content_type = response.headers["Content-Type"]
    return fixieai.Message("#doc1", embeds={"doc1": fixieai.Embed(content_type, url)})

