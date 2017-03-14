"""Blockchain module."""

from passlib.apps import custom_app_context as pwd_context
import datetime


class Block(object):
    """Implementation of the block object."""

    def __init__(self, index, previous_hash, timestamp, data, block_hash):
        """Initialization of the block object."""
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.block_hash = block_hash


class Blockchain(object):
    """Implementatiion of the blockchain object."""

    def __init__(self):
        """Initialize the blockchain."""
        self._chain = [create_genesis_block()]


def calculate_hash(index, previous_hash, timestamp, data):
    """Generate a hash for a new block."""
    return pwd_context.hash(str(index) + previous_hash + str(timestamp) + data)


def generate_next_block(block_data, blockchain):
    """Generate a new block object."""
    previous_block = get_previous_block(blockchain)
    next_index = previous_block.index + 1
    next_timestamp = datetime.date.today()
    next_hash = calculate_hash(next_index, previous_block.block_hash, next_timestamp, block_data)
    return Block(next_index, previous_block.block_hash, next_timestamp, block_data, next_hash)


def create_genesis_block():
    """Return the initial block of the blockchain."""
    return Block(0, "0", 1465154705, "the genesis block", "$6$rounds=656000$3B8jwjIaMBHvO4Rk$73YPhzB2ntaF7iwP6i7YChVMK4RD9Qp6rBuqMYmNYgyGtuMCV.NB.JXLNi29oYNyQJTRERWRac8hABzcd9lHO1")


def add_block(block, blockchain):
    """Add a new block to the blockchain."""
    blockchain._chain.append(block)


def get_previous_block(blockchain):
    """Return the latest block of the blockchain."""
    return blockchain._chain[-1]
