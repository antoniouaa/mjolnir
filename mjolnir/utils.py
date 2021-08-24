import sys
import traceback
import pathlib


def exceptions(*exceptions):
    def deco(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exceptions as e:
                filename = sys.exc_info()[2].tb_frame.f_code.co_filename
                tb = traceback.TracebackException.from_exception(e)
                filename = pathlib.Path(tb.stack[-1].filename).parts[-2:]
                print(
                    f"[ERROR] {sys.exc_info()[0].__name__}: {str(sys.exc_info()[1]).title()}",
                    f"        at line {sys.exc_info()[2].tb_lineno} in {'/'.join(filename)}",
                    sep="\n",
                )
                sys.exit(1)

        return wrapper

    return deco
