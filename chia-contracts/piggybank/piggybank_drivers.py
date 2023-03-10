from chia.types.blockchain_format.coin import Coin
from chia.types.blockchain_format.sized_bytes import bytes32
from chia.type.blockchain_format.program import Program
from chia.types.condition_opcodes import ConditionOpcode
from chia.util.ints import uint64
from chia.util.hash import std_hash

from clvm.casts import int_to_bytes

from cdv.util.load_clvm import load_clvm

PIGGYBANK_MOD = load_clvm("piggybank-currying.clsp", "piggybank")

#Create a piggybank (create NFT with initial owner and IPFS hash)
def create_piggybank_puzzle(amount, cash_out_puzhash):
    return PIGGYBANK_MOD.curry(amount, cash_out_puzhash) #return curried version of the puzzle, returned as a "Program" object.

#generate a solution to contribute to a piggybank.
# pb_coin: the coin to contribute to 
def solution_for_piggybank(pb_coin, contribution_amount):
    #Program is how we do chialisp program code in Python
    return Program.to([pb_coin.amount, (pb_coin.amount + contribution_amount), pb_coin.puzzle_hash])

#Return the condition to assert the announcement. Remember, the annoucement is the "CREATE_COIN_ANNOUNCEMENT" condition in the contract.
def piggybank_announcement_assertion(pb_coin, contribution_amount):
    return [ConditionOpcode.ASSERT_COIN_ANNOUNCEMENT, std_hash(pb_coin.name() + int_to_bytes(pb_coin.amount + contribution_amount))]

def main():
    print("hello world")

if __name__ == "__main__":
    main()