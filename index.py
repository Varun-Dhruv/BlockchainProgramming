from typing import Union

from fastapi import FastAPI
from utils.blockchain import Blockchain
from classes.base import BlockData
blockchain=Blockchain()
app = FastAPI()


@app.post("/mine_block")
def mine_block(data:BlockData):
    previous_block = blockchain.print_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof, previous_hash,data=data.data)
 
    response = {'message': 'A block is MINED',
                'index': block['index'],
                'timestamp': block['timestamp'],
                'proof': block['proof'],
                'previous_hash': block['previous_hash']}
 
    return response

    
@app.get("/chain")
def chain():
    return {
        'chain':blockchain.chain,
        'length':len(blockchain.chain)
    }

@app.get("/chain/valid")
def check_validity():
    valid = blockchain.chain_valid(blockchain.chain)
    if valid:
        response = {'message': 'The Blockchain is valid.'}
    else:
        response = {'message': 'The Blockchain is not valid.'}
    return response
