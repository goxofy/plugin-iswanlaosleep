#import re
#import requests
import datetime
from plugins import register, Plugin, Event, logger, Reply, ReplyType


@register
class IsWanLaoSleep(Plugin):
    name = "iswanlaosleep"

    def did_receive_message(self, event: Event):
        pass

    def will_generate_reply(self, event: Event):
        query = event.context.query
        if query == self.config.get("command"):
            event.reply = self.reply()
            event.bypass()

    def will_send_reply(self, event: Event):
        pass

    def help(self, **kwargs) -> str:
        return "Use the command to get Leipzig time"

	def reply(self) -> Reply:
		reply = Reply(ReplyType.TEXT, "Failed to get Leipzig time")
		try:
			current_time = datetime.datetime.now()
			local_time = current_time.astimezone(datetime.timezone(datetime.timedelta(hours=2)))  # 设置时区为德国莱比锡的时区，即东欧标准时间
			reply = Reply(ReplyType.TEXT, f"丸佬那里现在是 {local_time}")
		except Exception as e:
			logger.error(f"Error occurred while getting Leipzig time: {e}")
		return reply
