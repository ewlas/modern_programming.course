from __future__ import annotations
from abc import ABC
from typing import Any, Optional


class Handler(ABC):
    """
    The Handler interface declares a method for building the chain of handlers.
    It also declares a method for executing a request.
    """

    def set_next(self, handler: Handler) -> Handler:
        pass

    def handle(self, request) -> Optional[str]:
        pass


class AbstractHandler(Handler):
    """
    The default chaining behavior can be implemented inside a base handler
    class.
    """

    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        # Returning a handler from here will let us link handlers in a
        # convenient way like this:
        # builder.set_next(plumber).set_next(electrician)
        return handler

    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)

        return None


"""
All Concrete Handlers either handle a request or pass it to the next handler in
the chain.
"""


class PlumberHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Pipe":
            return f"Plumber: I'll install the {request}"
        else:
            return super().handle(request)


class ElectricianHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Wire":
            return f"Electrician: I'll set up the {request}"
        else:
            return super().handle(request)


class CarpenterHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Wood":
            return f"Carpenter: I'll work with the {request}"
        else:
            return super().handle(request)


def client_code(handler: Handler) -> None:
    """
    The client code is usually suited to work with a single handler. In most
    cases, it is not even aware that the handler is part of a chain.
    """

    for material in ["Pipe", "Wood", "Cement"]:
        print(f"\nClient: I need {material} for construction.")
        result = handler.handle(material)
        if result:
            print(f"  {result}", end="")
        else:
            print(f"  {material} was left untouched.", end="")


if __name__ == "__main__":
    builder = PlumberHandler()
    electrician = ElectricianHandler()
    carpenter = CarpenterHandler()

    builder.set_next(electrician).set_next(carpenter)

    # The client should be able to send a request to any handler, not just the
    # first one in the chain.
    print("Chain: Plumber > Electrician > Carpenter")
    client_code(builder)
    print("\n")

    print("Subchain: Electrician > Carpenter")
    client_code(electrician)
