from enum import Enum
from loguru._logger import (Logger, Core)
from loguru import logger


class LogLevel(Enum):
    TRACE = 5
    DEBUG = 10
    INFO = 20
    SUCCESS = 25
    WARNING = 30
    ERROR = 40
    CRITICAL = 50


class LogHandler(Logger):
    def __init__(self):
        super().__init__(
            core=Core(),
            exception=None,
            depth=0,
            record=False,
            lazy=False,
            colors=False,
            raw=False,
            capture=True,
            patcher=None,
            extra={},
        )

    @property
    def trace(self): return self._handle_log(LogLevel.TRACE)
    @property
    def debug(self): return self._handle_log(LogLevel.DEBUG)
    @property
    def info(self): return self._handle_log(LogLevel.INFO)
    @property
    def success(self): return self._handle_log(LogLevel.SUCCESS)
    @property
    def warning(self): return self._handle_log(LogLevel.WARNING)
    @property
    def error(self): return self._handle_log(LogLevel.ERROR)
    @property
    def critical(self): return self._handle_log(LogLevel.CRITICAL)

    def exception(self, message: str, *args, **kwargs):
        r"""Convenience method for logging an ``'ERROR'`` with exception information."""
        options = (True,) + self._options[1:]
        super()._log("ERROR", None, False, options, message, args, kwargs)

    def log(self, level: LogLevel, message: str, *args, **kwargs):
        r"""Log ``message.format(*args, **kwargs)`` with severity ``level``."""
        return super().log(level.value, message, *args, **kwargs)

    # handler methods
    @property
    def catch(
        self,
        exception=Exception,
        *,
        level="ERROR",
        reraise=False,
        onerror=None,
        exclude=None,
        default=None,
        message="An error has been caught in function '{record[function]}', "
        "process '{record[process].name}' ({record[process].id}), "
        "thread '{record[thread].name}' ({record[thread].id}):"
    ):
        """Return a decorator to automatically log possibly caught error in wrapped function.

        This is useful to ensure unexpected exceptions are logged, the entire program can be
        wrapped by this method. This is also very useful to decorate |Thread.run| methods while
        using threads to propagate errors to the main logger thread.

        Note that the visibility of variables values (which uses the great |better_exceptions|_
        library from `@Qix-`_) depends on the ``diagnose`` option of each configured sink.

        The returned object can also be used as a context manager.

        Parameters
        ----------
        exception : |Exception|, optional
            The type of exception to intercept. If several types should be caught, a tuple of
            exceptions can be used too.
        level : |str| or |int|, optional
            The level name or severity with which the message should be logged.
        reraise : |bool|, optional
            Whether the exception should be raised again and hence propagated to the caller.
        onerror : |callable|_, optional
            A function that will be called if an error occurs, once the message has been logged.
            It should accept the exception instance as it sole argument.
        exclude : |Exception|, optional
            A type of exception (or a tuple of types) that will be purposely ignored and hence
            propagated to the caller without being logged.
        default : optional
            The value to be returned by the decorated function if an error occurred without being
            re-raised.
        message : |str|, optional
            The message that will be automatically logged if an exception occurs. Note that it will
            be formatted with the ``record`` attribute.

        Returns
        -------
        :term:`decorator` / :term:`context manager`
            An object that can be used to decorate a function or as a context manager to log
            exceptions possibly caught.

        Examples
        --------
        >>> @logger.catch
        ... def f(x):
        ...     100 / x
        ...
        >>> def g():
        ...     f(10)
        ...     f(0)
        ...
        >>> g()
        ERROR - An error has been caught in function 'g', process 'Main' (367), thread 'ch1' (1398):
        Traceback (most recent call last):
          File "program.py", line 12, in <module>
            g()
            └ <function g at 0x7f225fe2bc80>
        > File "program.py", line 10, in g
            f(0)
            └ <function f at 0x7f225fe2b9d8>
          File "program.py", line 6, in f
            100 / x
                  └ 0
        ZeroDivisionError: division by zero

        >>> with logger.catch(message="Because we never know..."):
        ...    main()  # No exception, no logs

        >>> # Use 'onerror' to prevent the program exit code to be 0 (if 'reraise=False') while
        >>> # also avoiding the stacktrace to be duplicated on stderr (if 'reraise=True').
        >>> @logger.catch(onerror=lambda _: sys.exit(1))
        ... def main():
        ...     1 / 0
        """
        self.__handle_pre_catch()
        return super().catch(exception, level=level, reraise=reraise, onerror=onerror, exclude=exclude, default=default, message=message)

    def _handle_log(self, level: LogLevel):
        def handler(message: str, *args, **kwargs):
            rf"""Log ``message.format(*args, **kwargs)`` with severity ``'{level}'``."""
            self.__handle_pre_log(level)
            options = (True,) + super()._options[1:]
            super()._log(level.value, None, False, options, message, args, kwargs)

        return handler

    def __handle_pre_log(self, level: LogLevel):
        print(f'__handle: {level}')

    def __handle_pre_catch(self):
        print('__handle_pre_catch')


# TODO: LogHandler testing
# log = LogHandler()
log = logger
