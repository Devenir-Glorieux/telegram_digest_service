import structlog
import orjson
from structlog.processors import TimeStamper, JSONRenderer
from core.config.settings import settings




def json_dumps(obj, **kwargs):
    return orjson.dumps(obj).decode("utf-8")


def configure_logging():
    structlog.configure(
        processors=[
            TimeStamper(fmt="iso", utc=True),
            structlog.processors.add_log_level,
            structlog.processors.CallsiteParameterAdder(
                parameters=[
                    structlog.processors.CallsiteParameter.MODULE,
                    structlog.processors.CallsiteParameter.FUNC_NAME,
                ]
            ),
            structlog.contextvars.merge_contextvars,
            JSONRenderer(serializer=json_dumps),
        ],
        context_class=dict,
        logger_factory=structlog.PrintLoggerFactory(),
        wrapper_class=structlog.make_filtering_bound_logger(settings.LOG_LEVEL),
        cache_logger_on_first_use=True,
    )


def get_logger():
    return structlog.get_logger()
