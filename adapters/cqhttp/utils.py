from JustBot.objects import Friend, Group, Member
from JustBot.utils import Logger
from JustBot.application import HTTP_PROTOCOL

from aiohttp import request


class CQHttpUtils:
    def __init__(self, adapter):
        self.host = adapter.http_host
        self.port = adapter.http_port
        self.logger = adapter.logger

    async def __request_api(self, path: str, data: bool = True, params: dict = None) -> dict:
        async with request('GET', f'{HTTP_PROTOCOL}{self.host}:{self.port}{path}', params=params) as response:
            _ = await response.json()
            return _['data'] if data else _

    async def get_friend_by_id(self, user_id: int) -> Friend:
        for i in await self.__request_api('/get_friend_list'):
            if i['user_id'] == user_id:
                return Friend(i['nickname'], i['user_id'], i['remark'])
        self.logger.error(
            f'无法找到好友 `{user_id}`, 这可能是个内部错误!')

    async def get_group_by_id(self, group_id: int) -> Group:
        for i in await self.__request_api('/get_group_list'):
            if i['group_id'] == group_id:
                return Group(i['group_name'], i['group_id'], i['max_member_count'], i['member_count'],
                             i['group_level'], i['group_create_time'], i['group_memo'])
        self.logger.error(
            f'无法找到群 `{user_id}`, 这可能是个内部错误!')

    async def get_member_by_id(self, group_id: int, user_id: int) -> Member:
        data = await self.__request_api(f'/get_group_member_list', data=False, params={'group_id': group_id})
        if data['retcode'] == 100:
            self.logger.error(f'{data["wording"]}: `{user_id}`')
        else:
            for i in data['data']:
                if i['user_id'] == user_id:
                    return Member(await self.get_group_by_id(group_id), i['nickname'], i['user_id'], i['role'],
                                  i['last_sent_time'], i['join_time'])
            self.logger.error(
                f'无法找到群成员 `{user_id}`, 这可能是个内部错误!')
