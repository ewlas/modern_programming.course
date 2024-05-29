from __future__ import annotations
from abc import ABC
from typing import Any, Optional


class Handler(ABC):

    def set_next(self, handler: Handler) -> Handler:
        pass

    def handle(self, request) -> Optional[str]:
        pass


class AbstractHandler(Handler):

    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)

        return None


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

    print("Chain: Plumber > Electrician > Carpenter")
    client_code(builder)
    print("\n")

    print("Subchain: Electrician > Carpenter")
    client_code(electrician)
