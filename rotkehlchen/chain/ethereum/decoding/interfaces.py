from typing import TYPE_CHECKING, Any, Callable, Dict, List, Tuple

from rotkehlchen.types import ChecksumEthAddress

if TYPE_CHECKING:
    from rotkehlchen.chain.ethereum.decoding.base import BaseDecoderTools
    from rotkehlchen.chain.ethereum.manager import EthereumManager
    from rotkehlchen.user_messages import MessagesAggregator


class DecoderInterface():

    def __init__(
            self,
            ethereum_manager: 'EthereumManager',  # pylint: disable=unused-argument
            base_tools: 'BaseDecoderTools',  # pylint: disable=unused-argument
            msg_aggregator: 'MessagesAggregator',  # pylint: disable=unused-argument
    ) -> None:
        """This is the Decoder interface initialization signature

        To have smaller objects and since few decoders use most of the given objects
        we do not save anything here at the moment, but instead let it up to the individual
        decoder to choose what to keep"""
        return None

    def addresses_to_decoders(self) -> Dict[ChecksumEthAddress, Tuple[Any, ...]]:  # pylint: disable=no-self-use  # noqa: E501
        """Subclasses implement this to return the mappings of addresses to decode functions"""
        return {}

    def decoding_rules(self) -> List[Callable]:  # pylint: disable=no-self-use
        """
        Subclasses implement this to add new generic decoding rules to be attemped
        by the decoding process
        """
        return []
