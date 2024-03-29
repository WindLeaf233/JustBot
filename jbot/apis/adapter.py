from .adapter_config import AdapterConfig

from abc import ABCMeta, abstractmethod
from typing import Any, Union
from rich.traceback import install

install()


class Adapter(metaclass=ABCMeta):
    """
    > 说明
        适配器基类，用于实现适配器模式.
    """

    @abstractmethod
    def __init__(self) -> None:
        ...

    # TODO 添加文档
    @abstractmethod
    def _request_api(self, api_path: str) -> dict:
        ...

    @abstractmethod
    def check(self) -> None:
        ...

    @abstractmethod
    def login_info(self) -> dict:
        ...

    @abstractmethod
    def nick_name(self) -> str:
        ...

    @abstractmethod
    async def start_listen(self) -> Any:
        ...

    @abstractmethod
    async def send_message(self, target: "Contact", message: "MessageChain") -> Any:
        if not message.sendable:
            raise ValueError('消息链中含有不可被发送的消息!')
