from sentence_transformers import SentenceTransformer
import numpy as np
model_name = 'multi-qa-distilbert-cos-v1'
embedding_model = SentenceTransformer(model_name)

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):

    print(type(data))
    # embedded_documents = []
    # embeddings = []
    # for doc in data:
    #    question = doc['question']
    #    text = doc['text']
    #    qa_text = f'{question} {text}'
    #    doc["qa_embedding"] = embedding_model.encode(qa_text)
    #    embeddings.append(doc["qa_embedding"])
    #    embedded_documents.append(doc)

    #X = np.array(embeddings)
    #print(X.shape)
    #print(len(embedded_documents))
    # TODO: Mage AI converts embeddings to other type
    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'