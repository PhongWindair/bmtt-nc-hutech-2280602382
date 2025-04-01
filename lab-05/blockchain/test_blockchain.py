from blockchain import Blockchain

my_blockchain = Blockchain()

my_blockchain.add_transaction(sender="Alice", receiver="Bob", amount=50)
my_blockchain.add_transaction(sender="Bob", receiver="Charlie", amount=30)  
my_blockchain.add_transaction(sender="Charlie", receiver="Alice", amount=20)

previous_block = my_blockchain.get_previous_block()
previous_proof = previous_block.proof
new_proof = my_blockchain.proof_of_work(previous_proof)
previous_hash = previous_block.hash
my_blockchain.add_transaction('Genesis', 'Miner', 1)
new_block = my_blockchain.create_block(new_proof, previous_hash)

for block in my_blockchain.chain:
    print(f"Block {block.index}:")
    print("Timestamp:", block.timestamp)
    print("Transactions:", block.transactions)
    print("Proof:", block.proof)
    print("Previous Hash:", block.previous_hash)
    print("Hash:", block.hash)
    print("--------------------------")

print("Blockchain valid:", my_blockchain.is_chain_valid(my_blockchain.chain))