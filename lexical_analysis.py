from evaluand import evaluand
import io
import pprint
import tokenize


pprint.pprint(
    list(tokenize.tokenize(io.BytesIO(bytes(evaluand, encoding="utf-8")).readline))
    )