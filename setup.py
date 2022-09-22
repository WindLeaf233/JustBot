from setuptools import setup

setup(
    name='JustBot',
    version='2.0.2',
    description='一个轻量的机器人框架',
    author='WindLeaf233',
    author_email='me@windleaf.ml',
    py_modules=[
        'JustBot.adapters.cqhttp.adapter',
        'JustBot.adapters.cqhttp.config',
        'JustBot.adapters.cqhttp.elements',
        'JustBot.adapters.cqhttp.event_handler',
        'JustBot.adapters.cqhttp.message_handler',
        'JustBot.adapters.cqhttp.utils',
        'JustBot.adapters.mirai.adapter',
        'JustBot.adapters.mirai.config',
        'JustBot.adapters.mirai.elements',
        'JustBot.adapters.mirai.message_handler',
        'JustBot.adapters.mirai.utils',
        'JustBot.apis.adapter_config',
        'JustBot.apis.adapter',
        'JustBot.apis.config',
        'JustBot.apis.element',
        'JustBot.apis.event',
        'JustBot.contact.friend',
        'JustBot.contact.group',
        'JustBot.contact.member',
        'JustBot.events.message_events',
        'JustBot.events.notice_events',
        'JustBot.matchers.command_matcher',
        'JustBot.matchers.keyword_matcher',
        'JustBot.utils.listener_manager',
        'JustBot.utils.listener',
        'JustBot.utils.logger',
        'JustBot.utils.matcher_util',
        'JustBot.utils.message_chain',
        'JustBot.utils.priority_queue'
    ]
)
