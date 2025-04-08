import wake.deployment
from wake.testing import *

from pytypes.csm.src.CSVerifier import CSVerifier


pre_chain = Chain()
post_chain = wake.deployment.Chain()

@pre_chain.connect(fork="http://localhost:8545@22217070")
@post_chain.connect("http://localhost:8545")
def test_deployment():
    cs_verifier = CSVerifier.deploy(
        withdrawalAddress="0xb9d7934878b5fb9610b3fe8a5e441e8fad7e293f",
        module="0xda7de2ecddfccc6c3af10108db212acbbf9ea83f",
        slotsPerEpoch=32,
        gIFirstWithdrawalPrev=bytes.fromhex("0000000000000000000000000000000000000000000000000000000000e1c004"),
        gIFirstWithdrawalCurr=bytes.fromhex("000000000000000000000000000000000000000000000000000000000161c004"),
        gIFirstValidatorPrev=bytes.fromhex("0000000000000000000000000000000000000000000000000056000000000028"),
        gIFirstValidatorCurr=bytes.fromhex("0000000000000000000000000000000000000000000000000096000000000028"),
        gIHistoricalSummariesPrev=bytes.fromhex("0000000000000000000000000000000000000000000000000000000000003b00"),
        gIHistoricalSummariesCurr=bytes.fromhex("0000000000000000000000000000000000000000000000000000000000005b00"),
        firstSupportedSlot=8626176,
        pivotSlot=11649024,
        chain=pre_chain,
        from_="0x0A0e4961A6b7f5D7b4807df876Ae068731102d44",
    )
    cs_verifier2 = CSVerifier("0x0c345dFa318f9F4977cdd4f33d80F9D0ffA38e8B", chain=post_chain)
    assert cs_verifier.code == cs_verifier2.code
    assert cs_verifier.address == cs_verifier2.address
