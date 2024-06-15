"""
init pubsub abstraction
"""
import abc


class IPubSub(abc.ABC):
    """
    pubsub abstraction
    """
    async def publish(self, topic, message):
        """
        publish message to given topic
        """
        raise NotImplementedError("notimplemented yet!")
