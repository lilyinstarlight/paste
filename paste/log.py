import log

from paste import config


pastelog = log.Log(config.log)
httplog = log.HTTPLog(config.log, config.httplog)
